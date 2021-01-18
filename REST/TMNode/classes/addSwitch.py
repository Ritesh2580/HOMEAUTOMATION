import sys
import ast
import mysql.connector as msc

data=sys.argv[1]
print(data);
tt=ast.literal_eval(data)

def add(data):
 code=0
 board_code=0;
 appliance_code=0;
 for element in tt:
   if element=="code":
    code=tt[element]
   if element=="board_code":
    board_code=tt[element]
   if element=="appliance_code":
    appliance_code=tt[element]

 
 if code==0 or board_code==0 or appliance_code==0:
  print("one of the field is empty cannot process request")
  return;
 try:
  connection=msc.connect(host="localhost",user="Ritesh",password="$$Ritesh$$",database="HOMEAUTOMATION");
  print(connection)
  cursor=connection.cursor();
  query="insert into switch(code,board_code,appliance_code)values(%s,%s,%s)";
  records=(code,board_code,appliance_code)
  cursor.execute(query,records)
  connection.commit()
  print("Record inserted successfully")
 except msc.Error as e:
  print(e)


add(tt);
   