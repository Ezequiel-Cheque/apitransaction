from src.pspsconfig.psps_configurations.toku import toku_config
from src.pspsconfig.psps_configurations.key2pay import key2pay_config
from src.pspsconfig.psps_configurations.fairpay import Fairpay

class Config_main:
    
    __name = ""
    __id = 0
    __currencies = {}
    __method = {}
    
    def __init__(self, name, site, country, config):
        self.__name = name
        self.__id = config["pspsIds"][site]
        self.__currencies = config["currencies"][country]
        self.__method = config["method"][country]
    
    @property
    def config(self):
        return {
            "name": self.__name,
            "pspId": self.__id,
            "currency": self.__currencies,
            "method": self.__method
        }

class Config():
    
    __site = ""
    __country = ""
    
    def __init__(self, site, country):
        self.__site = site
        self.__country = country
    
    @property
    def toku(self):
        config_toku = Config_main("Toku", self.__site, self.__country, toku_config)
        return config_toku.config
    
    @property
    def key2pay(self):
        config_key2pay = Config_main("Key2pay", self.__site, self.__country, key2pay_config)
        return config_key2pay.config
    
    @property
    def fairpay(self):
        fairpay = Fairpay(self.__site, self.__country)
        return fairpay.config