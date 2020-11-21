from bs4 import BeautifulSoup
import requests


class FetchSite:
    def __init__(self, url):
        self.url = url

    def __getSiteUrl(self, url):
        if (url):
            return requests.get(url)

        return requests.get(self.url)

    def __response(self, url):
        if url:
            return self.__getSiteUrl(url)

        return self.__getSiteUrl('')

    def __soupFind(self, target, element, elementclass):
        return target.find(element, class_=elementclass)

    def __avaliableLang(self):
        return ['pl', 'eng']

    def __mergeList(self, list1, list2):
        return [(list1[i], list2[i]) for i in range(0, len(list1))]

    def __crateSiteNames(self, pagination, pageSize):
        siteNames = []
        slug = '/page/'

        if (pagination and int(pageSize) > 0):
            for item in range(0, int(pageSize)):
                if (item == 0):
                    siteNames.append(self.url)
                else:
                    siteNames.append(self.url + slug + str(item + 1))
        else:
            siteNames.append(self.url)
            print('podales niepoprawne wartosci dla paginacji')

        return siteNames

    def printScrappedWord(self, lang, url):
        if url:
            soup = BeautifulSoup(self.__response(url).text, 'html.parser')
        else:
            soup = BeautifulSoup(self.__response().text, 'html.parser')
        avaliableLang = self.__avaliableLang()
        findInSoup = soup.find('div', class_="dictionary")
        words = findInSoup.findAll('div', class_='ditem')

        if (lang not in avaliableLang):
            print('Wybrałeś nie poprawny język')

        else:
            for word in words:
                if (lang == avaliableLang[0]):
                    print(self.__soupFind(word, 'p', 'tr').text)

                if (lang == avaliableLang[1]):
                    finedWord = word.find('p').text
                    elementLenght = int(len(finedWord) / 2)
                    print(word.find('p').text[0: elementLenght])

    def saveScrappedDictionary(self, url):
        if url:
            soup = BeautifulSoup(self.__response(url).text, 'html.parser')
        else:
            soup = BeautifulSoup(self.__response().text, 'html.parser')

        findInSoup = soup.find('div', class_="dictionary")
        words = findInSoup.findAll('div', class_='ditem')
        polishWords = []
        englishWords = []

        for word in words:
            finedWord = word.find('p').text
            elementLenght = int(len(finedWord) / 2)
            polishWords.append(self.__soupFind(word, 'p', 'tr').text)
            englishWords.append(word.find('p').text[0: elementLenght])

        mergedList = self.__mergeList(englishWords, polishWords)

        return mergedList

    def saveListToFile(self, url, fileName):
        if (url):
            list = self.saveScrappedDictionary(url)
        else:
            list = self.saveScrappedDictionary()

        with open(fileName + '.txt', 'a') as fp:
            fp.write('\n'.join('{}: {}'.format(x[0], x[1]) for x in list))

    def saveMultipleListTofile(self, isPaginationEnable, paginationCount, fileName):
        preparedLink = self.__crateSiteNames(isPaginationEnable, paginationCount)
        words = []

        if (isinstance(preparedLink, list)):
            for item in preparedLink:
                words.append(self.saveScrappedDictionary(item))
        else:
            print('nie jestem linkkiem')

        for item in words:
            with open(fileName + '.txt', 'a') as fp:
                fp.write('\n'.join('{}: {}'.format(x[0], x[1]) for x in item))
