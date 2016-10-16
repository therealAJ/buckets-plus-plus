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
	for(var key in playerPosition) {
		console.log("== KEYYY");
		console.log(key);
		console.log("=== POSITION");
   	console.log(playerPosition[key].position);
		playerPosition[key];
	}
	playerPosition.position = new Point(event.point.x, event.point.y );
	updatePercentOutput(event);
}

function onMouseUp(event) {

}
