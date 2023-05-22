import requests
import json

pspsId = {
    "ASCENDINGBULL": 90
}

class Fairpay:
    __name = ""
    __country = ""
    __data = {}
    __id = ""
    
    def __init__(self, site, country):
        self.__name = "Fairpay"
        self.__country = country
        self.__id = pspsId[site]
        self.__data = self.getFairPaymentMethods(site, country)
        
    def getFairPaymentMethods(self, site, country):
        params = {
            "site": site,
            "action": "getMethods",
            "country": country
        }
        headers = {
            "Content-Type": "application/json"
        }
        req = requests.request("POST", "https://webservicesnt.org/phpPunkaso/fairpay/index.php", data=json.dumps(params), headers=headers)
        response = req.json()
        if not response["data"]:
            return {}
        return response["data"]
    
    def getcurrencies(self):
        data = self.__data
        currencies = []
        for method in data:
            for currency in method["currencies"]:
                if currency in currencies:
                    continue
                currencies.append(currency)
        return currencies
        
    def getMethodsByCurrency(self, currency):
        data = self.__data
        methods = []
        for method in data:
            if currency in method["currencies"]:
                methods.append({
                    "type": method["channel"],
                    "label": method["name"],
                    "logo": method["imageUrl"],
                    "value": method["uid"]
                })
        return methods

    def getMethods(self, currencies):
        methods = {}
        for currency in currencies:
            methodsByCurrency = self.getMethodsByCurrency(currency)
            methods = {
                **methods,
                currency: methodsByCurrency
            }
        return methods

    @property
    def config(self):
        currencies = self.getcurrencies()
        configuration = {
            "name" : self.__name,
            "pspId": self.__id,
            "currency": {
                self.__country : currencies
            },
            "method": {
                self.__country : self.getMethods(currencies)
            }
        }   
        return configuration
    
