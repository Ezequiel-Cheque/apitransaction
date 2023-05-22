from src.pspsconfig.psps_configurations import Config

def AscendingBull_config(country):
    config = Config("ASCENDINGBULL", country)
    
    config = [
        config.fairpay,
        config.toku,
        config.key2pay
    ]
    
    return config 