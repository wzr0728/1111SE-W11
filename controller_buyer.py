#!/usr/bin/python3

from dbConfig import conn, cur
def getActiveList():
    sql = "select id, UiD,name, deadline from SaleCase where deadline >= NOW() ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records