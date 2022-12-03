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


records = controller_buyer.getMyActive('user2')
getRec = controller_buyer.getMyCase()

msg = "<h1>下標紀錄</h1>"
for (id, OiD, UiD, price) in records:
    msg = msg + f"下標編號 : {id} 標案編號：{OiD} 下標金額：{price}</p>" 

msg += "<h1>得標紀錄</h1>"
for (OiD, UiD, Price) in getRec:
    msg = msg + f" 標案編號：{OiD} 得標者 : {UiD} 得標金額：{Price}</p>" 

print(msg)
sys.stdout.flush()

    
