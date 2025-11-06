function validarComentario(nombre, comentario){
    return nombre && comentario && nombre.length >= 3 && nombre.length <= 80
    && comentario.length >= 5
}

botonAgregarComentario = document.getElementById("agregar")
botonAgregarComentario.onclick = async () => {
    nombre = document.getElementById("nombre")
    comentario = document.getElementById("comentario")
    err = document.getElementById("err")
    if (!validarComentario(nombre.value, comentario.value)){
        err.innerText = "El comentario ingresado no es correcto. Por favor revise que el nombre y el comentario cumplan los requisitos."
        err.hidden = false
        return
    }
    err.hidden = true
    const avisoid = document.getElementById("aviso_id").innerText
    try{
        const resp = await fetch(
            `${window.origin}/comentarios/${avisoid}`,
            {
                method: "POST",
                body: JSON.stringify({"nombre": nombre.value, "comentario": comentario.value}),
                cache: "no-cache",
                headers: {
                    "Content-Type": "application/json",
                },
            }
        )
        if (!resp.ok){
            throw new Error(`Error llamando al endpoint: Status ${resp.status}`)
        }
        const data = await resp.json()
        if (data.error) {
            throw new Error(`Error de respuesta del endpoint: ${data.error}`)
        }

        if (data.msg){
            location.reload()
            return
        }
    } catch(error){
        console.error(error)
        err = document.getElementById("err")
        err.innerText = error
        err.hidden = !err.hidden
    }
}

document.addEventListener("DOMContentLoaded", async () =>{
    const cajaComentarios = document.getElementById("caja-comentarios")
    const err = document.getElementById("err-com")
    const avisoid = document.getElementById("aviso_id").innerText
    try {
        const resp = await fetch(`${window.origin}/comentarios/${avisoid}`, {
            method: "GET",
            cache: "no-cache",
        })
        if (!resp.ok){
            throw new Error(`Error cargando comentarios: Status ${resp.status}`)
        }
        const data = await resp.json()
        if (data.error) {
            throw new Error(`Error de respuesta del endpoint: ${data.error}`)
        }
        data.comentarios.forEach(comentario => {
            const div = document.createElement("div")
            div.className = "comentario"
            const nombre = document.createElement("h3")
            nombre.className = "nombre-comentario"
            nombre.innerText = comentario.nombre
            const fecha = document.createElement("h3")
            fecha.className = "fecha-comentario"
            fecha.innerText = comentario.fecha
            const texto = document.createElement("p")
            texto.innerText = comentario.texto
            div.appendChild(nombre)
            div.appendChild(fecha)
            div.appendChild(texto)
            cajaComentarios.appendChild(div)
        });
    } catch (error){
        console.error(error)
        err.innerText = error
        err.hidden = false
    }
})