var pyShell = require('python-shell');

var shell = new pyShell('predictor.py');

shell.send('196,302');

shell.on('message', function(message){
	console.log(message);
});

shell.end(function (err) {
    if (err){
        throw err;
    };
});