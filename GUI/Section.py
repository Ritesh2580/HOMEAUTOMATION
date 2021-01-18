class Section:
 def __init__(self):
  self.code=0
  self.name=""
  self.boards=[]
  self.appliances=[]

 def getCode(self):
  return self.code

 def setCode(self,code):
  self.code=code

 def getName(self):
  return self.name

 def setName(self,name):
  self.name=name

 def setBoards(self,boards):
  self.boards=boards

 def getBoards(self):
  return self.boards

 def getAppliances(self,appliances):
  self.appliances=appliances
