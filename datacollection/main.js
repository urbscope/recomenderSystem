var getlandmarks = require('./landmarksSearch');
var getPhotos = require('./getPhotos')

inClient_id = '';
inClient_secret  = '';
inll = '48.858,2.294';
inQuery = 'Aqua'
inV = '20170801';
inLimit = 10;
picLimit = 1
radius =  10000;
category = '4d4b7104d754a06370d81259'
picSize = '100x100'

getlandmarks( inClient_id, inClient_secret, inll, inQuery, inV, inLimit, radius, category, function(error,response) {
  if (error) {
    console.log(error)
  } else {
    //console.log(response)
    getPhotos(response, function(error,response) {
	  if (error) {
	    console.log(error)
	  } else {
	    result= (response)
	    console.log(response)
	  }
	})

  }
});
