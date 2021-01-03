import json

class Provinces:
    
    def __init__(self,province_name=None):
        with open('locations.json','r') as fp:
            data=json.load(fp)
        self.datas=data
        if province_name == None:
            self.province_name == province_name
        else:
            self.province_name=province_name
    
    def provinces(self):
        pro=[]
        d=self.datas['provinces']
        for province in d:
            pro.append(province)
            
        return pro

