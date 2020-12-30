const getInputData = require("./utils");


const keyList = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];

const MIN_MAX_PARAMS = {
    byr: [1920, 2002],
    iyr: [2010, 2020],
    eyr: [2020, 2030],
    hgt: { cm: [150, 193], in: [59, 76] },

}

const validateRange = (rawValue, min, max) => {
    const value = parseInt(rawValue, 10);
    return min <= value && value <= max;
}

const validateHeight = (params) => {
    if(params) {
        const [_,height,unit] = params;
        if( height == parseInt(height,10) && Object.keys(MIN_MAX_PARAMS.hgt).includes(unit)) {
            return validateRange(height,...MIN_MAX_PARAMS.hgt[unit]);
        }
    }
    return false;
}

function isPassportValid(passport) {
    for(let j=0;j<keyList.length;j++) {
        const key = keyList[j];
        if(!(key in passport)) {
            return false;
        }

        const value = passport[key];
        let state = true;
        switch(key) {
            case 'byr':
            case 'iyr':
            case 'eyr':
                state = validateRange(value, ...MIN_MAX_PARAMS[key]);
                break;
            case 'hgt':
                const [params] =  [...value.matchAll(new RegExp(/(\d+)(cm|in)/g))];
                state = validateHeight(params);
                break;
            case 'hcl':
                state = RegExp(/^#[0-9|a-f]{6}$/).test(value);
                break;
            case 'ecl':
                state = ['amb','blu','brn','gry','grn','hzl','oth'].includes(value);
                break;
            case 'pid':
                state = RegExp(/^[0-9]{9}$/).test(value);
                break;
            case 'cid':
            default:
                break;
        }
        if(!state) {
            return false;
        }
    }

    return true;
}

function parsePassports(rawData) {
    const rows = rawData.split("\n");
    let valid = 0;

    let passport = {};
    for(let i=0; i<rows.length; i++) {
        const r = rows[i];
        if(r === '') {
            if(isPassportValid(passport)) {
                valid++;
            }
            passport = {};

        }
        else {
            const items = r.split(' ');
            items.forEach( item => {
                const [key, value] = item.split(':');
                passport[key] = value;
            })
        }
    }
    // Last record
    if(passport && isPassportValid(passport)) {
        valid++;
    }

    return valid;
}


function main() {
    const rawData = getInputData("day4");
    const valid = parsePassports(rawData);
    console.log('valid passports', valid);
}

main();

