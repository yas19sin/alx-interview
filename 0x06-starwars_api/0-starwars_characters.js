#!/usr/bin/node

const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make request to the Star Wars API
request(url, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Display character names in order
  for (let i = 0; i < characters.length; i++) {
    await new Promise((resolve, reject) => {
      request(characters[i], (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character:', charError);
          reject(charError);
          return;
        }

        const character = JSON.parse(charBody);
        console.log(character.name);
        resolve();
      });
    });
  }
});
