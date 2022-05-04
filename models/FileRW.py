import ujson

class FileRW(object):
    
    def __init__(self, file_name:str):
        self.file_name = file_name
        
    
    def write(self,list_dict):
        try:
            with open('json.txt','a') as f:
                for user in list_dict:
                    json = ujson.dumps(user)
                    print()
                    f.write(f'{json}\n')
                    
        except:
            print("Error writing to file")


    def read(self):
        l=[]
        try:
            with open('json.txt','r') as f:
            
                for i in f:
                    line=i.strip()
                    l.append(ujson.loads(line))
            return l    
        except:
            print("Error reading file")
