const fs = require('fs')


function getInputData(fileName) {
    try {
        const data = fs.readFileSync(`./inputs/${fileName}.txt`, 'utf8');
        return data;
      } catch (err) {
        console.error(err)
      }
}

module.exports = getInputData;