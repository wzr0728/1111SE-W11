#!/usr/bin/python3
import codecs,sys
import cgi
import controller_buyer

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = controller_buyer.getActiveList()
msg = """<form name="表單" method="post" action="userDetail.py">"""
for (id, UiD, name,deadline) in goodsList:
    msg = msg + f"編號 : {id} 標案名稱：{name} 標案期限：{deadline}</p>" 
    
msg+="""</p><input placeholder="輸入編號" name="searchId">"""

msg += """ <input type="submit" value="查看標案詳情"></form></p>"""
msg += """<form name="表單" method="post" action="userOrder.py">"""
msg+=""" <input placeholder="輸入編號" name="searchId">"""
msg+="""<input placeholder="輸入價格" name="price">"""
msg += """ <input type="submit" value="下標"></form>"""

with open("user.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()