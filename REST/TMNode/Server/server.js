let httpServerFactory=require("http");
let fileSystemUtilites=require("fs");
let urlUtilites=require("url");
let pathUtilites=require("path");
let bodyParser=require("body-parser");
const connections=new Map();
const WebSocket=require("ws");


let processBuffer=require("child_process").spawn;
bodyParser.json(({ type: 'application/*+json',inflate: false}));



class TMNode
{
constructor()
{
this.httpServer=httpServerFactory.createServer();
this.configuration=this.configureServer();
this.portNumber=this.configuration.configuration.port;
this.urls=this.configuration.configuration.urlMapping;
}
configureServer()
{
this.currentWorkingDirectory=process.cwd();
let configurationFile=(this.currentWorkingDirectory.substring(0,this.currentWorkingDirectory.length-6))+"Configuration\\configuration.json";
let obj=null;
try
{
let jsonString=fileSystemUtilites.readFileSync(configurationFile,'utf-8');
obj=JSON.parse(jsonString);
}
catch(execp)
{
console.log(execp);
}

return obj;
}

invokeServlet(request,response)
{
try
{
let path_to_file=(this.currentWorkingDirectory.substring(0,this.currentWorkingDirectory.length-6))+"classes\\"+this.currentURL.value;
let process=processBuffer('python',[path_to_file,this.body]);
process.stdout.on("data", function (data) {
const {headers,method,url}=request;
let t=this.body;
response.statusCode = 200;
let v=data.toString();
v=v.replace(/'/g, '"');
response.write(v);
response.end();


console.log(data.toString());

});

}
catch(excep)
{
console.log(excep);
}
}

processRequest(requestURI)
{
let url;
this.urls.forEach(u=>{
if(u.key==requestURI)url=u;
});
return url;
}

start()
{
const THIS=this;
this.httpServer.on('request',function(request,response)
{
const {headers,method,url}=request;
let requestURI=urlUtilites.parse(request.url).pathname;
THIS.body=[];
 request.on('error',(err)=>{console.error(err);
}).on('data',(chunk)=>{ 
THIS.body.push(chunk);
}).on('end',() => {
THIS.body=Buffer.concat(THIS.body).toString();
console.log(THIS.body);
THIS.invokeServlet(request,response);
});
response.on('error', (err) => {
console.error(err);
});
response.statusCode = 200;
let t=THIS.body;
response.setHeader('Content-Type', 'application/json');
const responseBody = { headers, method, url,t};




if(request.method.toUpperCase()=="GET")
{
console.log("GET request arrives");
THIS.currentURL=THIS.processRequest(requestURI);
console.log("request come for "+THIS.currentURL.key+"  "+THIS.currentURL.value);
}
if(request.method.toUpperCase()=="POST")
{
console.log("POST request arrives");
THIS.currentURL=THIS.processRequest(requestURI);
console.log("request come for "+THIS.currentURL.key+"  "+THIS.currentURL.value);
}



}).listen(this.portNumber);
console.log("http server is listening in port no: 3000");
}




initWebSocket()
{

const wss=new WebSocket.Server({
server:this.httpServer
});

wss.on("connection",(ws,request)=>{
let securityKey=request.url.substring(2,request.url.length);
connections.set(securityKey,ws);

ws.on("message",(message)=>{
console.log(`Message received by client => ${message}`);

let t=request.url.substring(2,request.url.length);
connections.forEach((connection,key)=>{
if(!(key==t))connection.send(message);

});
});

ws.on("error",error=>{
console.log(`Error occoured => ${error}`);
});
});

console.log("Server is listening in port : 3000");


}

}

const server=new TMNode();
server.start()
server.initWebSocket()