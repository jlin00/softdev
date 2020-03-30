//Jackie Lin and Yifan Wang (Team Ketchup Packets)
//SoftDev1 pd1
//K#13 -- Change || Die
//2020-03-31

var pic = document.getElementById("vimage");

var clear = function(){
  while (pic.firstChild){
    pic.removeChild(pic.firstChild);
  }
}

var clearbtn = document.getElementById("clear");
clearbtn.addEventListener('click', clear);

var createcircle = function(e){
  if (e.target == pic){ //blank canvas
    var x = e.offsetX;
    var y = e.offsetY;

    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", 20);
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "blue");
    c.addEventListener('click', changecircle);
    pic.appendChild(c);
  }
}

var changecircle = function(e){ //clicking on circle
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "cyan");
    e.target.setAttribute("stroke", "cyan");
  }
  else{
    var x = Math.floor(Math.random() * 500);
    var y = Math.floor(Math.random() * 500);
    e.target.setAttribute("cx", x);
    e.target.setAttribute("cy", y);
    e.target.setAttribute("fill", "blue");
    e.target.setAttribute("stroke", "blue");
  }
}

pic.addEventListener('click', createcircle);
