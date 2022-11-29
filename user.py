#!C:\Python39\python.exe
import codecs,sys
import cgi
import controller_buyer

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = controller_buyer.getActiveList()

msg = """<form name="表單" method="post">"""
for (id, UiD,name, deadline) in goodsList:
    msg = msg + f"編號 : {id} 標案 : {name} deadline : {deadline} </p>" 

msg += """<form method="post" action="detail.py">
輸入想了解的標案編號: <input type='text' name='i'><input type='submit'>
</form> <br>"""

msg+= """<form name="表單" method="post" action="bid.py"></p>"""
msg+=f"""<input placeholder="標案編號" name="i">"""
msg+=f"""<input placeholder="金額" name="k">"""
msg += """ <input type="submit" value="下標"></p></form>"""

#id, OiD, UiD, price競標紀錄
myactive = controller_buyer.getMyActive("user2")
msg+= """<form name="表單" method="post">"""
for (id, OiD, UiD, price) in myactive:
    msg = msg + f"編號 : {id} 標案 : {OiD} 下標者 : {UiD} 金額 : {price}</p>"

with open("user.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()