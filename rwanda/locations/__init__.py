import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'locations.json')
class Rwanda:
    
    def __init__(self,province_name=None):
        with open(my_file,'r') as fp:
            data=json.load(fp)
        self.datas=data
        if province_name is not None:
            self.province_name == province_name
    
    def all_provinces(self):
        pro=[]
        d=self.datas['provinces']
        for province in d:
            pro.append(province['name'])
            
        return pro

    def all_districts(self):
        di=[]
        d=self.datas['provinces']
        for districts in d:
            for district in districts['districts']:
                di.append(district['name'])
        return di

    def all_sectors(self):
        se=[]
        d=self.datas['provinces']
        for p in d:
            for district in p['districts']:
                for sector in district['sectors']:
                    se.append(sector['name'])
        
        return se