var getCordinates = require('./cordinates');
const fs = require('fs');
const request = require('request');

app_id = "hlKdIBnwnwBhG8xTg1NN"
app_code = "lV2A2fIcO1sWLuIhn5smSA"

var badLocations = 0
var places = fs.readFileSync('user_data.txt').toString().split("\n");
var x = 0
for(let i = 0; i < places.length-1; i++){
  getCordinates( app_id, app_code, places[i].split("|")[1], function(error,response) {
    if (error) {
      console.log(error)
    } else {
      x = x + 1
    }
  });
}

console.log(x)
