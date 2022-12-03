#!/usr/bin/python3
import codecs,sys
import cgi
import controller_seller

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = controller_seller.getList()

msg = """<form name="表單" method="post" action="change_stock.py">
不輸入即為不更改</p>"""
for (id,name,deadline,first_price) in goodsList:
    msg = msg + f"編號 : {id} 標案 : {name} 起標價 : {first_price} deadline : {deadline}" 
    msg+=f"""<input placeholder="更改名稱" name="name_{id}">"""
    msg+=f"""<input placeholder="更改起標價" name="first_price_{id}">"""
    msg+=f"""<input placeholder="更改deadline" name="deadline_{id}">"""
    msg+=f"""</p>"""

msg += """ <input type="submit" value="修改標案"></form></p>"""

msg += """<form method="post" action="del_stock.py">
輸入要刪除的標案編號: <input type='text' name='i'><input type='submit'>
</form> <br>"""
with open("root.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()