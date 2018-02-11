const request = require('request');
const fs = require('fs');

var getCordinates = function ( id, code, place, callback){

	var  searchResults = {
		cordinates: ''
	};
	request({
	    url: 'https://geocoder.cit.api.here.com/6.2/geocode.json',
	    method: 'GET',
	    qs: {
	        app_id:id,
	        app_code:code,
	        searchtext:place,
	    }

	}, function (err, res, body) {
		if (err) {
	        console.error(err);
          console.log(place);
	        callback(new Error('err'))
	    }
	    else {
	    	jsonBody = JSON.parse(body)
        //console.log(place + " \t" +JSON.stringify(jsonBody,null,4))
        if(jsonBody.Response.View[0]){
        //console.log(JSON.stringify(jsonBody.Response.View[0].Result[0].Location.DisplayPosition,null,4))
          longitude = jsonBody.Response.View[0].Result[0].Location.DisplayPosition.Longitude;
          latitude = jsonBody.Response.View[0].Result[0].Location.DisplayPosition.Latitude;
          searchResults.cordinates = latitude + " " + longitude + "\n"
          fs.appendFile('cordinates.txt', searchResults.cordinates, function (err) {
            if (err) {
              console.log(err)
            } else {
              // done
            }
          })
  	    	callback(null, searchResults);
          return 0;
        //console.log(searchResults.cordinates)
        }
        else{
          fs.appendFile('cordinates.txt', "\n", function (err) {
            if (err) {
              console.log(err)
            } else {
              // done
            }
          })
  	    	callback(null, searchResults);
          return 1;
        }
        /*
	    	var data = JSON.stringify(jsonBody, null, 4);
	    	fs.writeFileSync('file.json', data);
	    	data = JSON.stringify(searchResults, null, 4);
	    	fs.writeFileSync('results.json', data);*/
	    }
	});
};

module.exports = getCordinates;
