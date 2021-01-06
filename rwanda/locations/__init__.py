import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'locations.json')
class Rwanda:
    
    def __init__(self,province_name=None):
        with open(my_file,'r') as fp:
            data=json.load(fp)
        self.datas=data
        self.provinces=[]
        self.districts=[]
        self.sectors=[]
        self.cells=[]
        self.villages=[]

        for p in self.datas['provinces']:
            self.provinces.append(p['name'])
            for district in p['districts']:
                self.districts.append(district['name'])
                for sector in district['sectors']:
                    self.sectors.append(sector['name'])
                    for cell in sector['cells']:
                        self.cells.append(cell['name'])
                        for vilages in cell['villages']:
                            self.villages.append(vilages['name'])

        if province_name is not None:
            self.province_name == province_name
    
    def all_provinces(self):
        return self.provinces

    def all_districts(self):
        return self.districts

    def all_sectors(self):
        return self.sectors

    def all_cells(self):
        return self.cells

    def all_villages(self):
        return self.villages





        