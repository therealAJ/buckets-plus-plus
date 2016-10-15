var express = require('express');
var app = express();

app.use( express.static( __dirname + '/static' ));

app.get( '/', function( req, res ) {
  res.sendFile( path.join( __dirname, 'static' ));
});

app.listen(3000, function () {
  console.log('This shit is running m8');
});
