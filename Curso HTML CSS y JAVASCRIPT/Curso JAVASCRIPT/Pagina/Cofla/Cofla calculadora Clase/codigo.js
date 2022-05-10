class Calculadora {
	constructor(){

	}
	sumar(num1,num2){
		return parseInt(num1) + parseInt(num2);
	}

	restar(num1,num2){
		return parseInt(num1) - parseInt(num2);
	}

	dividir(num1,num2){
		return parseInt(num1) / parseInt(num2);
	}

	multiplicar(num1,num2){
	return parseInt(num1) * parseInt(num2);
	}

	potenciar(num,exp){
		return num**exp;
	}
	raizCuadrada(num){
		return Math.sqrt(num);
	}
	raizCubica(num){
		return Math.cbrt(num);
	}
}

const calculadora = new Calculadora();

alert("¿Qué operación deseas realiazar?");
let operacion = prompt("1: Suma, 2: Resta, 3: División. 4: Multiplicación, 5: Potenciación, 6: Raiz Cuadrada , 7: Raiz Cubica")

if(operacion == 1){
	let numero1 = prompt("Primer numero")
	let numero2 = prompt("Segundo numero")
	resultado = calculadora.sumar(numero1,numero2)
	alert(`Tu resultado es ${resultado}`);
}

if(operacion == 2){
	let numero1 = prompt("Primer numero")
	let numero2 = prompt("Segundo numero")
	resultado = calculadora.restar(numero1,numero2)
	alert(`Tu resultado es ${resultado}`)
}
if(operacion == 3){
	let numero1 = prompt("Primer numero")
	let numero2 = prompt("Segundo numero")
	resultado = calculadora.dividir(numero1,numero2)
	alert(`Tu resultado es ${resultado}`)
}
if(operacion == 4){
	let numero1 = prompt("Primer numero")
	let numero2 = prompt("Segundo numero")
	resultado = calculadora.multiplicar(numero1,numero2)
	alert(`Tu resultado es ${resultado}`)
}
if(operacion == 5){
	let numero1 = prompt("Numero a potenciar")
	let numero2 = prompt("exponente")
	resultado = calculadora.potenciar(numero1,numero2)
	alert(`Tu resultado es ${resultado}`)
}
if(operacion == 6){
	let numero1 = prompt("Numero para elevar al Cuadrado")
	resultado = calculadora.raizCuadrada(numero1)
	alert(`Tu resultado es ${resultado}`)
}
if(operacion == 7){
	let numero1 = prompt("Numero para elevar al Cubo")
	resultado = calculadora.raizCubica(numero1)
	alert(`Tu resultado es ${resultado}`)
}
