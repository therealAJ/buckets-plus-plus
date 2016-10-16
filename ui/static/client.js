var myPath;

var playerPosition;

var court_img_position = document.getElementById('court_img').getBoundingClientRect();
var img_left = court_img.left;

function recordPosition(event) {
	console.log("x: " + event.point.x);
	console.log("y: " + event.point.y);
	//console.log("Position of img: ");
	court_img;
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
