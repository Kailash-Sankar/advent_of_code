const getInputData = require("./utils");

const pattern = new RegExp(/(\d+)-(\d+).(\w):.(\w+)/g);

function isRowValid(row) {
    //console.log('row', row);
    const [params] = [...row.matchAll(pattern)];
    //console.log(pattern, 'params', params);
    if(params.length ==  5) {
        const [_, min, max, key, pwd] = params;
        
        const occurences = pwd.split('').filter(x => x === key);
        if(min <= occurences.length && occurences.length <= max ) {
            return true;
        }
    }
    return false;
}

function isRowValidP2(row) {
    //console.log('row', row);
    const [params] = [...row.matchAll(pattern)];
    //console.log(pattern, 'params', params);
    if(params.length ==  5) {
        const [_, min, max, key, pwd] = params;
        const p1 = pwd[min-1] == key ? 1 : 0;
        const p2 = pwd[max-1] == key ? 1 : 0;
        if( (p1 + p2) === 1 ) {
            return true;
        }
    }
    return false;
}



function main() {
    const rawData = getInputData("day2");
    const rows = rawData.split("\n");
    let noOfValidRows = 0;
    for(let i=0; i<rows.length; i++) {
        if( isRowValidP2(rows[i]) ) {
            noOfValidRows++;
        }
    }
    return noOfValidRows;
}

console.log('result', main());



