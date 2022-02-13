const express=require('express'),
      app=express(),
      ejs=require('ejs'),
      PORT=8000,
      spawn = require('child_process').spawn,
      data="bloodshot"

//middleware
app.set('view engine',"ejs")
app.use(express.static("public"))

//routes
app.get("/home",async(req,res)=>{
    res.render("home")
})

app.get("/getMovie",(req,res)=>{
    py = spawn('py', ['review.py',req.query.m])
        py.stdout.on('data', function(data) { 
        res.send(JSON.parse(data.toString())) 
    })
})


app.listen(PORT,()=>{
    console.log("connected to server")
})