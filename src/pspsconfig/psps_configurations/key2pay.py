pspsIds = {
    "CASHIER": 139,
    "FXTRATEGY": 133,
    "ASCENDINGBULL": 142
}
currencies = {
    "MX" : ["MXN"],
    "CL" : ["CLP"],
    "CO" : ["COP"],
    "BR" : ["BRL"],
    "CR" : ["CRC"],
    "PE" : ["PEN"]
}
method = {
    "MX" : {
        "MXN" : [
            {"label" : "Transferencia", "value" : "checkout", "logo" : ""}
        ]
    },
    "CL" : {
        "CLP" : [
            {"label" : "Transferencia", "value" : "checkout", "logo" : ""}
        ]
    },
    "CO" : {
        "COP" : [
            {"label" : "Transferencia", "value" : "checkout", "logo" : ""}
        ]
    },
    "BR" : {
        "BRL" : [
            {"label" : "Transferencia", "value" : "checkout", "logo" : ""}
        ]
    },
    "CR" : {
        "CRC" : [
            {"label" : "Transferencia", "value" : "checkout", "logo" : ""}
        ]
    },
    "PE" : {
        "PEN" : [
            {"label" : "Transferencia", "value" : "checkout", "logo" : ""}
        ]
    }
}

key2pay_config = {
    "pspsIds": pspsIds,
    "currencies": currencies,
    "method": method
}