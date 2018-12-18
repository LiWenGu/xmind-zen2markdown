import json
from zipfile import ZipFile

content_json = "content.json"
xmindFileContent = [content_json]

class XmindFileParser:

    @classmethod
    def parse(self, filePath):
        file_content = self.__unzip(filePath)
        file_json_content = self.__parseJson(file_content)
        return file_json_content

    @staticmethod
    def __unzip(filePath):
        with ZipFile(filePath) as xmindFile:
            for f in xmindFile.namelist():
                for key in xmindFileContent:
                    if f == key:
                        with xmindFile.open(f) as contentJsonFile:
                            return contentJsonFile.read().decode('utf-8')

    @staticmethod
    def __parseJson(fileContent):
        return json.loads(fileContent)
