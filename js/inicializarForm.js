import {region_comuna} from './region_comuna.js'

const regiones = region_comuna["regiones"].map(obj => obj.nombre)

function llenarSelect(domElement, valor){
    let option = document.createElement("option");
    option.value = valor;
    option.text = valor;
    domElement.appendChild(option)
}

function cargarRegiones(){
    let selectRegiones = document.getElementById("select-region")
    regiones.forEach(region => llenarSelect(selectRegiones, region))
}

function cambiarComunas(){
    let selectComuna = document.getElementById("select-comuna")
    let selectRegiones = document.getElementById("select-region")
    let region = selectRegiones.value
    selectComuna.innerHTML = '<option value="">Seleccione una comuna</option>'
    let regionObj = region_comuna["regiones"].find(obj => obj.nombre == region)
    if (regionObj){
        let comunas = regionObj.comunas.map(obj => obj.nombre)
        comunas.forEach(comuna => llenarSelect(selectComuna, comuna))
    }
}

function cargarFechaDefault(){
    let fechaInput = document.getElementById("fecha")
    let now = new Date()
    let def = new Date()
    def.setTime(now.getTime() + 60*60*1000)
    fechaInput.value = def.toISOString().substring(0,16)
    fechaInput.min = def.toISOString().substring(0,16)
}

let checkboxes = document.getElementsByClassName("chkbx")
for (const checkbox of checkboxes){
    checkbox.checked = false
    checkbox.onchange = () => {
        let opt = checkbox.id.slice(-5)
        if (checkbox.checked) {
            let inp = document.createElement("input")
            inp.type = "text"
            inp.id=opt + "-input"
            inp.minLength = 4
            inp.maxLength = 50
            inp.placeholder = "Introduce tu URL o ID de usuario"
            document.getElementById(opt).appendChild(inp)
        } else{
            document.getElementById(opt).removeChild(document.getElementById(opt + "-input"))
        }
    }
}

let nFotos = 1
let addPhotoBtn = document.getElementById("add-photo")
addPhotoBtn.onclick = () => {
    if (nFotos === 5) return
    let fotoBox = document.getElementById("foto-box")
    let inp = document.createElement("input")
    inp.type = "file"
    inp.name = "foto"
    inp.id = "foto-"+(1+nFotos).toString()
    inp.classList.add("fotos")
    inp.required = true
    inp.accept = "image/*"
    fotoBox.appendChild(inp)
    nFotos++
}

document.getElementById("select-region").addEventListener("change", cambiarComunas);

window.onload = () => {
    cargarFechaDefault()
    cargarRegiones()
}