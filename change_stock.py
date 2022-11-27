#!C:\Python39\python.exe
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control_in_stock

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
goodsList = control_in_stock.getList()
form = cgi.FieldStorage()

for i in range(goodsList[len(goodsList)-1][0]):
    i += 1
    id_deadline = form.getvalue(f'deadline_{i}')
    id_price = form.getvalue(f'first_price_{i}')
    id_name = form.getvalue(f'name_{i}')
    control_in_stock.changeStock(id_deadline, i)
    control_in_stock.changePrice(id_price, i)
    control_in_stock.changeName(id_name, i)
#name,deadline,first_price
    
    
print("修改完成")
print("<br><a href='root.py'>查看管理頁面</a>")
print("<br><a href='orderList.py'>查看訂單</a>")
print("</body></html>")
