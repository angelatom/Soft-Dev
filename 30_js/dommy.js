var heading;
var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = heading;
};

var removeItem = function(e) {

};

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', );
    lis[i].addEventListener('mouseout', );
    lis[i].addEventListener('click', );
};

var addItem = function(e) {
    var list = [];
    var item = document.createElement("li");

};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e){
    console.log(e);
};


var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);