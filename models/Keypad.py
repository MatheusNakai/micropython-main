from machine import Pin

class Keypad(object):
    def __init__(self):
        self.col_list=[8,9,10,11]
        self.row_list=[12,13,14,15]
        for x in range(0,4):
            self.row_list[x]=Pin(self.row_list[x], Pin.OUT)
            self.row_list[x].value(1)
        for x in range(0,4):
            self.col_list[x] = Pin(self.col_list[x], Pin.IN, Pin.PULL_UP)
        self.key_map=[["1","4","7","*"],\
                ["2","5","8","0"],\
                ["3","6","9","#"],\
                ["A","B","C","D"]]        

    def Keypad4x4Read(self):
        for r in self.rows:
            r.value(0)
            result=[self.cols[0].value(),self.cols[1].value(),self.cols[2].value(),self.cols[3].value()]
            if min(result)==0:
                key=self.key_map[int(self.rows.index(r))][int(result.index(0))]
                r.value(1) # manages key keept pressed
                return(key)
            r.value(1)
    