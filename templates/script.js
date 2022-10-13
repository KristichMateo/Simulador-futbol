
let API = "http://localhost:5000";
async function devolver_tabla() {
    const respuesta = await fetch(`${API}/devolver`,{
        method:["GET"],
      },)
    let data = await respuesta.json();
    console.log(data)
}
devolver_tabla()

