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

// Reposition the percentage
// oh shit this should be fixed with the relative point
function updatePercentOutput(event, percentage) {
	percent_output.style.left = (event.point.x + 35).toString() + "px";
	percent_output.style.top = (event.point.y - 40).toString() + "px";
	//percent_output.innerHTML = Math.round(event.point.x).toString() + "%";
	console.log(Math.round(percentage * 100));
	percentage = Math.round(percentage * 1000) /10;
	percent_output.innerHTML = percentage.toString() + "%";
}

function recordPosition(event) {
	sendHttp(event)
}

function sendHttp(event) {
	var http = new XMLHttpRequest();
	var url = "prediction";
	var data = new FormData();
	var location = convertPositionToLoc(event);
	var minutes = document.getElementById('minuteInput').value;
	var seconds = document.getElementById('secondInput').value;
	var totalSeconds = timeToSeconds(minutes, seconds);
	console.log(totalSeconds);
	console.log("x: " + Math.round(location[0]));
	console.log("y: " + Math.round(location[1]));
	data.append('loc_x', Math.round(location[0]));
	data.append('loc_y', Math.round(location[1]));
	data.append('time_remaining', totalSeconds);
	
	http.open("POST", url, true);

	http.onload = function() {
		console.log(this.responseText);
		updatePercentOutput(event, this.responseText)
	}
	http.send(data);
}

function convertPositionToLoc(event) {
	var width = document.getElementById('paper_stage').clientWidth;
	var height = document.getElementById('paper_stage').clientHeight;
	console.log("width: " + width);
	console.log("height: " + height);
	var x = event.point.x;
	var y = event.point.y;
	// console.log(x/width * 200)
	// console.log(y/width * 200)
	return [x/width * 500 - 250, -y/width * 500 + 422.5];
}

function timeToSeconds(minutes, seconds) {
	return minutes * 60 + seconds;
}

function onMouseDown(event) {
	// Only 5 players can be in the court
	//console.log("y: " + event.point.y);
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
		//updatePercentOutput(event);
	}
}

function onMouseDrag(event) {
	
}

function onMouseUp(event) {
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
	//updatePercentOutput(event);
	recordPosition(event);
}


