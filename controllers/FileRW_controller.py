from models.FileRW import FileRW

class FileRW_controller(object):

    def __init__(self, file_name):
        self.fileRW = FileRW(file_name)

    def read(self, file_name):
        return self.fileRW.read(file_name)

    def write(self, file_name, data):
        self.fileRW.write(file_name, data)