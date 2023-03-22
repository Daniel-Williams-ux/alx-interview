const request = require('request');

const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api';
const movieUrl = `${baseUrl}/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    return;
  }
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;
  const characterNames = [];
  let count = 0;
  for (const url of characterUrls) {
    request(url, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Unexpected status code: ${response.statusCode}`);
        return;
      }
      const character = JSON.parse(body);
      characterNames[characterUrls.indexOf(url)] = character.name;
      count++;
      if (count === characterUrls.length) {
        console.log(characterNames.join('\n'));
      }
    });
  }
});
