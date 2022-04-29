import ujson

class FileRW(object):
    
    def __init__(self, file_name:str):
        self.file_name = file_name
        
    
    def write(list_dict):
        try:
            with open('json.txt','a') as f:
                for user in list_dict:
                    json = ujson.dump(user)
                    f.write(f'{json}\n')
        except:
            print("Error writing to file")


    def read():
        l=[]
        try:
            with open('json.txt','r') as f:
                l = ujson.load(f)
            return l
        except:
            print("Error reading file")