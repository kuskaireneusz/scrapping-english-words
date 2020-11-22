from SaveDataToFile.SaveFileStrategy import SaveFileStrategy

class SaveFileToPdfStrategy(SaveFileStrategy):
    def __init__(self, fileName):
        super().__init__(fileName)

    def saveDataToFile(self, list):
        print(self.fileName, 'from pdf')

    def saveMultipleDataToFile(self, list):
        print(self.fileName, 'from pdf')