//Jackie Lin and Yifan Wang (Team Ketchup Packets)
//SoftDev1 pd1
//K#12 -- Connect the Dots
//2020-03-30

var pic = document.getElementById("vimage");
var prevX = -1;
var prevY = -1;

var clear = function(){
  while (pic.firstChild){
    pic.removeChild(pic.firstChild);
  }
  prevX = -1;
  prevY = -1;
}

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);


pic.addEventListener('mousedown', e => {
  var x = e.offsetX; //returns the x-coordinate of the click relative to the canvas
  var y = e.offsetY; //returns the y-coordinate of the click relative to the canvas

  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", 5);
  c.setAttribute("fill", "black");
  c.setAttribute("stroke", "black");
  pic.appendChild(c);

  if (prevX != -1){
    var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", prevX);
    l.setAttribute("y1", prevY);
    l.setAttribute("x2", x);
    l.setAttribute("y2", y);
    l.setAttribute("stroke", "black");
    l.setAttribute("stroke-width", 1);
    pic.appendChild(l);
  }
  prevX = x;
  prevY = y;
});
