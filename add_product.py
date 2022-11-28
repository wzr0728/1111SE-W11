#!C:\Python39\python.exe
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import controller_seller

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


id_uid = "user1"
id_price = form.getvalue(f'first_price')
id_name = form.getvalue(f'name')
id_deadline = form.getvalue(f'deadline')
status = controller_seller.add(id_uid, id_name, id_deadline, id_price)
if(status == False):
    print("資料不齊全，未成功新增")

    
    
print("新增完成")
print("<br><a href='root.py'>查看管理頁面</a>")
print("<br><a href='orderList.py'>查看訂單</a>")
print("</body></html>")
