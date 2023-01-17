import sys

from backend.connector import connect

def login(userInfo):
    sql="""SELECT * FROM user WHERE email=%s AND password=%s"""
    values= (userInfo.getemail(),userInfo.getpassword())
    user1=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        user1=cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return user1

def login2(adminInfo):
    sql="""SELECT * FROM admin WHERE email=%s AND password=%s"""
    values= (adminInfo.getemail(),adminInfo.getpassword())
    adminresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        adminresult=cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return adminresult

def login3(driverInfo):
    sql="""SELECT * FROM driver WHERE email=%s AND password=%s"""
    values= (driverInfo.getemail(),driverInfo.getpassword())
    driverresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        driverresult=cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return driverresult