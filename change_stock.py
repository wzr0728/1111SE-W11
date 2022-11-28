#!C:\Users\何晏禎\AppData\Local\Programs\Python\Python310\python.exe
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
goodsList = controller_seller.getList()
form = cgi.FieldStorage()

for i in range(goodsList[len(goodsList)-1][0]):
    i += 1
    id_deadline = form.getvalue(f'deadline_{i}')
    id_price = form.getvalue(f'first_price_{i}')
    id_name = form.getvalue(f'name_{i}')
    a=controller_seller.changeDeadline(id_deadline, i)
    b=controller_seller.changePrice(id_price, i)
    c=controller_seller.changeName(id_name, i)
#name,deadline,first_price
    

if(a==False):    
    print("修改失敗")
else:
    print("修改完成")
print("<br><a href='root.py'>查看管理頁面</a>")
print("<br><a href='orderList.py'>查看訂單</a>")
print("</body></html>")
