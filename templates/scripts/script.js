
let API = "http://localhost:5000";
let fila_datos = document.getElementById("fila_inicial");
let boton = document.getElementById("boton");
let borrar = document.getElementById("borrar");


boton.addEventListener("click",async function devolver_tabla() {
  
  
  
  const respuesta = await fetch(`${API}/devolver`,{
      method:["GET"],
    },)
  let data = await respuesta.json();
  console.log(data);
  data.nombre.reverse();
  data.puntos.reverse();

  for (let i = 0; i < 26; i++) {
    let celda = document.createElement("tr");
    let equipo_td = document.createElement("td");
    let puntos_td = document.createElement("td");
    celda.appendChild(equipo_td);
    celda.appendChild(puntos_td);
    fila_datos.insertAdjacentElement("afterend",celda)
    let nodo_equipo = document.createTextNode(data.nombre[i])
    let nodo_puntos = document.createTextNode(data.puntos[i])
    equipo_td.appendChild(nodo_equipo);
    puntos_td.appendChild(nodo_puntos);
    console.log(data.nombre[i]);
    console.log(data.puntos[i])
    }


  })
borrar.addEventListener("click",borrar_fun)
function borrar_fun() {
  window.location.reload()
}

