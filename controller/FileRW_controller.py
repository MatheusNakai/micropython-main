from models.FileRW import FileRW

class FileRW_controller(object):

    def __init__(self, file_name):
        self.fileRW = FileRW(file_name)

    def read(self):
        return self.fileRW.read()

    def write(self,data):
        self.fileRW.write(data)
