


function playTheGame() {
	let ask = confirm("would you like to play the game?")
	if (ask === true) {
		num()
	}
	else {
		alert("No problem, Goodbye!")
	}
}
playTheGame()

function num() {
	let num = prompt("chose a number between 0 and 10")
	let ex = Number(num)
	if (isNaN(ex)) {
		alert("Sorry, Not a Number, Goodbye")
	}
	else if (ex > 10) {
		alert("sorry its not a good number goodbye!")
	}
	else {
		let computerNumber = Math.floor(Math.random() * (9) + 1)
		console.log(computerNumber)
		compareNumbers (ex, computerNumber)
	}
}


function compareNumbers(userNumber,computerNumber) {
	
	if (userNumber == computerNumber){
		alert("WINNER")
	}

	else if (userNumber > computerNumber){
		alert('Your number is bigger then the computer’s, guess again')
		
		prompt("chose a number between 0 and 10")
		

	}

	else if (userNumber < computerNumber){
		alert('Your number is smaller then the computer’s, guess again')
		prompt("chose a number between 0 and 10")
		
	}



}