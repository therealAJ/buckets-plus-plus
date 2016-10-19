var myPath;

// As new points are being made, playerCcount increaments
// and becomes the id of the dot.
var playerCount = 0;
var playerPosition = {};
var playerExist = {};

// To calculate the canvas size ... but I hard coded it
// so its not responsive as of now. Only for ipad.
var court_img_position = document.getElementById('court_img').getBoundingClientRect();
var img_left = court_img.left;

var percent_output = document.getElementById('percent_output');

var total_remaining_time = document.getElementById('total_remaining_time')

document.getElementById('total_remaining_time')

function calcTotalTime() {
	console.log("CALCULATING TIME YO");
	var times = document.getElementsByClassName('value');
	total_remaining_time.innerHTML = times[0].innerHTML + ' : ' + times[1].innerHTML;
}

// Reposition the percentage
// oh shit this should be fixed with the relative point
function updatePercentOutput(event) {
	percent_output.style.left = (event.point.x + 35).toString() + "px";
	percent_output.style.top = (event.point.y - 40).toString() + "px";
	percent_output.innerHTML = Math.round(event.point.x).toString() + "%";
}

function recordPosition(event) {
	console.log("x: " + event.point.x);
}

function onMouseDown(event) {
	// Only 5 players can be in the court
	console.log("y: " + event.point.y);
	if (playerCount < 1) {
		recordPosition(event)
		playerCount++;
		playerPosition[playerCount] = new Path.Circle({
			id: playerCount,
			center: event.point,
			radius: 20
		});
		playerPosition[playerCount].strokeColor = 'blue';
		playerPosition[playerCount].fillColor = '#e09cb8';
		playerExist[playerCount] = true;
		updatePercentOutput(event);
	}
}

function onMouseDrag(event) {
	var closestCenter;
	var closestPath;
	console.log(event.point);
	// Find the closest point
	// for(var key in playerPosition) {
	// 	console.log("== KEYYY");
	// 	console.log(key);
	// 	console.log("=== POSITION");
  //  	console.log(playerPosition[key].position);
	// 	playerPosition[key];
	// }
	playerPosition[playerCount].position = new Point(event.point.x, event.point.y );
	updatePercentOutput(event);
}

function onMouseUp(event) {

}

var rec_map = [];

var drawGridRects = function(num_rectangles_wide, num_rectangles_tall, boundingRect) {
  var width_per_rectangle = boundingRect.width / num_rectangles_wide;
  var height_per_rectangle = boundingRect.height / num_rectangles_tall;
  for (var i = 0; i < num_rectangles_wide; i++) {
    for (var j = 0; j < num_rectangles_tall; j++) {
      var aRect = new paper.Path.Rectangle(boundingRect.left + i * width_per_rectangle, boundingRect.top + j * height_per_rectangle, width_per_rectangle, height_per_rectangle);
      aRect.strokeColor = 'white';
			rec_map.push(aRect);
    }
  }
}

function createHeatString(rec_map) {
	var output = {};

	// Put Time in seconds
	output['time'] = "111" // FIX THIS

	// x string
	var output_x = "";
	for (var k = 0; k < rec_map.length; k++) {
		output_x += rec_map[k].position._x.toFixed(3).toString() + ","
	}
	output_x.substring(0, output_x.length - 1);
	output['output_x'] = output_x;

	var output_y = "";
	for (var r = 0; r < rec_map.length; r++) {
		output_y += rec_map[r].position._y.toFixed(3).toString() + ","
	}
	output_y.substring(0, output_y.length - 1);
	output['output_y'] = output_y;

	return output;
}

drawGridRects(30, 30, paper.view.bounds);

function percetageToGradient(num) {
	return [255, 1-num * 255, 1-num * 255];
}

function mapPredictionAsHeat(predictions) {
	predictions = predictions.split(',');
	for (var t = 0; t < predictions.length; t++) {
		if (rec_map[t]) {
			rec_map[t].fillColor = percetageToGradient(predictions[t])
		}
	}
}
