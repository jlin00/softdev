//Jackie Lin and Amanda Zheng (Team DJAJ)
//SoftDev1 pd1
//K#03 -- Canvas
//2020-02-05

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#0000ff";
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

c.addEventListener('mousedown', e => {
  ctx.fillRect(e.clientX, e.clientY, 50, 50);
  console.log("drawing");
});

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);

var togglebtn = document.getElementById("toggle");
togglebtn.addEventListener('click', toggle);
