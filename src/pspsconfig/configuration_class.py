import json
from src.pspsconfig.models import Crmcustomer, Crmpspcat
import requests
from src.pspsconfig.configurations_by_sites import Config_by_sites


class Configuration(Config_by_sites):

    __tpId = ""
    __country = ""
    __bussinessUnit = ""
    __site = ""
    __psps = []

    def __init__(self, tpId, site):
        customer = self.get_customer_info(tpId)
        super().__init__(site, customer.country)
        self.__tpId = tpId
        self.__country = customer.country
        self.__bussinessUnit = customer.idCrmBusinessUnit
        self.__site = site
        self.__psps = self.get_site_psps()

    def get_customer_from_affico360(self, tpId):
        url = f"https://api.affico360.com/lead/tpId/{tpId}"
        headers = {
            "accept": "application/json",
            "affico-360-affiliate-key": "$2b$08$FKTM/4LzpNVLBWUZG1u2Necng9x5k6Vsz9Ndx8l3CmCDnFSTTpVBe"
        }
        requ = requests.request("GET", url, headers=headers)
        data = requ.json()
        if data.get("data") and len(data["data"]) > 0:
            return data["data"][0]
        else:
            return False 
            
    
    def get_customer_info(self, tpId):
        crmCustomer = Crmcustomer()
        customerData = crmCustomer.customer_data(tpId)
        if not customerData:
            affico360Data = self.get_customer_from_affico360(tpId)
            if not affico360Data:
                raise Exception("No existe el usuario")
            return {
                "tpId": affico360Data["tpId"],
                "country": affico360Data["country"],
                "bu": 8
            }
        return customerData

    def get_data(self):
        data = {
            "tpId": self.__tpId,
            "country": self.__country,
            "BU": self.__bussinessUnit
        }
        return data
        
    @staticmethod
    def get_psp_id(psp):
        return psp["pspId"]
    
    @staticmethod
    def str_keys(key):
        return f"{key},"

    def get_psps_info(self):
        crmpspcat = Crmpspcat()
        keys = list(map(self.get_psp_id, self.__psps))
        settings = []
        for idCrmPspCat in keys:
            setting = crmpspcat.get_setting(idCrmPspCat)
            settings.append({
                **setting,
                "id": idCrmPspCat
            })
        return settings
    
    def validate_psp(self, setting):
        newSetting = {}
        for psp in self.__psps:
            if psp["pspId"] == setting["id"]:
                if setting["available"] == True:
                    newSetting = {
                        **psp,
                        "available": True if (self.__country in setting["availableCountries"] and self.__bussinessUnit in setting["availableBusinessUnits"]) else False,
                        "min": setting["minAmount"],
                        "max": setting["maxAmount"]
                    }
                else:
                    newSetting = {
                    **psp,
                    "available": setting["available"],
                    "min": setting["minAmount"],
                    "max": setting["maxAmount"]
                }
        return newSetting

    def get_configuration(self):
        settings = self.get_psps_info()
        availables = list(map(self.validate_psp, settings))
        return availables
