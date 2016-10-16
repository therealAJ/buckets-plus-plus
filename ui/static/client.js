var myPath;

var playerCount = 0;
var playerPosition;
var playerExist = false;

var court_img_position = document.getElementById('court_img').getBoundingClientRect();
var img_left = court_img.left;

var percent_output = document.getElementById('percent_output');

function updatePercentOutput(event) {
	console.log("===== LEFT");
	console.log(percent_output.style);
	percent_output.style.left = (event.point.x + 35).toString() + "px";
	percent_output.style.top = (event.point.y - 40).toString() + "px";
	percent_output.innerHTML = Math.round(event.point.x).toString() + "%";
}

function recordPosition(event) {
	console.log("x: " + event.point.x);
	console.log("y: " + event.point.y);
	//console.log("Position of img: ");
	court_img;
}

function onMouseDown(event) {
	if (playerExist == false) {
		recordPosition(event)
		playerPosition = new Path.Circle({
			center: event.point,
			radius: 20
		});
		playerPosition.strokeColor = 'blue';
		playerPosition.fillColor = '#e09cb8';
		playerExist = true;
		updatePercentOutput(event);
	}
}

function onMouseDrag(event) {
	if (playerExist) {
		console.log(event.point);
		playerPosition.position = new Point(event.point.x, event.point.y );
		updatePercentOutput(event);
	}
}

function onMouseUp(event) {

}
