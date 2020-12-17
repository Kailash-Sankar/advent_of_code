const getInputData = require("./utils");

const rawData = getInputData("day3");

/*

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

*/

const rows = rawData.split("\n");
const maxIdx = rows[0].split("").length;

function checkSlopes({ down, right }) {
  let treeCount = 0;
  let currentIdx = 0;
  for (let i = 0; i < rows.length; i=i+down) {
    const row = rows[i];
    if (row[currentIdx] == "#") {
      treeCount++;
    }
    currentIdx = (currentIdx + right) % maxIdx;
  } 
  return treeCount;
}

function main() {
    const slopes = [
        { right: 1, down: 1 },
        { right: 3, down: 1 },
        { right: 5, down: 1 },
        { right: 7, down: 1 },
        { right: 1, down: 2 },
    ]

    let result = 1;
    slopes.forEach( slope => {
        result = result * checkSlopes(slope);
    })
    console.log("result", result);
}

main();

