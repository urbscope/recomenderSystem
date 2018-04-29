var pyShell = require('python-shell-master');

var shell = new pyShell('predictions.py');

shell.end(function (err){
	if (err){
	    throw err;
	};
});
