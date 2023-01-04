const recordItem = document.getElementById("recordItem");
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

document.getElementById("stop").addEventListener('click', function(){
    let li = document.createElement('li');
    let recordT = document.querySelector(".watch h1").innerText;
    li.innerText = recordT;

    const div = document.createElement("div");
    div.innerHTML = `
        <input type="checkbox" class="ch" />
    `;

    div.innerHTML += li.innerHTML;
    recordItem.append(div);
})


document.getElementById("aa").addEventListener("click", function(){
    checkAll();
})

function checkAll(){
    let checks = document.getElementsByClassName("ch");
    console.log(checks);
    let aa = document.getElementById("aa");
    let ischecked = aa.checked;
    console.log(ischecked);

    if(ischecked == true){
        for ( let i = 0; i < recordItem.childElementCount; i++){
            checks[i].checked = true;
        }
    }
    else {
        for ( let i = 0; i < recordItem.childElementCount; i++){
            checks[i].checked = false;
        }
    }
}