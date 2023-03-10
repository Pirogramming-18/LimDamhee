/*
const date = new Date(); // 현재 날짜 객체 만들기
const date2 = new Date(2023, 3, 2); // 지정 날짜 객체 만들기

console.log(date);
console.log(date2);

// 년, 월, 일, 요일 가져오기

const viewYear = date.getFullYear(); // 연도 가져오기
const viewMonth = date.getMonth(); // 월 가져오기
const viewDate = date.getDate(); // 일 가져오기
const viewDay = date.getDay(); // 요일 가져오기

console.log(viewYear); //2023
console.log(viewMonth); // 0    (0~11로 반환) !!
console.log(viewDate); // 5     (1~31로 반환)
console.log(viewDay);  // 4     (1~7로 반환, 1-월, 2-화 ...)

// 지난 달 마지막 날짜와 요일 & 이번 달 마지막 날짜와 요일

// 지난 달 마지막 날짜와 요일
const prevLast = new Date(viewYear, viewMonth, 0);
const prevDate = prevLast.getDate();
const prevDay = prevLast.getDay();

// 찍어보기
console.log(prevLast) // -> 저번 달 마지막 날짜
console.log(prevDate) // -> 31
console.log(prevDay) //  -> 6(토요일)

//이번 달 마지막 날짜와 요일
const thisLast = new Date(viewYear, viewMonth + 1, 0);
const thisDate = thisLast.getDate();
const thisDay = thisLast.getDay();

// 찍어보기
console.log(thisLast); // => 이번 달 마지막 날짜로 나옴
console.log(thisDate); // => 31
console.log(thisDay); // 2 (화요일)

//전체 날짜에 필요한 날짜 만들기
const prevDates = []; // [26, 27, 28, 29, 30, 31]
const nextDates = []; // [1, ...]
const thisDates = [...Array(thisDate + 1).keys()].slice(1); // [1, 2, 3, ..., 31]

// ... => 
// Array(n) => 길이가 n인 배열 생성 [undefined, undefined ...]
// .keys() => 인덱스가 key로 바뀜 [0,1,2,3, ... , 31]
// slice(n) => 앞의 요소 n개 삭제 후 반환 [1,2,3,4, ... 31]


// 이전 달 날짜 배열 채우기
// 저번 달이 목요일인 경우 => 목요일 = 4 prev = 30
if(prevDay !== 6) { // 전 달 마지막 요일이 토요일이면 전 달 날짜 배열이 필요없음
    for (let i = 0; i < prevDay + 1; i++) {
        //for (let i=0; i<4+1; i++)
        prevDates.unshift(prevDate - i);
        // 31-0, 31-1, 31-2, 31-3 ...
        // 31, 30, 29, 28, 27
        // [31], [30, 31], [29, 30, 31] ... <= unshift 사용해서 앞부터 넣음
    }
}


// 다음 날 날짜 배열 채우기
for (let i = 1; i < 7-thisDay; i++) {
    // for(1, 5)
    nextDates.push(i);
}

// nextDates = [1,2,3,4];

//unshift() 배열 앞 부분에 삽입 
//push() 배열 뒷 부분에 삽입

// 날짜 그리기

//Dates라는 배열로 모두 합치기
const dates = prevDates.concat(thisDates, nextDates);
// => [(지난 달 => 지금은 없음)] + [1, ~ 31] + [1 ~ 4]
// => [1~ 31, 1 ... 4]

// div로 감싸서 넣기
dates.forEach((date, i) => {
    dates[i] = `<div class="date"> ${date} </div>`;
});


// 배열.forEach((요소, 배열 인덱스) => {});

// => [<div class="date"> 1</div>, <div class="date"> 2</div>,
// <div class="date"> 31</div> ... <div class="date"> 1</div>, <div class="date"> 4</div>]

// html dates 그리기

document.querySelector('.dates').innerHTML = dates.join('');
*/

//캘린더 만드는 함수 만들기
let date = new Date();

const makeCalendar = () => {
    // 캘린더에 보이는 년도와 달을 보여주기 위해
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`

    // 지난 달 마지막 날짜와 요일
    const prevLast = new Date(viewYear, viewMonth, 0);
    const prevDate = prevLast.getDate();
    const prevDay = prevLast.getDay();

    //이번 달 마지막 날짜와 요일
    const thisLast = new Date(viewYear, viewMonth + 1, 0);
    const thisDate = thisLast.getDate();
    const thisDay = thisLast.getDay();

    //전체 날짜에 필요한 날짜 배열 만들기
    const prevDates = []; // [26, 27, 28, 29, 30, 31]
    const nextDates = []; // [1, ...]
    const thisDates = [...Array(thisDate + 1).keys()].slice(1); // [1, 2, 3, ..., 31]
    //thisDate + 1 => 0~31까지 배열 생성. slice(1) => 0 자르고 1~31 배열 반환

    if(prevDay !== 6) { 
        for (let i = 0; i < prevDay + 1; i++) {
            prevDates.unshift(prevDate - i);
        }
    }

    // 다음 날 날짜 배열 채우기
    for (let i = 1; i < 7-thisDay; i++) {
        nextDates.push(i);
    }

    //Dates라는 배열로 모두 합치기
    const dates = prevDates.concat(thisDates, nextDates);
    
    // div로 감싸서 넣기
    dates.forEach((date, i) => {
        dates[i] = `<div class="date"> ${date} </div>`;
    });

    //html dates 그리기
    document.querySelector('.dates').innerHTML = dates.join('');


    // 여기부터 다시 합시다요


    // 오늘 날짜 표시
    const today = new Date();
    if (viewMonth === today.getMonth && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.this')) {
            if (+date.innerText === today.detDate()) {
                date.classList.add('today');
                break;
            }
        }
    }

    // 현재 달 첫번째 시작일의 인덱스, 마지막 일의 인덱스
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(thisDate);

    dates.forEach((date, i) => {
        // 삼항연산자 (조건문) ? [참일 떄 실행] : [거짓일 때 실행]
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 ? 'this' : 'other';

        dates[i] = `<div class="date">${date}</div>`
        dates[i] = `<div class="date"><span class="${condition}">${date}</span></div>`
    });
}

//함수 실행
makeCalendar();

// 이전 달 그리는 함수
const prevMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() - 1);
    makeCalendar;
}

//다음 달 그리는 함수
const nextMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() + 1);
    makeCalendar;
}

//현재 달 그리는 함수
const curMonth = () => {
    date = new Date();
    makeCalendar();
}
