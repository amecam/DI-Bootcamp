// const myTimeout = setTimeout(myGreeting, 2000);

// function myGreeting() {
//   document.getElementById("demo").innerHTML = "Hello world"
// }

// function myStopFunction() {
//   clearInterval(myTimeout);
// }









// let counter = 0
// let tag = setInterval(function(){
//  var tag = document.createElement("p");
//  var text = document.createTextNode("Hello world");
//  tag.appendChild(text);
//  var element = document.getElementById("container");
//  element.appendChild(tag);
//  counter ++
//  if ( counter >= 5 ){ 
//   stop()
// }
// },2000);

// function stop(){
//   clearInterval(tag);



// }

//==========exercise 2 ===================



// function start(){
//   let box = document.getElementById('animate');
//   let pos = 0;
//   let id = setInterval(function(){
//     if(pos == 350){
//       clearInterval(id)
//     }
//     else{
//       pos++
//       box.style.left = pos + "px";

//     }

//   },1)
// }


///============exercise 3====================




// let elem = document.getElementById('box')

// elem.addEventListener('dragend',function (event){
//   let x = event.clientX
//   let y = event.clientY
//   elem.style.left = x+'px';
//   elem.style.top = y+'px';
// })




//==============daily challenge


// var text = document.getElementById('text');
// text.onkeypress = checkInput;
// text.onpaste = checkInput;

// function checkInput(e) {
//   var e = e || event,
//   char = e.type == 'keypress' 
//   ? String.fromCharCode(e.keyCode || e.which) 
//   : (e.clipboardData || window.clipboardData).getData('Text');
//   if (/[^\d]/gi.test(char)) {
//     return false;
//   }
// }


function lettersOnly(input){
  var regex=/[^a-z]/gi;
  input.value = input.value.replace(regex,"")
}











