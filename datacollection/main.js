var getlandmarks = require('./landmarksSearch');

inClient_id = 'EECH5IF2TSK01WV2DQUKIRNT5CUVRTH0AVVDFM521E32ZVPH';
inClient_secret  = '1LL20JSTUVM1BM4G30E0KMN1QBKU3ZDVLMO1OP5QIPWCQEOK';
inll = '48.858,2.294';
inQuery = 'Aqua'
inV = '20170801';
inLimit = 3;
radius =  1000;
category = '4fceea171983d5d06c3e9823'

getlandmarks( inClient_id, inClient_secret, inll, inQuery, inV, inLimit, radius, category, function(error,response) {
  if (error) {
    console.log(error)
  } else {
    console.log(response)
  }
});