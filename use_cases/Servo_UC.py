from controller.FileRW_controller import FileRW_controller

class FileRW_UC(object):

    def __init__(self, file_name):
        self.file_rw_controller = FileRW_controller(file_name)
        
    def write(self,list_dict):
        self.file_rw_controller.write(list_dict)
        
    def read(self):
        return self.file_rw_controller.read()
