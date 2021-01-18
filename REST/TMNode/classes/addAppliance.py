import sys
import ast
import mysql.connector as msc

data=sys.argv[1]
print(data);
tt=ast.literal_eval(data)

def add(data):
 code=0
 name="";
 is_regulatable=0;
 min_value=0;
 max_value=0;
 for element in tt:
  if element=="code":
   code=tt[element]
  if element=="name":
   name=tt[element]
  if element=="is_regulatable":
   is_regulatable=tt[element]
  if element=="min_value":
   min_value=tt[element]
  if element=="max_value":
   max_value=tt[element]
 if code==0 or len(name)==0 or is_regulatable==0 or min_value==0 or max_value==0:
  print("one of the field is empty cannot process request")
  return;
 
 try:
  connection=msc.connect(host="localhost",user="Ritesh",password="$$Ritesh$$",database="HOMEAUTOMATION");
  print(connection)
  cursor=connection.cursor();
  query="insert into appliance(code,name,is_regulatable,min_value,max_value)values(%s,%s,%s,%s,%s)";
  records=(code,name,is_regulatable,min_value,max_value)
  cursor.execute(query,records)
  connection.commit()
  print("Record inserted successfully")
 except msc.Error as e:
  print(e)


add(tt);
   