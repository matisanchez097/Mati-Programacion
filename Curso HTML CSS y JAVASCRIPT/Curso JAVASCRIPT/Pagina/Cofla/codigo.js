
dineroCofla = prompt("¿Cuanto dinero tienes cofla?");
dineroRoberto = prompt("¿Cuanto dinero tienes roberto?");
dineroPedro = prompt("¿Cuanto dinero tienes pedro?");

dineroCofla = parseInt(dineroCofla);

if (dineroCofla >= 0.6 && dineroCofla < 1){
	alert("Cofla; Comprate el helado de agua");
	alert("y te sobran" + (dineroCofla - 0.6));

}

else if (dineroCofla >= 1 && dineroCofla < 1.6){
	alert("Cofla; Comprate el helado de crema");
	alert("y te sobran" + (dineroCofla - 1));
}


else if (dineroCofla >= 1.6 && dineroCofla < 1.7){
	alert("Cofla; Comprate el helado de heladix");
	alert("y te sobran" + (dineroCofla - 1.6));
}

else if (dineroCofla >= 1.7 && dineroCofla < 1.8){
	alert("Cofla; Comprate el helado de heladovich");
	alert("y te sobran" + (dineroCofla - 1.7));
}

else if (dineroCofla >= 1.8 && dineroCofla < 2.9){
	alert("Cofla; Comprate el helado de helardo");
	alert("y te sobran" + (dineroCofla - 1.8));
}

else if (dineroCofla >= 2.9) {
	alert("helado con confites o pote de 1kg");
	alert("y te sobran" + (dineroCofla - 2.9));
}

else {
	alert("lo siento Cofla no te alcanza para ningun helado")
}

//Roberto

if (dineroRoberto >= 0.6 && dineroRoberto < 1){
	alert("Comprate el helado de agua");

}

else if (dineroRoberto >= 0.6 && dineroRoberto < 1.6){
	alert("Comprate el helado de crema");
}

else if (dineroRoberto >= 0.6 && dineroRoberto < 1.7){
	alert("Comprate el helado de heladix");
}

else if (dineroRoberto >= 0.6 && dineroRoberto < 1.8){
	alert("Comprate el helado de heladovich");
}

else if (dineroRoberto >= 0.6 && dineroRoberto < 2.9){
	alert("Comprate el helado de helardo");
}

else if (dineroRoberto >= 2.9) {
	alert("helado con confites o pote de 1kg");
}

else {
	alert("lo siento no te alcanza para ningun helado");
}

//Pedro

if (dineroPedro >= 0.6 && dineroPedro < 1){
	alert("Comprate el helado de agua");

}

else if (dineroPedro >= 0.6 && dineroPedro < 1.6){
	alert("Comprate el helado de crema");
}

else if (dineroPedro >= 0.6 && dineroPedro < 1.7){
	alert("Comprate el helado de heladix");
}

else if (dineroPedro >= 0.6 && dineroPedro < 1.8){
	alert("Comprate el helado de heladovich");
}

else if (dineroPedro >= 0.6 && dineroPedro < 2.9){
	alert("Comprate el helado de helardo");
}

else if (dineroPedro >= 2.9) {
	alert("helado con confites o pote de 1kg");
}

else {
	alert("lo siento no te alcanza para ningun helado");
}