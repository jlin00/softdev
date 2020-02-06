//Jackie Lin and Devin Lin (Team Rocchio)
//SoftDev1 pd1
//K#05 -- Canvas
//2020-02-06

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var colors=["black","green","yellow","purple","red","blue","brown","orange","pink","grey"]
var colorIndex=0
ctx.fillStyle = colors[colorIndex]
ctx.strokeStyle = colors[colorIndex]
var mode = 0; //0 for dot, 1 for box

var clear = function(){
  ctx.clearRect(0, 0, c.width, c.height);
  //console.log("clear");
}

var toggle = function(){
  if (mode == 0){
    mode = 1;
    document.getElementById("mode").innerHTML = "box";
  }
  else {
    mode = 0;
    document.getElementById("mode").innerHTML = "dot";
  }
  //console.log(mode);
}

var colorize = function(){
  //console.log("hi")
  colorIndex=(colorIndex+1)%10;
  ctx.fillStyle=colors[colorIndex];
  ctx.strokeStyle = colors[colorIndex];
  document.getElementById("CurrentColor").innerHTML = colors[colorIndex];
}

c.addEventListener('mousedown', e => {
  var x = e.offsetX; //returns the x-coordinate of the click relative to the canvas
  var y = e.offsetY; //returns the y-coordinate of the click relative to the canvas

  //e.preventDefault() //we did not use this function, but it prevents default action of an event from occurring
  //this would be more  helpful if we added an event listener for mousedown on the entire page
  //but we only added a listener to canvas, so this is unnecessary

  if (mode == 1){
    ctx.fillRect(x, y, 20, 20);
  }
  else {
    ctx.beginPath(); //begins a path or resets the current path
    //analogous to putting the tip of your pencil down on the paper
    ctx.arc(x, y, 10, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
  }
});

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);

var togglebtn = document.getElementById("toggle");
togglebtn.addEventListener('click', toggle);

var colorizebtn = document.getElementById("color");
colorizebtn.addEventListener('click', colorize);
