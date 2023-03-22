#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId || isNaN(parseInt(movieId))) {
  console.error('Invalid movie ID. Please provide a valid integer.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error retrieving film:', error.message);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Error retrieving film: ${response.statusCode} ${response.statusMessage}`);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  if (characters.length === 0) {
    console.log('No characters found for this film.');
    process.exit(0);
  }

  const characterUrls = characters.map((url) => url.replace('http', 'https'));
  const characterNames = [];
  let numResponses = 0;
  for (let i = 0; i < characterUrls.length; i++) {
    request(characterUrls[i], (error, response, body) => {
      if (error) {
        console.error(`Error retrieving character ${i+1}: ${error.message}`);
      } else if (response.statusCode !== 200) {
        console.error(`Error retrieving character ${i+1}: ${response.statusCode} ${response.statusMessage}`);
      } else {
        const character = JSON.parse(body);
        characterNames[i] = character.name;
      }
      numResponses++;
      if (numResponses === characterUrls.length) {
        console.log(characterNames.join('\n'));
      }
    });
  }
});
