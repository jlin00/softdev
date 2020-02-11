//Jackie Lin and Devin Lin (Team Rocchio)
//SoftDev1 pd1
//K#05 -- Canvas
//2020-02-11

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
ctx.fillStyle = "black";
ctx.strokeStyle = "black";
var prevX = -1;
var prevY = -1;

var clear = function(){
  ctx.clearRect(0, 0, c.width, c.height);
  prevX = -1;
  prevY = -1;
}

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);

c.addEventListener('mousedown', e => {
  var x = e.offsetX; //returns the x-coordinate of the click relative to the canvas
  var y = e.offsetY; //returns the y-coordinate of the click relative to the canvas

  ctx.beginPath();
  ctx.arc(x, y, 5, 0, 2 * Math.PI);

  if (prevX != -1){ //if not first dot, draw line to previous dot
    ctx.moveTo(x, y);
    ctx.lineTo(prevX, prevY);
  }
  ctx.stroke();
  ctx.fill();
  ctx.closePath();
  prevX = x; //update x, y values
  prevY = y;
});
