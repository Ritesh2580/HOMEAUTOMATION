import sys
import ast
import mysql.connector as msc

data=sys.argv[1]
print(data);
tt=ast.literal_eval(data)

def add(data):
 code=0
 name="";
 for element in tt:
  if element=="code":
   code=tt[element]
  if element=="name":
   name=tt[element]
 
 if code==0 or len(name)==0:
  print("one of the field is empty cannot process request")
  return;
 try:
  connection=msc.connect(host="localhost",user="Ritesh",password="$$Ritesh$$",database="HOMEAUTOMATION");
  print(connection)
  cursor=connection.cursor();
  query="insert into section(code,name)values(%s,%s)";
  records=(code,name)
  cursor.execute(query,records)
  connection.commit()
  print("Record inserted successfully")
 except msc.Error as e:
  print(e)


add(tt);
   