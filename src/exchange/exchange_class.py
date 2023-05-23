import datetime
import requests
import json

class Exchange:
    """
        This class recived an amount, and a currency, and return the exchange value to local currency,
        we do a request to an exchange api, in our mornex server
    """
    __api_exchange = ""
    __amount = 0
    __currency = ""
    __comissionFactor = 1.07
    
    def __init__(self, amount, currency):
        self.__amount = float(amount)
        self.__currency = currency.upper()
        self.__api_exchange = self.api_exchange()
        
        
    def api_exchange(self):
        """ to consult the api, we need to built the api url,
            because everyday there are a different json, with the current exchange
        """
        x = datetime.datetime.now()
        pathMonth = x.strftime("%Y%m")
        curdate = f"{pathMonth}{x.strftime('%d')}"
        url = f"https://webservicesnt.org/exchangeapi/{pathMonth}/exchange.{curdate}.json"
        return url
    
    def get_exchange(self):
        """
            get the rate to the local currency, we need the higher round value
        """
        try:
            data = requests.request("GET", self.__api_exchange)
            exchangeData = data.json()
            rate = exchangeData["rates"][self.__currency]
            exchange = rate if rate > round(rate, 1) else round(rate)
            return exchange
        except:
            raise Exception("Error al obtener datos de exchange")
    
    def exchange(self):
        """
            return the correct exchange value, for MXN, if the exchange value is less than 20 MXN, we have to return 20 for dolar,
            for other countries we are gonna return the exchange value, without the commission factor
        """
        exchange = self.get_exchange()
        response = {
            "currency": self.__currency,
            "amount": None
        }
        if self.__currency == "MXN":
            exchangeComission = exchange * self.__comissionFactor
            # print(exchangeComission * self.__amount)
            response["amount"] = exchangeComission * self.__amount if exchangeComission > 20 else 20 * self.__amount
        else:
            response["amount"] = exchange * self.__amount if self.__currency != "USD" else self.__amount * 1
        
        return response