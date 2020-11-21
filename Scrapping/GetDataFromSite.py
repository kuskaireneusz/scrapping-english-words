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
            soup = BeautifulSoup(self.__response('').text, 'html.parser')
        avaliableLang = self.__avaliableLang()
        searchElement = 'div'
        containerClass = 'dictionary'
        wordContainerCLass = 'ditem'
        container = soup.find(searchElement, class_=containerClass)
        words = container.findAll(searchElement, class_=wordContainerCLass)

        if (lang not in avaliableLang):
            print('Wybrałeś nie poprawny język')

        else:
            paragraph = 'p'
            paragraphClass = 'tr'
            for word in words:
                if (lang == avaliableLang[0]):
                    print(self.__soupFind(word, paragraph, paragraphClass).text)

                if (lang == avaliableLang[1]):
                    finedWord = word.find(paragraph).text
                    elementHalfLenght = int(len(finedWord) / 2)
                    print(word.find(paragraph).text[0: elementHalfLenght])

    def saveScrappedDictionary(self, url):
        parserType = 'html.parser'
        searchElement = 'div'
        containerClass = 'dictionary'
        wordContainerClass = 'ditem'
        paragraph = 'p'
        paragraphClass = 'tr'

        if url:
            soup = BeautifulSoup(self.__response(url).text, parserType)
        else:
            soup = BeautifulSoup(self.__response().text, parserType)

        container = soup.find(searchElement, class_=containerClass)
        words = container.findAll(searchElement, class_=wordContainerClass)
        polishWords = []
        englishWords = []

        for word in words:
            finedWord = word.find(paragraph).text
            elementLenght = int(len(finedWord) / 2)
            polishWords.append(self.__soupFind(word, paragraph, paragraphClass).text)
            englishWords.append(word.find(paragraph).text[0: elementLenght])

        mergedList = self.__mergeList(englishWords, polishWords)

        return mergedList

    def saveListToFile(self, url, fileName):
        fileExtension = '.txt'
        writeType = 'a'
        if (url):
            list = self.saveScrappedDictionary(url)
        else:
            list = self.saveScrappedDictionary()

        with open(fileName + fileExtension, writeType) as fp:
            fp.write('\n'.join('{}: {}'.format(x[0], x[1]) for x in list))

    def saveMultipleListTofile(self, isPaginationEnable, paginationCount, fileName):
        fileExtension = '.txt'
        writeType = 'a'
        preparedLink = self.__crateSiteNames(isPaginationEnable, paginationCount)
        words = []

        if (isinstance(preparedLink, list)):
            for item in preparedLink:
                words.append(self.saveScrappedDictionary(item))
        else:
            print('nie jestem linkkiem')

        for item in words:
            with open(fileName + fileExtension, writeType) as fp:
                fp.write('\n'.join('{}: {}'.format(x[0], x[1]) for x in item))
