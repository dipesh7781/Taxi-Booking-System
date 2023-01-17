class Driver():
    def __init__(self,driverID=0,name=None,address=None,number=None,email=None,licenseno=None,taxino=None,password=None, status=None):
        self.driverID=driverID
        self.name=name
        self.address=address
        self.number=number
        self.email=email
        self.licenseno=licenseno
        self.taxino=taxino
        self.password=password
        self.status=status

################Getters##############################
    def getdriverID(self):
            return self.driverID

    def getname(self):
            return self.name

    def getaddress(self):
        return self.address

    def getnumber(self):
        return self.number

    def getemail(self):
        return self.email

    def getlicenseno(self):
        return self.licenseno

    def gettaxino(self):
        return self.taxino

    def getpassword(self):
        return self.password

    def getstatus(self):
        return self.status


#################Setters#######################################33

    def setdriverID(self,driverID):
        self.driverID=driverID

    def setname(self,name):
        self.name=name

    def setaddress(self,address):
        self.address=address

    def setnumber(self,number):
        self.number=number

    def setemail(self,email):
        self.email=email

    def setlicenseno(self,licenseno):
        self.licenseno=licenseno

    def settaxino(self,taxino):
        self.taxino=taxino

    def setpassword(self,password):
        self.password=password

    def setstatus(self, status):
        self.status=status

#############String####################33333
    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}",format(self.driverID,self.name,self.address,self.number,self.email,self.licenseno,
                                                self.taxino,self.password, self.status)









