import sys
from backend.connector import connect

def insertbooking(booking):
    sql="""INSERT INTO booking VALUES(%s, %s, %s, %s, %s, %s, %s,%s) """
    values =(booking.getbooking_ID(),booking.getpickup_Address(),booking.getdropOff_Address(),booking.getbooking_Status(),
            booking.getbooking_Date(),booking.getpickup_Time(),booking.getuserID(), booking.getdriverID())
    result=False
    try:
        con=connect()
        cursor=con.cursor()
        cursor.execute(sql,values)
        con.commit()
        cursor.close()
        con.close()
        result=True
    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return result

def customertable(user_id):
    conn=None
    sql="""SELECT * FROM user WHERE userID=%s"""
    values=(user_id)
    result=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error",sys.exc_info())

    finally:
        del values, sql,conn
        return result


def usertable(book):
    sql=""" SELECT booking_ID,pickup_Address,dropOff_Address,pickup_Time,booking_Date, booking_Status FROM booking WHERE userID=%s AND  NOT booking_Status='Confirmed' order by booking_Status desc"""
    values=(book,)
    cuspending=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        cuspending=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return cuspending


def delete_booking(book):
    sql=""" DELETE FROM booking WHERE booking_ID=%s"""
    values=(book,)
    deleteResult=False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        deleteResult=True

    except:
        print("Error:",sys.exc_info())
    finally:
        del values,sql
        return deleteResult


def cust_update_booking(Info):
    sql="""UPDATE booking SET pickup_Address=%s,dropOff_Address=%s,booking_Date=%s, pickup_Time=%s WHERE booking_ID=%s"""
    values =(Info.getpickup_Address(),Info.getdropOff_Address(),Info.getbooking_Date(),Info.getpickup_Time(),Info.getbooking_ID())
    customerResult=False

    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        customerResult=True

    except:
        print("Error",sys.exc_info())
    finally:
        del values,sql,conn
        return customerResult

def bookingtable55():
    conn=None
    sql="""SELECT * FROM booking WHERE booking_Status='Pending'"""
    result=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error",sys.exc_info())
    finally:
        del  sql,conn
        return result

def bookingtable56():
    conn=None
    sql="""SELECT * FROM booking WHERE booking_Status='Completed'"""
    result56=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result56=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error",sys.exc_info())
    finally:
        del  sql,conn
        return result56

def assigndriverupdate(bid):
    sql = """UPDATE booking SET driverID=%s , booking_Status='Confirmed' WHERE booking_ID=%s"""
    values = (bid.getdriverID(), bid.getbooking_ID())
    confirmbookingresult = False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        confirmbookingresult=True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql, values
        return confirmbookingresult

def drivernewbooking(bid):
    sql = """SELECT * FROM booking WHERE booking_Status='Confirmed' AND driverID=%s"""
    value = [bid.getdriverID()]
    drivernewbookingresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, value)
        drivernewbookingresult=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql, value
        return drivernewbookingresult

def driveroldbooking(bid):
    sql = """SELECT * FROM booking WHERE booking_Status='Completed' AND driverID=%s"""
    values = (bid,)
    driveroldbookingresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        driveroldbookingresult=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql, values
        return driveroldbookingresult

def completebooking(bid):
    sql = """UPDATE booking SET booking_Status='Completed' WHERE booking_ID=%s"""
    values = (bid,)
    completebookingresult = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        completebookingresult = True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql, values
        return completebookingresult