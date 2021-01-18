import sys
import ast
import mysql.connector as msc

data=sys.argv[1]

print(data);
tt=ast.literal_eval(data)

def add(data):
 code=0
 name="";
 is_admin=False;
 mobile_number="";
 pass_key="";
 pass_key_key="";

 for element in tt:
  if element=="code":
   code=tt[element]
  if element=="is_admin":
   is_admin=tt[element]
  if element=="mobile_number":
   mobile_number=tt[element]
  if element=="name":
   name=tt[element]
  if element=="pass_key":
   pass_key=tt[element]
  if element=="pass_key_key":
   pass_key_key=tt[element]

 if code==0 or len(name)==0 or len(pass_key)==0 or len(pass_key_key)==0 or len(mobile_number)==0:
  print("one of the field is empty cannot process request")
  return;
 
 try:
  connection=msc.connect(host="localhost",user="Ritesh",password="$$Ritesh$$",database="HOMEAUTOMATION");
  print(connection)
  cursor=connection.cursor();
  query="insert into operator(code,name,pass_key,pass_key_key,is_admin,mobile_number)values(%s,%s,%s,%s,%s,%s)";
  records=(code,name,pass_key,pass_key_key,is_admin,mobile_number)
  cursor.execute(query,records)
  connection.commit()
  print("Record inserted successfully")
 except msc.Error as e:
  print(e)


add(tt);
   