var myPath;

var court_img_position = document.getElementById('court_img').getBoundingClientRect();
var img_left = court_img.left;

function recordPosition(event) {
	console.log("x: " + event.point.x);
	console.log("y: " + event.point.y);
	console.log("Position of img: ");
	court_img;
}

function onMouseDown(event) {
	recordPosition(event)
	var myCircle = new Path.Circle({
		center: event.point,
		radius: 20
	});
	myCircle.strokeColor = 'blue';
	myCircle.fillColor = 'red';
}

function onMouseDrag(event) {
	myPath.add(event.point);
}

function onMouseUp(event) {

}
