#!C:\Python39\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import controller_buyer

#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>範例1</title>
</head>
<body>
""")

#查詢 OiD, UiD, price
form = cgi.FieldStorage()
id=form.getvalue(f'i')
UiD="user2"
price=form.getvalue(f'k')
status=controller_buyer.bid(id, price, UiD)
if(status == False):
    print("下標失敗")

print("下標成功")
print("<br><a href='user.py'>繼續下標</a>")
print("</body></html>")
