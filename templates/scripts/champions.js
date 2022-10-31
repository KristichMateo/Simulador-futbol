
let API = "http://localhost:5000";
let fila_datos = document.getElementById("fila_inicial");
let boton = document.getElementById("boton");
let borrar = document.getElementById("borrar");
let div_copas = document.getElementById("copas");

boton.addEventListener("click",async function devolver_tabla() {
  
  
  const respuesta = await fetch(`${API}/champions`,{
      method:["GET"],
    },)
  let data = await respuesta.json();
  console.log(data);
 
})
  
borrar.addEventListener("click",borrar_fun)
function borrar_fun() {
  window.location.reload()
}

