from SaveDataToFile.SaveFileStrategy import SaveFileStrategy


class SaveFileToTextStrategy(SaveFileStrategy):
    def __init__(self, fileName):
        self._fileExtension = '.txt'
        self._writeType = 'a'
        super().__init__(fileName)

    def saveDataToFile(self, list):
        with open(self.fileName + self._fileExtension,self._writeType) as fp:
            fp.write('\n'.join('{}: {}'.format(item[0], item[1]) for item in list))

    def saveMultipleDataToFile(self, listData):
        if(isinstance(listData, list)):
            for item in listData:
                with open(self.fileName + self._fileExtension, self._writeType) as fp:
                    fp.write('\n'.join('{}: {}'.format(x[0], x[1]) for x in item))
        else:
            print('Podany obiekt jest nie poprawny')
