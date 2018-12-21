/*
Team SlipKnot -- Angela Tom and Bo Hui Lu
SoftDev1 pd6
K30 -- Sequential Progression III: Season of the Witch
2018-12-21
*/

//changes heading to match "this" which is what the mouse is hovering over
var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = this.innerHTML
};

//default heading for when mouse is not over an item
var setHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
};

var lis = document.getElementsByTagName("li");

//removes "this" which is the item that mouse is hovering over
var removeItem = function(e) {
    this.remove();
};

//goes through list and gives it the remove/change heading functionality
for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', setHeading);
    lis[i].addEventListener('click', removeItem);
};

//adds an entry containing "word" to the list
var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    //updates item with the functionalities of the other parts of the list
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', setHeading);
    item.addEventListener('click', removeItem);
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

//fxn for getting nth num in fib sequence
var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

//for numbering the fib sequence numbers
var counter = 0;
var addFib = function(e){
    console.log(e);

    //retrieves the list that we will be adding to soon, and creates an element for each entry in lis
    var list = document.getElementById("fiblist");
    var item = document.createElement("li");
    //item.setAttribute("fib", );

    //edits the entry to hold the fib numbers and adds it to the list we retrieved
    item.innerHTML = fib(counter);
    list.appendChild(item);
    counter = counter + 1;
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
