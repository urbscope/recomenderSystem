var getlandmarks = require('./landmarksSearch');
var fs = require('fs');
var fs2 = require('fs');
var text = "as";

inClient_id = '';
inClient_secret  = '';
inll = '48.858,2.294';
inQuery = 'Aqua'
inV = '20170801';
inLimit = 3;
radius =  1000;
category = '4fceea171983d5d06c3e9823';
file = './CityList.txt';
file2 = './categories.txt';

//fs.readFile(file, 'utf8');
var cities = fs.readFileSync(file,'utf8');
var categories = fs2.readFileSync(file2, 'utf8');

// Make cordinates array
temp = cities.split("\n");
cordinates = [];
for(let i = 0; i < temp.length-1; i++){
	var cords = temp[i].split(":")[1];
	//lat = cords.split(",")[0];
	//lng = cords.split(",")[1];
	cordinates.push(cords)
}
//console.log(cordinates);

temp = categories.split("\n");
categoryIDs = [];
for(let i = 0; i < temp.length-1; i++){
	categoryIDs.push(temp[i].split(":")[0]);
}

//onsole.log(categoryIDs);


for(let i = 0; i < cordinates.length; i++){
	for(let j = 0; j < categoryIDs.length; j++){
		getlandmarks( inClient_id, inClient_secret, cordinates[i], inQuery, inV, inLimit, radius, categoryIDs[j], function(error,response) {
		  if (error) {
		    console.log(error)
		  } else {
		    lmarks = response['landmarks'];
		    console.log(lmarks);
		  }
		}
		);
	}
}

//console.log(array)
/*
getlandmarks( inClient_id, inClient_secret, inll, inQuery, inV, inLimit, radius, category, function(error,response) {
  if (error) {
    console.log(error)
  } else {
    console.log(response)
  }
});
*/