var changeHeading = function(e) {
  var h = document.getElementById("h");
  //console.log(e.srcElement.innerHTML);
  h.innerHTML = e.srcElement.innerHTML;
};

var removeItem = function(e) {
  e.srcElement.remove();
};

var lis = document.getElementsByTagName("li");

for (var i=0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeHeading);
  console.log(i);
  lis[i].addEventListener('mouseout', () => {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
  });
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
  //var list = ???;
  var item = document.createElement("li");
  //??? = "WORD";
  //list.???(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  if (n < 2){
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
};

var addFib = function(e) {
  console.log(e);
  ///???
};

var addFib2 = function(e) {
  console.log(e);
  ///???
  //DYNAMIC PROGRAMMING
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
