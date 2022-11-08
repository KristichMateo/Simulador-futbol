let como_funciona = document.getElementById("como_funciona");
let titulo = document.getElementById("titulo");
let ul_dinamico = document.getElementById("ul_dinamico");
let estadisticas = document.getElementById("estadisticas");
como_funciona.addEventListener("click",()=>{
    titulo.innerHTML = " "
    ul_dinamico.innerHTML = " "
    titulo.innerHTML = "¿Como funciona?"
    ul_dinamico.innerHTML = `<ul id="ul_dinamico">
    <h6>Cada equipo tiene:</h6>
    <li> Posiilidades de meter un gol un gol (del 1 al 100) </li>
    <li> Posibilidades de defender (del 1 al 25) </li>
    <li> Cantidad de chances por partido (4 o 5) </li>
    <li> Por medio de un algoritmo se simulan los goles</li>
    <li> Esta variables fueron decididas por el desarrollador</li>

</ul>`
})
estadisticas.addEventListener("click",()=>{
    titulo.innerHTML = " "
    ul_dinamico.innerHTML = " "
    titulo.innerHTML = "¿En que se baso?"
    ul_dinamico.innerHTML = `<ul id="ul_dinamico">
    <h6>Basadas en el estado de los equipos en el momento que se programo</h6>
    <li> LPF:2021 </li>
    <li> Premier League:2021/2022 </li>
    <li> Bundes Liga:2022 (temporada actual)</li>
    <li> Champions League:2022 (temporada actual)</li>
    <li> Mundial:2022 (temporada actual)</li>


</ul>`
})