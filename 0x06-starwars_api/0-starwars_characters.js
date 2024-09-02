#!/usr/bin/node

// Import the required module
const request = require('request');

// Get the Movie ID from the first positional argument
const movieID = process.argv[2];

// Define the base URL for the Star Wars API
const baseUrl = 'https://swapi.dev/api/films/';

// Check if the Movie ID is provided
if (!movieID) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

// Define the URL for fetching the movie details
const movieUrl = `${baseUrl}${movieID}/`;

// Fetch the movie details using the request module
request(movieUrl, (error, response, body) => {
  // Handle any errors that occur during the request
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Check if the movie data contains the "characters" list
  if (!movieData.characters) {
    console.error('No characters found for the provided Movie ID.');
    return;
  }

  // Fetch and print each character's name in order
  movieData.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      // Handle any errors that occur during the request
      if (charError) {
        console.error('Error fetching character details:', charError);
        return;
      }

      // Parse the character data as JSON and print the name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

