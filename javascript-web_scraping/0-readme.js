#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);

try {
  const content = fs.readFileSync(args[0], 'utf8');
  console.log(content);
} catch (error) {
  console.log(error);
}
