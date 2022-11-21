#!/usr/bin/python3
from dbConfig import conn, cur
def add(Uid, name, deadline, first_price):
    if(name == None):
        return False
    sql = "insert into SaleCase (UiD, name, deadline, first_price) values (%s,%s,%s);"
    cur.execute(sql,(UiD, name, deadline, first_price))
    conn.commit()
    return True

def getList():
    sql="select id,UiD, Name,deadline from SaleCase ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
