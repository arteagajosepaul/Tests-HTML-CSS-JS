let botones = document.getElementsByClassName("boton");
for (let boton of botones) {
    boton.addEventListener("click", function() {
        alert("Botón clickeado!");
    });
}


