
function handleSubmit(e) {
	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	// this reprezentuje ten formular, ktory odosielame
	const ves = this.querySelector("textarea").value; // Načítame text z textarea
	const width = document.querySelector("section:nth-child(2)").clientWidth; // Načítame aktuálnu šírku výstupného okna

	const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
	formular.append('ves', ves); // Pridáme tam naše hodnoty
	formular.append('width', width);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
	fetch(url, { method: method, body: formular }) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob()) // Dostali sme binárne dáta (blob)
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image); // Nastavíme src našeho <img> na načítaný obrázok
		})
}
document.querySelector("form").addEventListener("submit", handleSubmit); // Nastavíme formulár, aby pri submit udalosti spustil našu handleSubmit funkciu
let textLength = 0;
let text = "Do textového poľa zadaj ves súbor s veľkosťou obrázka 600:400. Pre nový hárok stlač vymazať. "

function type() {
	let textChar = text.charAt(textLength++);
	let paragraph = document.getElementById("typed");
	let charElement = document.createTextNode(textChar);
	paragraph.appendChild(charElement);
	if (textLength < text.length + 1) {
		setTimeout('type()', 50);
	} else {
		text = '';
	}
}

document.addEventListener("DOMContentLoaded", function () {
	type();
});


function clear() {
	// When clear button is clicked

	let color = "#FFFFFF";
	let text = "VES v1.4 600 400\n"
	let columns = text.split('\n')
	let background = columns[0] + "\n" + "CLEAR " + color;
	document.querySelector("#ves").value = background
	document.getElementById("vykresli").click();

}


function download_image(linkElement) {
	// When download button is clicked
	let source = document.getElementById("output").src;
	linkElement.href = source
}

/*FOOTER */

const gl = document.getElementById("canvas").getContext("webgl");
const programInfo = twgl.createProgramInfo(gl, ["vertexShader", "fragmentShader"]);

const arrays = {
	position: [-1, -1, 0, 1, -1, 0, -1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0],
};
const bufferInfo = twgl.createBufferInfoFromArrays(gl, arrays);

let mouseX = 0, mouseY = 0;

document.getElementById("canvas").addEventListener('mousemove', e => {
	mouseX = e.clientX;
	mouseY = e.clientY;
});


function render(time) {
	//Paints only 25% pixels in the screen space, 
	//Slightly lower resolution but much better performance!
	//See also: the zoom feature of https://glslsandbox.com/

	twgl.resizeCanvasToDisplaySize(gl.canvas, 0.5);

	//Paints 4x the number of pixels.
	//Very computationally expensive in full screen on desktop devices
	//twgl.resizeCanvasToDisplaySize(gl.canvas, 1.0); 

	gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);

	const uniforms = {
		u_time: (time) * 0.002,
		u_resolution: [gl.canvas.width, gl.canvas.height],
		u_mouse: [mouseX, mouseY],
	};

	gl.useProgram(programInfo.program);
	twgl.setBuffersAndAttributes(gl, programInfo, bufferInfo);
	twgl.setUniforms(programInfo, uniforms);
	twgl.drawBufferInfo(gl, bufferInfo);

	requestAnimationFrame(render);
}
requestAnimationFrame(render);