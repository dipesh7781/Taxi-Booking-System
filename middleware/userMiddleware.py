class User():
    def __init__(self, userID=0,name=None,email=None, contact_number=None, password=None, gender= None,address=None):
        self.userID=userID
        self.name= name
        self.contact_number= contact_number
        self.email= email
        self.password= password
        self.gender= gender
        self.address=address


        #Getters

    def getuserID(self):
        return self.userID

    def getname(self):
        return self.name

    def getemail(self):
        return self.email

    def getcontact_number(self):
        return self.contact_number

    def getpassword(self):
        return self.password

    def getgender(self):
            return self.gender

    def getaddress(self):
        return self.address

    #SEtters

    def setuserID(self,userID):
        self.userID=userID

    def setname(self,name):
        self.name=name

    def setemail(self,email):
        self.email=email

    def setcontact_number(self,contact_number):
        self.contact_number=contact_number

    def setpassword(self,password):
        self.password=password

    def setgender(self, gender):
        self.gender = gender

    def setaddress(self,address):
        self.address=address


##############    STR   ######################

    def __str__(self):
        return"{},{},{},{},{},{},{}",format(self.userID,self.name,self.email,self.contact_number,self.password,self.gender,self.address)






