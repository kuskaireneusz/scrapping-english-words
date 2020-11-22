from abc import abstractmethod, ABC


class SaveFileStrategy(ABC):
    def __init__(self, fileName):
        self.fileName = fileName

    @abstractmethod
    def saveDataToFile(self, list): pass

    @abstractmethod
    def saveMultipleDataToFile(self, list): pass
