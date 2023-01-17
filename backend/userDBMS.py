import sys
from backend.connector import connect

def registration(userInfo):
    sql="""INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values=(userInfo.getuserID(),userInfo.getname(),userInfo.getemail(),userInfo.getcontact_number(),userInfo.getpassword(),
            userInfo.getgender(),userInfo.getaddress())
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