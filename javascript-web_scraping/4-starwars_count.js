#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const response = JSON.parse(body);
    let wedgeAntillesCount = 0;
    response.results.forEach(element => {
      if (element.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        wedgeAntillesCount++;
      }
    });
    console.log(wedgeAntillesCount);
  }
});
