import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'locations.json')


class Rwanda:

    def __init__(self, province_name=None):
        with open(my_file, 'r') as fp:
            data = json.load(fp)
        self.datas = data
        self.provinces_names = [province['name']
                                for province in self.datas['provinces']]

    def provinces(self):
        return self.provinces_names
