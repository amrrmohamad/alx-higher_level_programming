#!/usr/bin/node

const arg = require('process');
const num = process.argv[2];

if (!isNaN(num)){
	for (let i = 0; i < num; i++ ){
		console.log("C is fun");
	}
} else {
    console.log("Missing number of occurrences");
}