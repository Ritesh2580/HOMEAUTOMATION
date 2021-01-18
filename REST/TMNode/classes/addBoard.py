import sys
import ast
import mysql.connector as msc

data=sys.argv[1]
print(data);
tt=ast.literal_eval(data)

def add(data):
 code=0
 section_code=0;
 location="";
 number_of_appliances=0;
 pass_key="";
 pass_key_key="";
 for element in tt:
  if element=="code":
   code=tt[element]
  if element=="location":
   location=tt[element]
  if element=="section_code":
   section_code=tt[element]
  if element=="number_of_appliances":
   number_of_appliances=tt[element]
  if element=="pass_key":
   pass_key=tt[element]
  if element=="pass_key_key":
   pass_key_key=tt[element]

 if code==0 or section_code==0 or len(pass_key)==0 or len(pass_key_key)==0 or len(location)==0 or number_of_appliances==0:
  print("one of the field is empty cannot process request")
  return;
 
 try:
  connection=msc.connect(host="localhost",user="Ritesh",password="$$Ritesh$$",database="HOMEAUTOMATION");
  print(connection)
  cursor=connection.cursor();
  query="insert into board(code,section_code,location,number_of_appliances,pass_key,pass_key_key)values(%s,%s,%s,%s,%s,%s)";
  records=(code,section_code,location,number_of_appliances,pass_key,pass_key_key)
  cursor.execute(query,records)
  connection.commit()
  print("Record inserted successfully")
 except msc.Error as e:
  print(e)


add(tt);
   