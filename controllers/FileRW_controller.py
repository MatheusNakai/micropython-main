from models.FileRW import FileRW

class FileRW_controller(object):

    def __init__(self, file_name):
        self.fileRW = FileRW(file_name)

    def read_file(self, file_name):
        return self.fileRW.read_file(file_name)

    def write_file(self, file_name, data):
        self.fileRW.write_file(file_name, data)