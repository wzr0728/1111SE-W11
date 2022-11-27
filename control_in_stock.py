#!C:\Python39\python.exe
from dbConfig import conn, cur
def delStock(id):
    sql = "DELETE FROM `SaleCase` WHERE `SaleCase`.`id` = %s"
    cur.execute(sql,(id,))
    conn.commit()
def addProduct(name, first_price, deadline):
    if(name == None or first_price == None or deadline == None):
        return False
    sql = "insert into salecase (name, first_price, deadline) values (%s,%s,%s);"
    cur.execute(sql,(name, first_price, deadline))
    conn.commit()
    return True
def changeName(name, id):
    if(name == None):
        return
    else:
        sql = "update SaleCase set name=%s where id=%s;"
        cur.execute(sql,(name, id))
        conn.commit()
def changePrice(price, id):
    if(price == None):
        return
    else:
        sql = "update SaleCase set first_price=%s where id=%s;"
        cur.execute(sql,(price, id))
        conn.commit()
def changeStock(deadline, id):
    if(deadline == None):
        return
    elif(len(deadline)==19):
        sql = "update SaleCase set deadline=%s where id=%s;"
        cur.execute(sql,(deadline, id))
        conn.commit()
    return True
def decrease(id, amount):
    sql = "update product set Stock=Stock-%s where id=%s;"
    cur.execute(sql,(amount, id))
    conn.commit()
def getList():
    #查詢
    sql="select id,name,deadline,first_price from salecase ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
def searchProduct(id):
    sql = "select id, Name, Stock, Price from product where id = %s;"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    return records[0][1], records[0][3], records[0][2]

