var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.srcElement.innerHTML;
};

var removeItem = function(e) {
  e.srcElement.remove();
};

//helper function for adding event listeners to a list item
var addEvents = function(element) {
  element.addEventListener('mouseover', changeHeading);
  element.addEventListener('mouseout', () => {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
  });
  element.addEventListener('click', removeItem);
}

var lis = document.getElementsByTagName("li");
console.log(lis);

for (var i=0; i < lis.length; i++){
  addEvents(lis[i]);
}

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  addEvents(item);
  list.appendChild(item);
  lis = document.getElementsByTagName("li");
  //console.log(lis);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);
var fibarray = [0,1,1];
var fib = function(n){
    if(n==0){
      return 0;
    }
    if (fibarray[n]){
      return fibarray[n];
    }
    fibarray[n] = fib(n-1) + fib(n-2);
    return fibarray[n];
};

var addFib = function(e) {
  console.log(e);
  fibarray.push(fib(fibarray.length+1));
  var fiblist=document.getElementById("fiblist");
  var item = document.createElement("li");
  document.body.insertAfter(fiblist,item);
  item.innerHTML = fibarray[fibarray.length-1];
};

var addFib2 = function(e) {
  console.log(e);
  ///???
  //DYNAMIC PROGRAMMING
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
