var getPhotos = require('./getPhotos');
let result
inClient_id = 'EECH5IF2TSK01WV2DQUKIRNT5CUVRTH0AVVDFM521E32ZVPH';
inClient_secret  = '1LL20JSTUVM1BM4G30E0KMN1QBKU3ZDVLMO1OP5QIPWCQEOK';
inll = '48.858,2.294';
inQuery = 'Aqua'
inV = '20170801';
inLimit = 1;
radius =  100000;
category = '4fceea171983d5d06c3e9823'
venue_Id  = '4b767f0df964a520074f2ee3'
picSize = '100x100'
getPhotos( inClient_id, inClient_secret, inV, inLimit, venue_Id, picSize, function(error,response) {
  if (error) {
    console.log(error)
  } else {
    result= (response)
  }
})

console.log(result)