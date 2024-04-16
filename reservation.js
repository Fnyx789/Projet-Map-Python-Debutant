const urlParams = new URLSearchParams(window.location.search);
const phone = urlParams.get("phone");
const name = urlParams.get("name");
const date = urlParams.get("date");
const email = urlParams.get("email");
const time = urlParams.get("time")

const phoneText = document.getElementById("phone");
phoneText.textContent = phone;
const nameText = document.getElementById("name");
nameText.textContent = name;
const dateText = document.getElementById("date");
dateText.textContent = date;
const timeText = document.getElementById("time")
timeText.textContent = time
const emailText = document.getElementById("email");
emailText.textContent = email;
console.log(phone);