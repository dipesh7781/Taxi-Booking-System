class booking():
    def __init__(self,booking_ID=0,pickup_Address=None,dropOff_Address=None,booking_Status=None,booking_Date=None,pickup_Time=None,userID=None,driverID=None):
        self.booking_ID=booking_ID
        self.pickup_Address=pickup_Address
        self.dropOff_Address=dropOff_Address
        self.booking_Status=booking_Status
        self.booking_Date=booking_Date
        self.pickup_Time=pickup_Time
        self.userID=userID
        self.driverID=driverID

#######Getters #####################33333
    def getbooking_ID(self):
        return self.booking_ID

    def getpickup_Address(self):
        return self.pickup_Address

    def getdropOff_Address(self):
        return self.dropOff_Address
    def getbooking_Status(self):
        return self.booking_Status
    def getbooking_Date(self):
        return self.booking_Date
    def getpickup_Time(self):
        return self.pickup_Time
    def getuserID(self):
        return self.userID
    def getdriverID(self):
        return self.driverID

################Setters##################
    def setbooking_ID(self,booking_ID):
        self.booking_ID=booking_ID

    def setpickup_Address(self,pickup_Address):
        self.pickup_Address=pickup_Address

    def setdropOff_Address(self,dropOff_Address):
        self.dropOff_Address=dropOff_Address

    def setbooking_Status(self,booking_Status):
        self.booking_Status=booking_Status

    def setbooking_Date(self,booking_Date):
        self.booking_Date=booking_Date

    def setpickup_Time(self,pickup_Time):
        self.pickup_Time=pickup_Time

    def setuserID(self,userID):
        self.userID=userID

    def setdriverID(self, driverID):
        self.driverID=driverID

###########String########################

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.booking_ID,self.pickup_Address,self.dropOff_Address,self.booking_Status,
                                            self.booking_Date,self.pickup_Time,self.userID, self.driverID)


