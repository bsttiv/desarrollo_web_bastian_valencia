let tableRows = document.getElementsByClassName("aviso")
for (const row of tableRows){
    row.onclick = () => {
        console.log("test")
        window.location = "avisos/"+row.id+".html"
    }
}