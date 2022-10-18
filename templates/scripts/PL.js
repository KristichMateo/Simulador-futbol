
let API = "http://localhost:5000";
let fila_datos = document.getElementById("fila_inicial");
let boton = document.getElementById("boton");
let borrar = document.getElementById("borrar");
let div_copas = document.getElementById("copas");

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
    equipo_td.setAttribute("class","equipo");
    puntos_td.setAttribute("class","equipo");
    celda.appendChild(equipo_td);
    celda.appendChild(puntos_td);
    fila_datos.insertAdjacentElement("afterend",celda)
    let nodo_equipo = document.createTextNode(data.nombre[i])
    let nodo_puntos = document.createTextNode(data.puntos[i])
    equipo_td.appendChild(nodo_equipo);
    puntos_td.appendChild(nodo_puntos);
    console.log(data.nombre[i]);
    console.log(data.puntos[i])
    if (i==25){
      celda.setAttribute("id","campeon")
    }
    else if (i==24||i==23||i==22||i==21||i==20){
      celda.setAttribute("class","libertadores")
    }
    else if (i==19||i==18||i==17||i==16||i==15||i==14){
      celda.setAttribute("class","sudamericana")
    }
    else if (i==1||i==0){
      celda.setAttribute("class","descensos")
    }
    else{
      celda.setAttribute("class","nada")
    }
    
      
    
  }
  
  
})
borrar.addEventListener("click",borrar_fun)
function borrar_fun() {
  window.location.reload()
}

