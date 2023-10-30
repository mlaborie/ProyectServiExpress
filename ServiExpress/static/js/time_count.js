// time countdown 1
var countDownDate = new Date("Jan 6, 2024 15:37:25").getTime();
var x = setInterval(function() {
var now = new Date().getTime();
var distance = countDownDate - now;
var days = Math.floor(distance / (1000 * 60 * 60 * 24));
var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    
document.getElementById("days").innerHTML = days;
document.getElementById("hours").innerHTML = hours;
document.getElementById("minutes").innerHTML = minutes;
    
if (distance < 0) {
    clearInterval(x);
    document.getElementById("days").innerHTML = "00";
    document.getElementById("hours").innerHTML = "00";
    document.getElementById("minutes").innerHTML = "00";
}
}, 1000);
// time countdown 1

// time countdown 2
var countDownDate = new Date("Jan 4, 2024 15:37:25").getTime();
var x = setInterval(function() {
var now = new Date().getTime();
var distance = countDownDate - now;
var day = Math.floor(distance / (1000 * 60 * 60 * 24));
var hour = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minute = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
var second = Math.floor((distance % (1000 * 60)) / 1000);

document.getElementById("day").innerHTML = day + ":";
document.getElementById("hour").innerHTML = hour + ":";
document.getElementById("minute").innerHTML = minute + ":";
document.getElementById("second").innerHTML = second;
    
if (distance < 0) {
    clearInterval(x);
    document.getElementById("day").innerHTML = "00";
    document.getElementById("hour").innerHTML = "00";
    document.getElementById("minute").innerHTML = "00";
    document.getElementById("second").innerHTML = "00";
}
}, 1000);
// time countdown 2

