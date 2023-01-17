class Admin():
    def __init__(self, admin_ID=0, fullname=None, password=None, contactNo=None, email=None):
        self.admin_ID = admin_ID
        self.fullname=fullname
        self.password=password
        self.contactNo=contactNo
        self.email=email

    def getadmin_ID(self):
        return self.admin_ID

    def getfullname(self):
        return self.fullname

    def getpassword(self):
        return self.password

    def getcontactNo(self):
        return self.contactNo

    def getemail(self):
        return self.email

    def setadmin_ID(self, admin_ID):
        self.admin_ID= admin_ID

    def setfullname(self, fullname):
        self.fullname=fullname

    def setpassword(self, password):
        self.password=password

    def setcontactNo(self, contactNo):
        self.contactNo=contactNo

    def setemail(self, email):
        self.email=email

    def __str__(self):
        return '{},{},{},{},{}'.format(self.admin_ID, self.fullname, self.password, self.contactNo, self.email)