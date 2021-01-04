import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'locations.json')
class Provinces:
    
    def __init__(self,province_name=None):
        with open(my_file,'r') as fp:
            data=json.load(fp)
        self.datas=data
        
        if province_name is not None:
            self.province_name == province_name
    
    def provinces(self):
        pro=[]
        d=self.datas['provinces']
        for province in d:
            pro.append(province)
            
        return pro