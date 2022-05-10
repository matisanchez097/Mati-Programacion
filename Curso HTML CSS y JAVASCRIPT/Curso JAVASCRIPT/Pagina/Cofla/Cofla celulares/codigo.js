class App {
	constructor(descargas,puntuacion,peso){
	this.descargas = descargas;
	this.puntuacion = puntuacion;
	this.peso = peso;
	this.iniciada = false;
	this.instalada = false;
	}
	instalar(){
		if (this.instalada == false){
			this.instalada = true;
			alert("La app se ha instalado correctamente!")
		}
	}
	desinstalar(){
		if (this.instalada == true){
			this.instalada = false;
			alert("La app se ha desinstalado correctamente!")
		}
	}
	abrir(){
		if (this.iniciada == false && this.instalada == true){
			this.iniciada = true;
			alert("App Iniciada")
		} else {
			alert("La app que elegiste no esta instalada o no se encontraron los archivos!")
		}
	}
	cerrar(){
		if (this.iniciada == true && this.instalada == true){
			this.iniciada = false;
			alert("App Cerrada")
		} else {
			alert("La app que elegiste no esta instalada o no se encontraron los archivos!")
		}
	}
	appInfo(){
		return `
		Descargas: <b>${this.descargas}</b><br>
		Puntuacion: <b>${this.puntuacion}</b><br>
		Peso: <b>${this.peso}</b><br>
		`
	}
}

app = new App("199.000 Descargas","4.7 Estrllas","900mb");
app2 = new App("390.000 Descargas","4.8 Estrllas","320mb");
app3 = new App("99.000 Descargas","4.2 Estrllas","157mb");
app4 = new App("19.000 Descargas","3.2 Estrllas","90mb");
app5 = new App("14.000 Descargas","2.6 Estrllas","450mb");
app6 = new App("1.000.000 Descargas","5 Estrllas","670mb");
app7 = new App("3.000.000 Descargas","5 Estrllas","400mb");

document.write(`
	<b>Resetas de la nona:</b><br>${app.appInfo()} <br>
	<b>Lazy Town:</b></b><br>${app2.appInfo()} <br>
	<b>Fifa23:</b><br>${app3.appInfo()} <br>
	<b>Rutinas de ejercicio:</b><br>${app4.appInfo()} <br>
	<b>Alarmarapp:</b><br>${app5.appInfo()} <br>
	<b>La reseta de Paulina:</b><br>${app6.appInfo()} <br>
	<b>Truco en linea:</b><br>${app7.appInfo()} <br>
	`)

// app.instalar();
// app.desinstalar();
// app.abrir();
// app.cerrar();
// app.instalar();
// app.abrir();
// app.cerrar();
// app.desinstalar();