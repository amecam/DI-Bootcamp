


//-----------exercise 1------------------


// function infoAboutme(){
// 	let name = "Amecam";
// 	let age = 29;
// 	let hobbies = 'watching sports';
// 	console.log('my name is ' +name+  ' my age is ' +age+  ' my hobbies are ' +hobbies);
// }
// infoAboutme ()

// function infoAboutPerson (personName, PersonAge, personFavoriteColor){

// 	console.log("my name is " + personName +" my age is " + PersonAge +" my favorite color is " + personFavoriteColor )
// }
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

//------------exercise 2---------------------
// function calculateTip(){
// 	let bill = prompt("Put in number")
// 	if (bill>50) {
// 		console.log(`Pay $ ${bill*1.2} `)
// 	} else if (50<bill<200) {
// 		console.log(`Pay $ ${bill*1.15} `)
// 	} else if (bill>200){
// 		console.log(`Pay $ ${bill*1.1} `)
// 	}
// }
// calculateTip()

//-----------exercise 3-----------------------

// let sum= 0
// function isDivisible(){
// 	for(let i=0; i<=500; i++){
// 		if (i%23==0) {
// 			console.log(i);
// 			sum += i;
// 		}
// 	}

// }
// isDivisible()
// console.log(sum);

//------exercise 4----------------------

// let stock = { 
// 	"banana": 6, 
// 	"apple": 0,
// 	"pear": 12,
// 	"orange": 32,
// 	"blueberry":1
// }  

// let prices = {    
// 	"banana": 4, 
// 	"apple": 2, 
// 	"pear": 1,
// 	"orange": 1.5,
// 	"blueberry":10
// } 

// let shoppingList = ['banana','orange','apple'];

// function myBill() {
// 	bill = 0
// 	for (let i of shoppingList) {
// 		if (i in stock && stock[i] !==0) {
// 			bill +=prices[i];
// 			stock[i] -= 1;
// 		} 

// 	} 
// 	console.log(bill);
// }

// myBill()

//----------exercise 6----------------------




function hotelCost(){
	let nights = prompt("number of nights would like to stay in hotel");
	while(isNaN(nights)){
		nights = prompt("number of nights would like to stay in hotel");
	}
	return nights * 140
}
hotelCost()
function planeRideCost(){
	let destination = prompt("enter your destination").toLowerCase()
	while(!isNaN(destination)){
		destination = prompt("enter your destination").toLowerCase()
	}
	if(destination === "london"){
		return 183;
	}else if (destination === "paris") {
		return 220;
	}else{
		return 300;
	}
}
planeRideCost()
function rentalCarCost(){
	let day = prompt("number of day")
	while (isNaN(day)) {
		day = prompt("number of day")
	}
	if(day < 10){
		return day*40
	}else{
		return (day*40)/1.05
	}
}
rentalCarCost().toFixed(2)


//----------------------------
































