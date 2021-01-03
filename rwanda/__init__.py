from .main import Provinces

app = Provinces()


def provinces(province_name=None):
  return app.provinces()

