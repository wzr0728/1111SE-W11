#!/usr/bin/python3

from dbConfig import conn, cur
def getActiveList():
    sql = "select id, UiD,name, deadline from SaleCase where deadline >= NOW() ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
def getDetail(id):
    sql = "select id, UiD,name, deadline from SaleCase where id = %s;"
    sql2 = "select OiD, UiD, price from OrderCase where OiD = %s;"
    cur.execute(sql)
    SalesRecords = cur.fetchall()
    cur.execute(sql2)
    OrderRecords = cur.fetchall()
    return SalesRecords, OrderRecords # 標案資訊, 標案下標價格
def bid(id, price, UiD):
    if(id == None or price == None):
        return False
    sql = "insert into OrderCase (OiD, UiD, price) values (%s,%s,%s);"
    cur.execute(sql,(OiD, UiD, price))
    conn.commit()
    return True
