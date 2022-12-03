#!/usr/bin/python3
#2022-11-21 07:40:08
from dbConfig import conn, cur
def add(UiD, name, deadline, first_price):
    if(name == None):
        return False
    sql = "insert into SaleCase (UiD, name, deadline, first_price) values (%s,%s,%s,%s);"
    cur.execute(sql,(UiD, name, deadline, first_price))
    conn.commit()
    return True

def getList():
    sql="select id, name,deadline,first_price from SaleCase ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def delete(id):
    sql = "DELETE FROM `SaleCase` WHERE `SaleCase`.`id` = %s"
    cur.execute(sql,(id,))
    conn.commit()

def changeName(name, id):
    if(name == None):
        return 2
    else:
        sql = "update SaleCase set name=%s where id=%s;"
        cur.execute(sql,(name, id))
        conn.commit()

def changePrice(price, id):
    if(price == None):
        return 2
    else:
        sql = "update SaleCase set first_price=%s where id=%s;"
        cur.execute(sql,(price, id))
        conn.commit()

def changeDeadline(deadline, id):
    if(deadline == None):
        return 2
    elif(len(deadline)==19):
        sql = "update SaleCase set deadline=%s where id=%s;"
        cur.execute(sql,(deadline, id))
        conn.commit()
        return True
    else:
        return False