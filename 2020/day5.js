const getInputData = require("./utils");

function parseSeat(seat) {
  let rowMin = 0;
  let rowMax = 127;
  let colMin = 0;
  let colMax = 7;

  const values = seat.split("");
  values.forEach((v) => {
    switch (v) {
      case "F":
        rowMax = (rowMin + rowMax - 1) / 2;
        break;
      case "B":
        rowMin = (rowMin + rowMax + 1) / 2;
        break;
      case "R":
        colMin = (colMin + colMax + 1) / 2;
        break;
      case "L":
        colMax = (colMin + colMax - 1) / 2;
        break;
    }
  });
  return rowMax * 8 + colMax;
}

function findSeat(seatList) {
  seatList.sort((a, b) => a - b);
  for (let i = 0; i < seatList.length - 1; i++) {
    if (seatList[i] + 1 !== seatList[i + 1]) {
      return seatList[i] + 1;
    }
  }
}

function main() {
  const rawData = getInputData("day5");
  const inputs = rawData.split("\n");
  const seatList = [];
  let maxSeatId = 0;
  inputs.forEach((seat) => {
    const seatId = parseSeat(seat);
    seatList.push(seatId);
    if (seatId > maxSeatId) {
      maxSeatId = seatId;
    }
  });
  console.log("max seatId", maxSeatId);
  console.log("missing seatId", findSeat(seatList));
}

main();
