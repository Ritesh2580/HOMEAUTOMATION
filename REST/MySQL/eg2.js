var connection=require("mysql").createConnection(
{
host:'localhost',
user:"root",
password:"password",
});

connection.connect((error)=>{
if(error)
{
console.log(error);
console.log("Unable to connect with database");
return;
}
console.log('connection established');
});
connection.query("use tmdb");
console.log(connection.query("show tables"));
