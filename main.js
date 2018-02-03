var getlandmarks = require('./landmarksSearch');

inClient_id = 'EECH5IF2TSK01WV2DQUKIRNT5CUVRTH0AVVDFM521E32ZVPH';
inClient_secret  = '1LL20JSTUVM1BM4G30E0KMN1QBKU3ZDVLMO1OP5QIPWCQEOK';
inll = '40.431875,116.570428';
inQuery = 'History'
inV = '20170801';
inLimit = 3;
inOpenNow = 0;
radius =  1000;

getlandmarks( inClient_id, inClient_secret, inll, inQuery, inV, inLimit, inOpenNow,  function(error,response) {
  if (error) {
    console.log(error)
  } else {
    console.log(response)
  }
});
