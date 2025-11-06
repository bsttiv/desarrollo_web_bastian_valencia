let pageSelector = document.getElementById("select-page")
if (pageSelector){
    pageSelector.onchange = () => {
        const pagina = pageSelector.value
        cargarListado(pagina)
    }
}

async function enviarNota(avisoId, nota){
    if (!nota || !avisoId) {throw new Error("avisoId o nota es nulo")}
    if (Number.isNaN(Number(nota)) || Number.isNaN(Number(avisoId))){throw new Error("Nota o ID no es un entero")}
    if (!Number.isInteger(Number(nota)) || !Number.isInteger(Number(avisoId))){throw new Error("Nota o ID no es un entero")}
    try{
        const resp = await fetch(`${window.origin}/api/notas`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    avisoId: avisoId,
                    nota: parseInt(nota)
                })
            })
        if (!resp.ok) {
            throw new Error(`Error en la petición: Status ${resp.status}`);
        }
        const json = await resp.json()
        if (json.error){
            throw new Error(`Error de respuesta del endpoint: ${json.error}`)
        }
        const tr = document.getElementById("aviso-" + avisoId);
        if (tr && json.status === "ok") {
            const notaTd = tr.children[4];
            if (notaTd) {
                notaTd.innerText = json.notaActual;
            }
        }
    } catch (error){
        console.log("Error: " + error)
    }
}

function crearDialogo(avisoId){
    if (document.getElementById("modal-overlay")) {
        return; 
    }

    const overlay = document.createElement("div");
    overlay.id = "modal-overlay";

    const modal = document.createElement("div");
    modal.id = "nota-modal";

    const header = document.createElement("div");
    header.className = "modal-header";
    header.innerText = `Evaluar Aviso ID: ${avisoId}`;
    modal.appendChild(header);

    const body = document.createElement("div");
    body.className = "modal-body";
    
    const label = document.createElement("label");
    label.setAttribute("for", "nota-select-dialog");
    label.innerText = "Nota (de 1 a 7):";
    body.appendChild(label);

    const select = document.createElement("select");
    select.id = "nota-select-dialog";
    
    for (let i = 1; i <= 7; i++) {
        const option = document.createElement("option");
        option.value = i;
        option.text = i;
        select.appendChild(option);
    }
    body.appendChild(select);
    modal.appendChild(body);

    const actions = document.createElement("div");
    actions.className = "modal-actions";

    const closeBtn = document.createElement("button");
    closeBtn.innerText = "Cerrar";
    closeBtn.className = "btn-secondary";
    closeBtn.onclick = cerrarDialogo;

    const sendBtn = document.createElement("button");
    sendBtn.innerText = "Enviar";
    sendBtn.className = "btn-primary";
    sendBtn.onclick = async () => {
        const notaSeleccionada = select.value;
        await enviarNota(avisoId, notaSeleccionada);
        cerrarDialogo();
    };

    actions.appendChild(closeBtn);
    actions.appendChild(sendBtn);
    modal.appendChild(actions);

    document.body.appendChild(overlay);
    document.body.appendChild(modal);
    
    overlay.onclick = cerrarDialogo;
}

function cerrarDialogo() {
    const modal = document.getElementById("nota-modal");
    const overlay = document.getElementById("modal-overlay");
    if (modal) {
        modal.remove();
    }
    if (overlay) {
        overlay.remove();
    }
}

async function obtenerListado(pagina){
    try{
        const resp = await fetch(
            `${window.origin}/api/listado/${pagina}`,
            {
                method: "GET",
                cache: "no-cache",
            }
        )
        if (!resp.ok) {
            throw new Error(`Error cargando listado: Status ${resp.status}`)
        }
        const json = await resp.json()
        if (json.error) {
            throw new Error(`Error de respuesta del endpoint: ${json.error}`)
        }
        return json
    } catch(error){
        throw new Error("No se pudo obtener el listado: " + error)
    }
}

function crearTd(contenido){
    const td = document.createElement("td")
    td.innerText = contenido
    return td
}

async function cargarListado(pagina){
    try{
        const datos = await obtenerListado(pagina)
        const tabla = document.getElementById("tabla")
        tabla.innerHTML = ""
        datos.forEach(elemento => {
            const tr = document.createElement("tr")
            tr.id = "aviso-"+elemento.id
            tr.classList.add("aviso")
            tr.appendChild(crearTd(elemento.fechaPublicacion))
            tr.appendChild(crearTd(elemento.sector))
            tr.appendChild(crearTd(elemento.cantidadTipoEdad))
            tr.appendChild(crearTd(elemento.comuna))
            tr.appendChild(crearTd(elemento.nota == 0 ? "-" : elemento.nota))
            const td = document.createElement("td")
            const but = document.createElement("button")
            but.innerText = "Evaluar"
            but.classList.add("boton")
            but.onclick = () => {
                crearDialogo(elemento.id)
            }
            td.appendChild(but)
            tr.appendChild(td)
            tabla.appendChild(tr)
        });
    } catch (error){
        console.log("Error: " + error)
    }
}

document.addEventListener("DOMContentLoaded", async function(){
    await cargarListado(0)
})
