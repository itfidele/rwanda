import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(f'{THIS_FOLDER}/locations', 'locations.json')


class Places:

    def __init__(self, province_name:str=None):
        with open(my_file, 'r') as fp:
            data = json.load(fp)
        self.datas = data
        self.provinces_names = [province['name']
                                for province in self.datas['provinces']]
        

    def provinces(self)->list[str]:
        return self.provinces_names
    
    def districts(self,province_name):
        """Returns all districts from a province

        Args:
            province_name ([string]): [province name]
        """
        pass

    def sectors(self,district_name):    
        """Returns all sectors from a district

        Args:
            district_name ([string]): [district name]
        """
        pass

    def cells(self,sector_name):
        """Returns all cells from a sector

        Args:
            sector_name ([string]): [sector name]
        """
        pass

    def villages(self,cell_name):
        """Returns all villages from a cell

        Args:
            cell_name ([string]): [cell name]
        """
        pass

    def get_province(self,province_name):
        """Returns a province

        Args:
            province_name ([string]): [province name]
        """
        pass

    def get_district(self,district_name):
        """Returns a district

        Args:
            district_name ([string]): [district name]
        """
        return district_name

    def get_sector(self,sector_name):
        """Returns a sector

        Args:
            sector_name ([string]): [sector name]
        """
        pass
