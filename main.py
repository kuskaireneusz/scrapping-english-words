from Scrapping.GetDataFromSite import FetchSite
from SaveDataToFile.SaveFileToTextStrategy import SaveFileToTextStrategy
from SaveDataToFile.SaveFileToPdfStrategy import SaveFileToPdfStrategy

class Context():
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def saveFile(self, list):
        return self._strategy.saveDataToFile(list)

    def saveMultipleFile(self, listData):
        return self._strategy.saveMultipleDataToFile(listData)

# siteNameA2 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-a2')
# siteNameA2.saveMultipleListTofile(True, 22, 'a2-words')
#
# siteNameB1 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-b1')
# siteNameB1.saveMultipleListTofile(True, 31, 'b1-words')
#
# siteNameB2 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-b2')
# siteNameB2.saveMultipleListTofile(True, 52, 'b2-words')

a1Object = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-a1')
a1Words = a1Object.saveScrappedDictionary()
a1Links = a1Object.createLinks(True, 13)
a1Data = a1Object.createMultiplePageData(a1Links)

a2Object = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-a2')
a2Words = a2Object.saveScrappedDictionary()
a2Links = a2Object.createLinks(True, 22)
a2Data = a2Object.createMultiplePageData(a2Links)

saveFileContextA1 = Context(SaveFileToTextStrategy('a1-words'))
saveFileContextA1.saveMultipleFile(a1Data)

saveFileContextA2 = Context(SaveFileToTextStrategy('a2-words'))
saveFileContextA2.saveMultipleFile(a2Data)

#
# saveFileContext = Context(SaveFileToPdfStrategy('test'))
#
# saveFileContext.saveFile('file name', 'list')


# saveFile = SaveFileToTextStrategy('test')
# #
# saveFile.saveDataToFile()
#
# saveFilePdf = SaveFileToPdfStrategy('pdf test')
#
# saveFilePdf.saveDataToFile()