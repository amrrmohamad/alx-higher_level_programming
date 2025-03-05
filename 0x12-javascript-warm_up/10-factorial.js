#!/usr/bin/node

const arg = require('process');
const num = arg.argv[2];

let res = 1;
function factorial(n){
	while(n != 0 && !isNaN(n)){
		res = res * n;
		n--;
		return factorial(n);
	}
	return res;
}

console.log(factorial(num));