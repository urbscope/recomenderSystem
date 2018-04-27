const request = require('request');
var getPhotos = require('./getPhotos')
const fs = require('fs');

var getLandmarks = function ( inClient_id, inClient_secret, inll, inQuery, inV, inLimit, inRadius,inCat, callback){

	var  searchResults = {
		landmarks: []
	};
	
	request({
	    url: 'https://api.foursquare.com/v2/venues/search',
	    method: 'GET',
	    qs: {
	        client_id: inClient_id,
	        client_secret: inClient_secret,
	        ll: inll,
	        //query: inQuery,
	        v: inV,
	        limit: inLimit,
			radius: inRadius,
			categoryId: inCat 
	    }

	}, function (err, res, body) {
		if (err) {
	        console.error(err);
	        callback(new Error('err'))
	    } 
	    else {
	    	
	    	jsonBody = JSON.parse(body)
	    	
	    	for (var i = 0; i < jsonBody.response.venues.length; i++){
	    		console.log('Item Found')

	    		/*
	    		var destData = {};
	    		destData['destinationID'] = jsonBody.response.venues[i].id;
	    		photo = getPhotos(inClient_id, inClient_secret,inV, 1, jsonBody.response.venues[i].id )
	    		destData['name'] = jsonBody.response.venues[i].name;
	    		destData['latitude'] = jsonBody.response.venues[i].location.lat;
	    		destData['longitude'] = jsonBody.response.venues[i].location.lng;
	    		destData['address'] = jsonBody.response.venues[i].location.formattedAddress;
	    		destData['categoryID'] = jsonBody.response.venues[i].categories[0].id;
	    		destData['category'] = jsonBody.response.venues[i].categories[0].name;*/
	    		searchResults.landmarks.push(jsonBody.response.venues[i].id);
	    	}

	    	/**
	    	for (var i = 0; i < jsonBody.response.groups[0].items.length; i++){

	    		var destData = {};

	    		destData['destinationID'] = jsonBody.response.groups[0].items[i].venue.id;
		    	destData['name'] = jsonBody.response.groups[0].items[i].venue.name;
		    	destData['latitude'] = jsonBody.response.groups[0].items[i].venue.location.lat;
		    	destData['longitude'] = jsonBody.response.groups[0].items[i].venue.location.lng;
		    	destData['address'] = jsonBody.response.groups[0].items[i].venue.location.formattedAddress;
		    	destData['categoryID'] = jsonBody.response.groups[0].items[i].venue.categories[0].id;
		    	destData['category'] = jsonBody.response.groups[0].items[i].venue.categories[0].name;
		    	searchResults.landmarks.push(destData);
	    	}
			**/
	    	
	    	//var data = JSON.stringify(jsonBody, null, 4);
	    	//fs.appendFileSync('file.json', data);
	    	//data = JSON.stringify(searchResults, null, 4);	
	    	//fs.writeFileSync('results.json', data);
	    	callback(null, searchResults);
	    	
	    }
	});
};

module.exports = getLandmarks;
