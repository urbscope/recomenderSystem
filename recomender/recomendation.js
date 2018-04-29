var fs = require('fs');
var d3 = require('d3-request-master');

userfile = 'userIndex.json'
categoryfile = 'categoryIndex.json'
var userIndex = fs.readFileSync(userfile,'utf8');
var categoryIndex = fs.readFileSync(categoryfile,'utf8');
console.log(userIndex)

var recomendation = function (userId){

	userList = JSON.parse(userIndex)
	//console.log(userList)

	categoryList = JSON.parse(categoryIndex)
	//console.log(categoryList)

	userMatIndiex = userList[userId]

	

};

module.exports = recomendation;
