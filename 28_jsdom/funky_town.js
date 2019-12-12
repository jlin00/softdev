//Jackie Lin and Yifan Wang (Team HydroFlask)
//SoftDev1 pd1
//K#28 -- Sequential Progression
//2019-12-11

// console.log("this is a test");

//function for factorial
var fact = function(n) {
  if (n < 2) return 1;
  return fact(n - 1) * n;
};

//function for fibonacci
var fib = function(n) {
  if (n <= 0) return 0;
  if (n == 1) return 1;
  return fib(n - 1) + fib(n - 2);
};

//function for GCD
var gcd = function(a, b){
  if (b > a) return gcd(b, a);
  if (a % b == 0) return b;
  return gcd(b, a % b);
};

var test = ["Tiffany", "Jackie", "Tina", "Wooooo", "Bob", "Joe", "Esteban"]

//function for selecting random student from a given list
var randomStudent = function() {
  var index = parseInt(Math.random() * test.length);
  return test[index];
};

var inputHTML = document.getElementById("input");
var outputHTML = document.getElementById("output");

document.getElementById("fact").addEventListener("click", function() {
    inputHTML.innerHTML = "fact(5)"
    var ans = fact(5);
    outputHTML.innerHTML = ans;
    console.log(ans);
});

document.getElementById("fib").addEventListener("click", function() {
  inputHTML.innerHTML = "fib(5)"
  var ans = fib(5);
  outputHTML.innerHTML = ans;
  console.log(ans);
});

document.getElementById("gcd").addEventListener("click", function() {
  inputHTML.innerHTML = "gcd(36, 84)"
  var ans = gcd(36, 84);
  outputHTML.innerHTML = ans;
  console.log(ans);
});

document.getElementById("rand").addEventListener("click", function() {
  inputHTML.innerHTML = "randomStudent() from [" + test + "]";
  var ans = randomStudent();
  outputHTML.innerHTML = ans;
  console.log(ans);
});
