const request = require('request');
const fs = require('fs');

var getLandmarks = function ( inClient_id, inClient_secret, inll, inQuery, inV, inLimit, inOpenNow, lund){

	var  searchResults = {
		landmarks: []
	};
	
	request({
	    url: 'https://api.foursquare.com/v2/venues/explore',
	    method: 'GET',
	    qs: {
	        client_id: inClient_id,
	        client_secret: inClient_secret,
	        ll: inll,
	        query: inQuery,
	        v: inV,
	        limit: inLimit,
	        openNow: inOpenNow,
	        sortByDistance: 1
	    }

	}, function (err, res, body) {
		if (err) {
	        console.error(err);
	        lund(new Error('err'))
	    } 
	    else {
	    	jsonBody = JSON.parse(body)
	    

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

	    	
	    	var data = JSON.stringify(jsonBody, null, 4);
	    	fs.writeFileSync('file.json', data);
	    	data = JSON.stringify(searchResults, null, 4);	
	    	fs.writeFileSync('results.json', data);
	    	lund(null, searchResults);
	    }
	});
};

module.exports = getLandmarks;
