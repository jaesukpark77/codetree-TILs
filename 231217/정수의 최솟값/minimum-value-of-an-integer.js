// 최솟값을 반환하는 함수를 작성합니다.
function min(a, b, c) {
    let minVal = a;
    if (minVal > b) minVal = b;
    if (minVal > c) minVal = c;

    return minVal;
}

// 변수 선언 및 입력
const fs = require("fs");
let [a, b, c] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

console.log(min(a, b, c));