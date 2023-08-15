#!/usr/bin/node
const request = require('request');

const main = () => {
  const number = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${number}/`;
  request(url, async function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }
    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map((item) => {
      return new Promise((resolve, reject) => {
        request(item, function (error, response, body) {
          if (error) {
            reject(error);
            return;
          }
          const name = JSON.parse(body).name;
          resolve(name);
        });
      });
    });

    try {
      const characterNames = await Promise.all(characterPromises);
      characterNames.forEach(name => console.log(name));
    } catch (error) {
      console.error(error);
    }
  });
};

main();
