var myPath;
console.log("HI")
var playerPosition;

var court_img_position = document.getElementById('court_img').getBoundingClientRect();
var img_left = court_img.left;

function recordPosition(event) {
	var x = event.point.x;
	var y = event.point.y;
	console.log("x: " + event.point.x);
	console.log("y: " + event.point.y);
	console.log("Position of img: ");
	convertPositionToLoc(x, y);
	court_img;
}

function convertPositionToLoc(x, y) {
	var width = document.getElementById('court_img').clientWidth;
	var height = document.getElementById('court_img').clientHeight;
	console.log(x/width * 250 - 250);
	console.log(y/width * 250 - 250);
}

function onMouseDown(event) {
	recordPosition(event)
	playerPosition = new Path.Circle({
		center: event.point,
		radius: 20
	});
	playerPosition.strokeColor = 'blue';
	playerPosition.fillColor = 'red';
}

function onMouseDrag(event) {
	console.log(event.point);
	playerPosition.translate(event.position)
}

function onMouseUp(event) {

}
