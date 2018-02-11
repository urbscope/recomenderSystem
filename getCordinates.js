var getCordinates = require('./cordinates');
const fs = require('fs');
const request = require('request');

app_id = "hlKdIBnwnwBhG8xTg1NN"
app_code = "lV2A2fIcO1sWLuIhn5smSA"

var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('test.txt')
});

var badLocations = 0
var places = fs.readFileSync('user_data.txt').toString().split("\n");
/*lineReader.on('line', function (line) {
  places.push(line.split("|")[1])
});*/
//console.log(places)
/*getCordinates( app_id, app_code, places[0].split("|")[1], function(error,response) {
  if (error) {
    console.log(error)
  } else {
    //console.log(response)
  }
});*/
for(let i = 0; i < places.length-1; i++){
  getCordinates( app_id, app_code, places[i].split("|")[1], function(error,response) {
    if (error) {
      console.log(error)
    } else {
      //console.log(response)
    }
  });
}
/*places.forEach(getCordinates( app_id, app_code, places[0].split("|")[1], function(error,response) {
  if (error) {
    console.log(error)
  } else {
    //console.log(response)
  }
}));*/
