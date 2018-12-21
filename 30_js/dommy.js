/*
Team SlipKnot -- Angela Tom and Bo Hui Lu
SoftDev1 pd6
K30 -- Sequential Progression III: Season of the Witch
2018-12-21
*/

var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = this.innerHTML
};

var setHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
};

var lis = document.getElementsByTagName("li");

var removeItem = function(e) {
    this.remove();
};

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', setHeading);
    lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', setHeading);
    item.addEventListener('click', removeItem);
    list.appendChild(item);
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

var counter = 0;
var addFib = function(e){
    console.log(e);
    var list = document.getElementById("fiblist");
    var item = document.createElement("li");
    //item.setAttribute("fib", );
    item.innerHTML = fib(counter);
    list.appendChild(item);
    counter = counter + 1;
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);