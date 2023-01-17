import sys

from backend.connector import connect

def drivreg(driverInfo):
    sql="""INSERT INTO driver VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(driverInfo.getdriverID(),driverInfo.getname(),driverInfo.getaddress(),driverInfo.getnumber(),driverInfo.getemail(),
            driverInfo.getlicenseno(),driverInfo.gettaxino(),driverInfo.getpassword(),driverInfo.getstatus())
    result= False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True
    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return result


def availabledriver111():
    sql="""SELECT driverID FROM driver WHERE status ='Available'"""
    result= None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del sql
        return result

def driverstatusupdate(did):
    sql = """UPDATE driver SET status=%s WHERE driverID=%s"""
    values=(did.getstatus(), did.getdriverID())
    driverstatusresult=False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        driverstatusresult=True
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return driverstatusresult