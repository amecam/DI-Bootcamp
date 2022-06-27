
let sentence = prompt ("The traffic today was not bad")

let sentenceArr = sentence.split(" ");
let wordNot = sentenceArr.indexOf("not");
let wordBad = sentenceArr.indexOf("bad");
let badAfterNot = wordBad > wordNot;
let result;
if(badAfterNot){
  result = sentence.replace("not","").replace("bad","good").replace("","");
} else{
  result = sentence;
}
console.log(result);