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
<title>add_cart</title>
</head>
<body>
""")
form = cgi.FieldStorage()
id = form.getvalue("searchId")

SalesRecords, OrderRecords = controller_buyer.getDetail(id)

msg = ""
msg = msg + f"編號 : {id} 標案名稱：{SalesRecords[0][2]} 標案期限：{SalesRecords[0][3]} 立標人：{SalesRecords[0][1]}</p>"
for (OiD, UiD, price) in OrderRecords:
    msg = msg + f"下標人：{UiD} 下標價格：{price}</p>" 
    

print(msg)
sys.stdout.flush()

    
