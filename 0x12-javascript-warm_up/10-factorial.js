#!/usr/bin/node

const arg = require('process');
const num = arg.argv[2];
let res = 1;

for (let i = num; i > 1; i-- ){
	res = res * i
}
console.log(res);
