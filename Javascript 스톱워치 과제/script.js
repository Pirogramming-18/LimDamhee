// start
let on = 0;

document.getElementById("start").addEventListener("click", function(){
    if (on > 0)
        return;

    let sec = document.getElementById("sec").innerText;
    let mil = document.getElementById("mil").innerText;

    //start time
    timer_start = setInterval(function(){
        mil++;  
        if (mil == 100){
            mil = "00";
            sec++;
            if (sec < 10) 
                sec = "0" + sec;
            document.getElementById("sec").innerText = sec;
        } else if (mil < 10)
            mil = "0" + mil;
        document.getElementById("mil").innerText = mil;
    }, 10);

    on++;
})

//stop
function stop() {
    clearInterval(timer_start);

    on--;
    if (on < 0)
        on = 0;
}

document.getElementById("stop").addEventListener("click", function(){
    stop();
});

// clear 
document.getElementById("reset").addEventListener("click", function(){
    stop();
    document.getElementById("sec").innerText = "00";
    document.getElementById("mil").innerText = "00";
})


// record

/*
function recordTime(){
    const list = document.querySelector('.recordItem');
    list.innerText = createHTMLString();
    var newli = document.createElement("li");
    var newContent = document.createTextNode(list.innerText);
    document.body.insertBefore(newli, list);
}

function createHTMLString() {
    
    console.log(recordT);
    return `
        ${recordT}
    `;
}

function setEventListeners() {
    const stime = document.querySelector('.stop');
    stime.addEventListener('click', () => recordTime());
}

document.getElementById("stop").addEventListener("click", function(){
    recordTime();
})
*/

document.getElementById("stop").addEventListener('click', function(){
    let recordItem = document.getElementById("recordItem");
    let li = document.createElement('li');
    let recordT = document.querySelector(".watch h1").innerText;
    li.innerText = recordT;

    recordItem.append(li);
})

