const getInputData = require("./utils");


const rawData = getInputData("day1");
const  data = rawData.split("\n").map(x => parseInt(x,10));
// create a set for quick lookup
const dataSet = new Set(data);

// part 1
// find the two numbers in input which sum to form 2020
// multiply the numbers to get result
// part 2
// find three numbers which do the same

function part1(SUM) {
  // subtract each item from 2020, check if diff is present in list
  for (let i = 0; i < data.length; i++) {
    const diff = SUM - data[i];
    if (dataSet.has(diff)) {
      return diff *  data[i];
    }
  }
}


function part2(SUM) {
  // subtract each item from 2020, call part 1 with the diff
  for (let i = 0; i < data.length; i++) {
    const diff = SUM - data[i];
    const res = part1(diff);
    if (res) {
      return data[i] *  res;
    }
  }
}

// corner case of the same number being used twice
// can be avoided by using a map with count and some extra checks

// part 1
const r1 =  part1(2020);
console.log('result 1', r1);

const r2 =  part2(2020);
console.log('result 2', r2);
