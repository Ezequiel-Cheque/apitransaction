from src.pspsconfig import configuration
from src.pspsconfig.configuration_class import Configuration
from flask import request
import json

@configuration.route("/", methods=["GET"])
def get_settings():
    response = {
        "result": 0,
        "data": {},
        "error": ""
    }
    try:
        args = request.args
        if not (args.get("site") and args.get("tpId")):
            raise Exception("Parametros incompletos (tpId, site)")
        config = Configuration(args["tpId"], args["site"])
        response["data"] = config.get_configuration()
        response["result"] = 1
            
    except Exception as ex:
        response["error"] = str(ex)
    
    return response
    