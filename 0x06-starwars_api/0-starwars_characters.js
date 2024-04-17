#!/usr/bin/node

const request = require('request');

// Extract movie ID from command-line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as the first argument.');
  process.exit(1);
}

// Define function to fetch movie data
function fetchMovieData(movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, (error, response, body) => {
      if (error) {
        reject(`Error fetching movie data: ${error}`);
      } else if (response.statusCode !== 200) {
        reject(`Failed to fetch movie data: Status ${response.statusCode}`);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Define function to print character names
async function printCharacterNames(movieId) {
  try {
    const movieData = await fetchMovieData(movieId);
    const characters = movieData.characters.map(character => character.name);
    characters.forEach(character => console.log(character));
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
}

// Main execution
printCharacterNames(movieId);
