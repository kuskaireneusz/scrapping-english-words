from bs4 import BeautifulSoup
import requests


class FetchSite:
    def __init__(self, url):
        self.url = url

    def _getSiteUrl(self, url):
        if (url):
            return requests.get(url)

        return requests.get(self.url)

    def _response(self, url):
        if url:
            return self._getSiteUrl(url)

        return self._getSiteUrl('')

    def _soupFind(self, target, element, elementclass):
        return target.find(element, class_=elementclass)

    def _avaliableLang(self):
        return ['pl', 'eng']

    def _mergeList(self, list1, list2):
        return [(list1[i], list2[i]) for i in range(0, len(list1))]

    def _crateSiteNames(self, pagination, pageSize):
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

    def saveScrappedDictionary(self, url=''):
        parserType = 'html.parser'
        searchElement = 'div'
        containerClass = 'dictionary'
        wordContainerClass = 'ditem'
        paragraph = 'p'
        paragraphClass = 'tr'

        if url:
            soup = BeautifulSoup(self._response(url).text, parserType)
        else:
            soup = BeautifulSoup(self._response(self.url).text, parserType)

        container = soup.find(searchElement, class_=containerClass)
        words = container.findAll(searchElement, class_=wordContainerClass)
        polishWords = []
        englishWords = []

        for word in words:
            finedWord = word.find(paragraph).text
            elementHalfLenght = int(len(finedWord) / 2)
            polishWords.append(self._soupFind(word, paragraph, paragraphClass).text)
            englishWords.append(word.find(paragraph).text[0: elementHalfLenght])

        mergedList = self._mergeList(englishWords, polishWords)

        return mergedList

    def createLinks(self, isPaginationEnable, paginationCount):
        return self._crateSiteNames(isPaginationEnable, paginationCount)

    def createMultiplePageData(self, linksList):
        words = []
        if (isinstance(linksList, list)):
            for item in linksList:
                words.append(self.saveScrappedDictionary(item))
            return words
        else:
            print('Nie poprawna format listy')
            return words

    def printScrappedWord(self, lang, url=''):
        soup = BeautifulSoup(self._response(url).text, 'html.parser')
        avaliableLang = self._avaliableLang()
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
                    print(self._soupFind(word, paragraph, paragraphClass).text)

                if (lang == avaliableLang[1]):
                    finedWord = word.find(paragraph).text
                    elementHalfLenght = int(len(finedWord) / 2)
                    print(word.find(paragraph).text[0: elementHalfLenght])



