#!/usr/bin/node

const arg = require('process');
const num = arg.argv[2];

if (!isNaN(num)){
	for(let i = 0; i < num ; i++){
		let row = '';
		for(let j = 0; j < num; j++){
			row += 'X';
		}
		console.log(row);
	}
}else{
	console.log('Missing size');
}
