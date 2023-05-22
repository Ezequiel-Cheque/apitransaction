pspsIds = {
    "NFTSLEARN": 125,
    "ASCENDINGBULL": 143,
    "FXTRATEGY": 145 
}
currencies = {
    "MX" : ["MXN"],
    "CL" : ["CLP"]
}
document = {
    "CL" : {"placeHolder" : "CI/RUT", "minLength" : 8, "maxLength" : 9},
    "MX" : {"placeHolder" : "CURP", "minLength" : 10, "maxLength" : 18},    
}
method = {
    "MX" : {
        "MXN" : [
            {"label" : "Transferencia", "value" : "transfer" , "logo" : ""},
            {"label" : "Pago en efectivo", "value" : "cash", "logo" : ""}
        ]
    },
    "CL" : {
        "CLP" : [
            {"label" : "Transferencia", "value" : "transfer", "logo" : ""},
            {"label" : "Pago en efectivo", "value" : "cash", "logo" : ""}
        ]
    }
}

toku_config = {
    "pspsIds": pspsIds,
    "currencies": currencies,
    "method": method
}