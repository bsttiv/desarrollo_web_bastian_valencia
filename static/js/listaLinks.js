let tableRows = document.getElementsByClassName("aviso")
for (const row of tableRows){
    row.onclick = () => {
        window.location = "/listado/"+row.id
    }
}

let pageSelector = document.getElementById("select-page")
if (pageSelector){
    pageSelector.onchange = () => {
        window.location = "/listado/?page="+pageSelector.value
    }
}