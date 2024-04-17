#!/usr/bin/node

const request = require('request');

// Parse command-line arguments
const movieId = process.argv[2];

// Make HTTP GET request to Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  
  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }
  
  // Parse JSON response
  const filmData = JSON.parse(body);
  
  // Extract character names
  const characters = filmData.characters.map(character => character.name);
  
  // Print character names
  characters.forEach(character => console.log(character));
});
