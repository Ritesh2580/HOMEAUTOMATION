import sys
import ast
import mysql.connector as msc
import json 
def getAll():
 
 try:
  connection=msc.connect(host="localhost",user="Ritesh",password="$$Ritesh$$",database="HOMEAUTOMATION");
  cursor=connection.cursor();

  query="select * from section";
  cursor.execute(query)
  sections=cursor.fetchall();  

  query="select * from board";
  cursor.execute(query)
  boards=cursor.fetchall();  

  query="select * from appliance";
  cursor.execute(query)
  appliances=cursor.fetchall();  

  query="select * from switch";
  cursor.execute(query)
  switches=cursor.fetchall();  

  Obj={"sections":[]}

  for sec in sections:
   oo = {"code": sec[0], "name": sec[1], "appliances": []}
   for a in appliances:
    for s in switches:
     if  a[0]==s[2]:
      for b in boards:
       if b[0]==s[1]:
        if(sec[0]==b[1]):
         section={"code":sec[0],"name":sec[1],"appliance":[]}
         b1={"code": b[0], "location": b[2], "number_of_appliances": b[3], "pass_key": b[4], "pass_key_key": b[5],"section":section}
         s1={"state": 0, "board":b1}
         appliance={"code":a[0],"name":a[1],"is_regulatable":a[2],"min_value":a[3],"max_value":a[4],"switch":s1,"speed":0}
         oo["appliances"].append(appliance)
   Obj["sections"].append(oo)





  return(str(Obj).replace("'",'"'))

 except msc.Error as e:
  print(e)


def createFile(data):
 f=open("HOMEAUTOMATION.data","w+")
 f.writelines(data)
 f.close()


createFile(getAll());