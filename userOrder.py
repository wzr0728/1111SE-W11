#!/usr/bin/python3
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import controller_buyer

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>del</title>
</head>
<body>
""")

form = cgi.FieldStorage()
id = form.getvalue("searchId")
price = form.getvalue("price")
money = controller_buyer.bid(id, price, 'user2')

print("下標完成!")


print("<br><a href='user.py'>查看首頁</a>")
print("</body></html>")

