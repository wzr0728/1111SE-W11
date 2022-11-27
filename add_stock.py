#!C:\Python39\python.exe
import codecs,sys
import cgi
import control_in_stock

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = control_in_stock.getList()

msg = """<form name="表單" method="post" action="add_product.py">
請依序輸入標案名稱、起標價、deadline</p>"""
#請依序輸入商品名稱、價格、庫存

msg+=f"""<input placeholder="標案名稱" name="name">"""
msg+=f"""<input placeholder="起標價" name="first_price">"""
msg+=f"""<input placeholder="例:2022-11-21 07:40:08" name="deadline"></p>"""
#msg+=f"""<input placeholder="商品名稱" name="name">"""
#msg+=f"""<input placeholder="商品價格" name="price">"""
#msg+=f"""<input placeholder="商品數量" name="amount"></p>"""

msg += """ <input type="submit" value="新增標案"></form>"""

with open("add_stock.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()