from src.pspsconfig.configurations_by_sites.AscendingBull import AscendingBull_config
from src.pspsconfig.configurations_by_sites.NfstLearn import NfstsLearn_config

class Config_by_sites():
    
    __site = ""
    __country = ""
    
    def __init__(self, site, country):
        self.__site = site
        self.__country = country
    
    def get_site_psps(self):
        sites = {
            "ASCENDINGBULL": AscendingBull_config(self.__country),
            "NFTSLEARN": NfstsLearn_config(self.__country)
        }
        try:
            config = sites[self.__site]
            return config
        except:
            raise Exception("No hay configuraciones para este sitio")
        