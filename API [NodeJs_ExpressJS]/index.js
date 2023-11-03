const express = require("express");
const app = express();

app.get('/',(req, res) => {
    res.send("Welcome to 9ino6ano")
})

app.listen(3000,() => {
    console.log("Listening to port 4000")
})