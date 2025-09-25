import {region_comuna} from './region_comuna.js'

const regiones = region_comuna["regiones"].map(obj => obj.nombre)
let comunas = (region) => {
    let regionObj = region_comuna["regiones"].find(obj => obj.nombre == region)
    if (!regionObj) return []
    return regionObj.comunas.map(obj => obj.nombre)
}

function validateText(text, minLength=1, maxLength){
    if (!text) return false
    let trimmed = text.trim()
    return trimmed.length >= minLength && trimmed.length <= maxLength
}

function validateEmail(email){
    if (!email) return false
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    return re.test(email) && email.trim().length <= 100
}

function validatePhone(phone){
    if (!phone) return true
    // La expresion regular tambien testea el largo del numero
    let re = /^\+\d{3}\.\d{8}$/
    return re.test(phone)
}

function validateCheckboxes(checkboxes){
    let checkedCount = 0
    for (const checkbox of checkboxes){
        if (checkbox.val.checked){
            checkedCount++
            let opt = checkbox.val.name
            let inp = document.getElementById(opt + "-input").value
            if (inp.length < 4 || inp.length > 50 || !inp) return false
        }
    }
    return checkedCount <= 5
}

function validateRadios(r1, r2){
    return r1.checked || r2.checked
}

function validateNumber(number){
    if (!number) return false
    return number >= 1
}

function validateDate(date, min){
    if (!date) return false
    let re = /^\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}$/
    let dateObj = new Date(date)
    let minDateObj = new Date(min)
    return re.test(date) && dateObj.getTime() >= minDateObj.getTime()
}

function validateFiles(files){
    if (files.length === 0 || !files) return false
    for (const file of files){
        if (!file) return false
        let fileFamily = file.type.split("/")[0]
        if (fileFamily !== "image") return false
    }
    return files.length <= 5
}

function validateSelect(select, arr){
    if (!select) return false
    return arr.includes(select)
}

function validateForm(){
    const form = document.forms["myForm"]
    const region = form["select-region"]
    const comuna = form["select-comuna"]
    const sector = form["sector"]
    const nombre = form["nombre"]
    const email = form["email"]
    const telefono = form["tel"]

    const whatsapp = form["whatsapp"]
    const tiktok = form["tiktok"]
    const x = form["x"]
    const instagram = form["instagram"]
    const telegram = form["telegram"]
    const otra = form["otra"]
    const checkboxes = [{name: "whatsapp", val: whatsapp},
        {name:"tiktok", val: tiktok},
        {name: "x", val: x},
        {name: "instagram", val: instagram},
        {name: "telegram", val: telegram},
        {name: "otra", val: otra}
    ]

    const perro = form["perro"]
    const gato = form["gato"]

    const cantidad = form["cantidad"]
    const edad = form["edad"]
    const meses = form["meses"]
    const años = form["años"]
    const fecha = form["fecha"]
    const fotosClass = document.getElementsByClassName("fotos")
    const fotos = Array.prototype.map.call(fotosClass, fotoDom => fotoDom.files[0])

    let invalidInputs = []
    let isValid = true
    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };

    if (!validateSelect(region.value, regiones)){
        setInvalidInput("Region");
    }
    if (!validateSelect(comuna.value, comunas(region.value))){
        setInvalidInput("Comuna");
    }
    if (!validateText(sector.value, 1, 100) && sector.value.trim().length > 0){
        setInvalidInput("Sector");
    }
    if (!validateText(nombre.value, 3, 200)){
        setInvalidInput("Nombre");
    }
    if (!validateEmail(email.value)){
        setInvalidInput("Email");
    }
    if (!validatePhone(telefono.value)){
        setInvalidInput("Telefono");
    }
    if (!validateCheckboxes(checkboxes)){
        setInvalidInput("Contactar por");
    }
    if (!validateRadios(perro, gato)){
        setInvalidInput("Tipo de mascota");
    }
    if (!validateNumber(parseInt(cantidad.value))){
        setInvalidInput("Cantidad");
    }
    if (!validateNumber(parseInt(edad.value))){
        setInvalidInput("Edad");
    }
    if (!validateRadios(meses, años)){
        setInvalidInput("Unidad medida edad");
    }
    if (!validateDate(fecha.value, fecha.min)){
        setInvalidInput("Fecha entrega");
    }
    if (!validateFiles(fotos)){
        setInvalidInput("Fotos");
    }

    let validationListElem = document.getElementById("val-list")
    let validationBox = document.getElementById("error-msg")
    let msgTitle = document.getElementById("msg-title")
    let msg = document.getElementById("msg")
    if (!isValid) {
        msgTitle.innerText = "Hubo un error enviando el formulario"
        msg.innerText = "Los siguientes campos son inválidos: "
        validationListElem.textContent = "";
        // agregar elementos inválidos al elemento val-list.
        for (let input of invalidInputs) {
            let listElement = document.createElement("li");
            listElement.innerText = input;
            validationListElem.append(listElement);
        }

        // hacer visible el mensaje de validación
        validationBox.hidden = false;
        form.style.display = "none";
        let backButton = document.createElement("button");
        backButton.innerText = "Volver";
        backButton.addEventListener("click", () => {
            // Mostrar el formulario nuevamente
            form.style.display = "block";
            validationBox.hidden = true;
        });
        validationListElem.appendChild(backButton);
    } else {
        msgTitle.innerText = "¡Formulario válido! ¿Deseas enviarlo o volver?"
        msg.hidden = true
        validationListElem.textContent = "";
        // Ocultar el formulario
        form.style.display = "none";

        // Agregar botones para enviar el formulario o volver
        let submitButton = document.createElement("button");
        //submitButton.type = "submit";
        submitButton.innerText = "Enviar";

        let backButton = document.createElement("button");
        backButton.innerText = "Volver";
        backButton.addEventListener("click", () => {
            // Mostrar el formulario nuevamente
            form.style.display = "block";
            validationBox.hidden = true;
        });

        submitButton.onclick = () => {
            submitButton.hidden = true
            form.submit()
        }

        validationListElem.appendChild(submitButton);
        validationListElem.appendChild(backButton);

        // hacer visible el mensaje de validación
        validationBox.hidden = false;
    }

}

const formButton = document.getElementById("submit-btn")
formButton.addEventListener("click", validateForm)