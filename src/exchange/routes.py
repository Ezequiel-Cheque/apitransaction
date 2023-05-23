from src.exchange import exchange
from flask import request

@exchange.route("/", methods=["GET"])
def index():
    from src.exchange.exchange_class import Exchange
    response = {
        "result": 0,
        "data": {},
        "error": ""
    }
    try:
        args = request.args
        
        if not (args.get("amount") and args.get("currency")):
            raise Exception("Parametros incompletos (amount, currency)")
        
        exchange = Exchange(args.get("amount"), args.get("currency"))
        exchangeData = exchange.exchange()
        
        response["result"] = 1
        response["data"] = exchangeData
    except Exception as ex:
        response["error"] = str(ex)
    
    return response