#!C:\Python39\python.exe
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
id = form.getvalue('i')
goodsdetail1, goodsdetail2 = controller_buyer.getDetail(id)
msg = """<form name="表單" method="post">"""
for (id, UiD,name, deadline) in goodsdetail1:
    msg = msg + f"編號 : {id} 標案 : {name} deadline : {deadline} </p>" 
for (OiD, UiD, price) in goodsdetail2:
    msg += msg + f"編號 : {OiD} 標案 : {UiD} deadline : {price} </p>" 
#print(msg)
    
#print("刪除完成")
print("<br><a href='root.py'>查看管理頁面</a>")
print("</body></html>")
