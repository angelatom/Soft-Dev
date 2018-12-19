/*
Team SlipKnot -- Angela Tom + Bo Hui Lu
SoftDev1 pd6
K28 -- Sequential Progression
2018-12-18
*/

var fibonacci = (n) => {
    if (n <= 0){
	return 0;
    }
    else if (n == 1){
	return 1;
    }
    else{
	return fibonacci(n-2)  + fibonacci(n -1);
    }
    
}

//console.log(fibonacci(0))

//console.log(fibonacci(1))

//console.log(fibonacci(2))

//console.log(fibonacci(3))

var gcd = (a, b) => {
    c = a % b;
    if (c == 0){
	return b;
    }
    else {
	return gcd(b, c);
    }
}

var students = ["Angela", "Person", "Person2", "Someone", "Name", "Name2"]

var randomStudent = () => {
    //console.log(students.length)
    //console.log(Math.random(students.length))
    return students[Math.floor(Math.random() * students.length)]
}
