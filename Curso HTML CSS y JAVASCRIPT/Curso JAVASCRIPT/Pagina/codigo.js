
const contenedor = document.querySelector(".contenedor");

const parrafo = document.createElement("p").innerHTML = "parrafo";
const h2_nuevo = document.createElement("h2");
h2_nuevo.innerHTML = "titulo"

const h2_antiguo = document.querySelector(".h2");

let respuesta = contenedor.hasChildNodes();

if (respuesta){
	document.write("El elemento tiene hijos");
} else {
	document.write("El elemento no tiene hijos");
}