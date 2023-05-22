from utils.db import db

class Crmpspcat(db.Model):
    idCrmPspCat = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    settings = db.Column(db.JSON)
    visibility = db.Column(db.Integer)
    insertDate = db.Column(db.TIMESTAMP)
    endDate = db.Column(db.TIMESTAMP)
    active = db.Column(db.Integer)

    @staticmethod
    def get_by_id(id):
        return Crmpspcat.query.get(id)
    
    @staticmethod
    def get_setting(idCrmPspCat):
        data = Crmpspcat.query.filter_by(idCrmPspCat=idCrmPspCat).first()
        return data.settings
        
        
class Crmcustomer(db.Model):
    crmId = db.Column(db.VARCHAR(20), primary_key=True)
    tpId = db.Column(db.VARCHAR(30))
    firstName = db.Column(db.VARCHAR(75))
    lastName = db.Column(db.VARCHAR(75))
    email = db.Column(db.VARCHAR(100))
    profileImage = db.Column(db.VARCHAR(150))
    phoneCode = db.Column(db.VARCHAR(5))
    phoneNumber = db.Column(db.VARCHAR(15))
    password = db.Column(db.VARCHAR(50))
    idCrmAffiliate = db.Column(db.Integer)
    insertIp = db.Column(db.VARCHAR(100))
    transactionIp = db.Column(db.VARCHAR(20))
    userAgent = db.Column(db.Text)
    street = db.Column(db.VARCHAR(100))
    streetJob = db.Column(db.VARCHAR(100))
    colony = db.Column(db.VARCHAR(100))
    colonyJob = db.Column(db.VARCHAR(100))
    city = db.Column(db.VARCHAR(75))
    cityJob = db.Column(db.VARCHAR(75))
    state = db.Column(db.VARCHAR(50))
    zipCode = db.Column(db.VARCHAR(15))
    zipCodeJob = db.Column(db.VARCHAR(15))
    additionalInformation = db.Column(db.VARCHAR(255))
    country = db.Column(db.VARCHAR(5))
    countryJob = db.Column(db.VARCHAR(5))
    birthDate = db.Column(db.Date)
    birthCountry = db.Column(db.VARCHAR(5))
    idCrmCustomerStatusCat = db.Column(db.Integer)
    idCrmBusinessUnit = db.Column(db.Integer)
    referral = db.Column(db.Text)
    lastNote = db.Column(db.VARCHAR(600))
    campaignId = db.Column(db.VARCHAR(500))
    originalPartner = db.Column(db.Integer)
    source = db.Column(db.Text)
    owner = db.Column(db.Integer)
    complianceOwner = db.Column(db.Integer)
    minAmount = db.Column(db.Integer)
    ftd = db.Column(db.SMALLINT)
    ftdDate = db.Column(db.TIMESTAMP)
    affiliateFtdDate = db.Column(db.TIMESTAMP)
    sendToCrm = db.Column(db.Enum("1", "0", "SENT"))
    accountId = db.Column(db.VARCHAR(50))
    kyc = db.Column(db.Enum("R", "N/R"))
    agent = db.Column(db.Integer)
    gender = db.Column(db.Enum("FEMALE", "MALE"))
    activityJob = db.Column(db.VARCHAR(100))
    salary = db.Column(db.Integer)
    depositAmount = db.Column(db.Integer)
    insertDate = db.Column(db.TIMESTAMP)
    insertMinute = db.Column(db.Integer)
    updateDate = db.Column(db.TIMESTAMP)
    active = db.Column(db.SMALLINT)
    affiliateActive = db.Column(db.SMALLINT)
    retry = db.Column(db.SMALLINT)
    rhinoUpdated = db.Column(db.SMALLINT)
    integrationCrm = db.Column(db.Integer)
    
    @staticmethod
    def customer_data(tpId):
        return Crmcustomer.query.filter_by(tpId=tpId).first()
    