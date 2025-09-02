let fotos = document.getElementsByClassName("imagen")
for (const foto of fotos){
    foto.onclick = () => {
        if (foto.id === "giant") return
        for (const foto of document.getElementsByClassName("imagen")) {
            foto.classList.toggle("hidden")
        }
        foto.id = "giant"
        document.getElementById("caja-texto").classList.toggle("hidden")
        let x = document.createElement("h1")
        x.innerText = "X"
        x.id = "equis"
        x.onclick = () => {
            document.getElementById("caja-texto").classList.toggle("hidden")
            foto.id = ""
            for (const foto of document.getElementsByClassName("imagen")) {
                foto.classList.toggle("hidden")
            }
            document.getElementById("caja-fotos").removeChild(x)
        }
        document.getElementById("caja-fotos").appendChild(x)
    }
}