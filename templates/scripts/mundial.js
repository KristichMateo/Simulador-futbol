
let API = "http://localhost:5000";
let fila_datos = document.getElementById("fila_inicial");
let boton = document.getElementById("boton");
let borrar = document.getElementById("borrar");
let div_copas = document.getElementById("copas");
let tabla_A = document.getElementById("tabla_A");
let tabla_B = document.getElementById("tabla_B");
let tabla_C = document.getElementById("tabla_C");
let tabla_D = document.getElementById("tabla_D");
let tabla_E = document.getElementById("tabla_E");
let tabla_F = document.getElementById("tabla_F");
let tabla_G = document.getElementById("tabla_G");
let tabla_H = document.getElementById("tabla_H");
let tabla_octavos = document.getElementById("tabla_octavos");
let tabla_Cuartos = document.getElementById("tabla_Cuartos");
let tabla_semis = document.getElementById("tabla_semis");
let tabla_final = document.getElementById("tabla_final");
let padre_div = document.getElementById("padre_total")
boton.addEventListener("click",async function devolver_tabla() {
  
  padre_div.setAttribute("id","padre_cambio")
  const respuesta = await fetch(`${API}/mundial`,{
      method:["GET"],
    },)
  let data = await respuesta.json();
  console.log(data);
  let a = 0;
    for (let i = 0; i < 4; i++) {
        let tr_A = document.createElement("tr");
        let th_nombre =document.createElement("th");
        let th_puntos = document.createElement("th");
        th_nombre.innerHTML = data.grupos.A[a]
        th_puntos.innerHTML = data.grupos.A[a+1]
        tr_A.appendChild(th_nombre);
        tr_A.appendChild(th_puntos);
        tabla_A.appendChild(tr_A);
        a = a+2
        if (i == 0 || i == 1){
          th_nombre.setAttribute("class","clasificados")
          th_puntos.setAttribute("class","clasificados")
        }
        if(i == 2){
          th_nombre.setAttribute("class","europa")
          th_puntos.setAttribute("class","europa")
        }
        if(i == 3){
          th_nombre.setAttribute("class","eliminado")
          th_puntos.setAttribute("class","eliminado")
        }
    }
   let b = 0;
    for (let i = 0; i < 4; i++) {
        let tr_B = document.createElement("tr");
        let th_nombre =document.createElement("th");
        let th_puntos = document.createElement("th");
        th_nombre.innerHTML = data.grupos.B[b]
        th_puntos.innerHTML = data.grupos.B[b+1]
        tr_B.appendChild(th_nombre);
        tr_B.appendChild(th_puntos);
        tabla_B.appendChild(tr_B);
        b = b+2
        if (i == 0 || i == 1){
          th_nombre.setAttribute("class","clasificados");
          th_puntos.setAttribute("class","clasificados")
        }
        if(i == 2){
          th_nombre.setAttribute("class","europa");
          th_puntos.setAttribute("class","europa")
        }
        if(i == 3){
          th_nombre.setAttribute("class","eliminado");
          th_puntos.setAttribute("class","eliminado")
        }
     }
     let c = 0;
    for (let i = 0; i < 4; i++) {
        let tr_C = document.createElement("tr");
        let th_nombre =document.createElement("th");
        let th_puntos = document.createElement("th");
        th_nombre.innerHTML = data.grupos.C[c]
        th_puntos.innerHTML = data.grupos.C[c+1]
        tr_C.appendChild(th_nombre);
        tr_C.appendChild(th_puntos);
        tabla_C.appendChild(tr_C);
        c = c+2
        if (i == 0 || i == 1){
          th_nombre.setAttribute("class","clasificados");
          th_puntos.setAttribute("class","clasificados")
        }
        if(i == 2){
          th_nombre.setAttribute("class","europa");
          th_puntos.setAttribute("class","europa")
        }
        if(i == 3){
          th_nombre.setAttribute("class","eliminado");
          th_puntos.setAttribute("class","eliminado")
        }
     }
     let d = 0;
     for (let i = 0; i < 4; i++) {
         let tr_D = document.createElement("tr");
         let th_nombre =document.createElement("th");
         let th_puntos = document.createElement("th");
         th_nombre.innerHTML = data.grupos.D[d]
         th_puntos.innerHTML = data.grupos.D[d+1]
         tr_D.appendChild(th_nombre);
         tr_D.appendChild(th_puntos);
         tabla_D.appendChild(tr_D);
         d = d+2
         if (i == 0 || i == 1){
          th_nombre.setAttribute("class","clasificados");
          th_puntos.setAttribute("class","clasificados")
        }
        if(i == 2){
          th_nombre.setAttribute("class","europa");
          th_puntos.setAttribute("class","europa")
        }
        if(i == 3){
          th_nombre.setAttribute("class","eliminado");
          th_puntos.setAttribute("class","eliminado")
        }
      }
      let e = 0;
     for (let i = 0; i < 4; i++) {
         let tr_E = document.createElement("tr");
         let th_nombre =document.createElement("th");
         let th_puntos = document.createElement("th");
         th_nombre.innerHTML = data.grupos.E[e];
         th_puntos.innerHTML = data.grupos.E[e+1];
         tr_E.appendChild(th_nombre);
         tr_E.appendChild(th_puntos);
         tabla_E.appendChild(tr_E);
         e = e+2;
         if (i == 0 || i == 1){
          th_nombre.setAttribute("class","clasificados");
          th_puntos.setAttribute("class","clasificados")
        }
        if(i == 2){
          th_nombre.setAttribute("class","europa");
          th_puntos.setAttribute("class","europa")
        }
        if(i == 3){
          th_nombre.setAttribute("class","eliminado");
          th_puntos.setAttribute("class","eliminado")
        }
      }
      let f = 0;
     for (let i = 0; i < 4; i++) {
         let tr_F = document.createElement("tr");
         let th_nombre =document.createElement("th");
         let th_puntos = document.createElement("th");
         th_nombre.innerHTML = data.grupos.F[f];
         th_puntos.innerHTML = data.grupos.F[f+1];
         tr_F.appendChild(th_nombre);
         tr_F.appendChild(th_puntos);
         tabla_F.appendChild(tr_F);
         f = f+2;
         if (i == 0 || i == 1){
          th_nombre.setAttribute("class","clasificados");
          th_puntos.setAttribute("class","clasificados")
        }
        if(i == 2){
          th_nombre.setAttribute("class","europa");
          th_puntos.setAttribute("class","europa")
        }
        if(i == 3){
          th_nombre.setAttribute("class","eliminado");
          th_puntos.setAttribute("class","eliminado")
        }
      }
      let g = 0;
      for (let i = 0; i < 4; i++) {
          let tr_G = document.createElement("tr");
          let th_nombre =document.createElement("th");
          let th_puntos = document.createElement("th");
          th_nombre.innerHTML = data.grupos.G[g];
          th_puntos.innerHTML = data.grupos.G[g+1];
          tr_G.appendChild(th_nombre);
          tr_G.appendChild(th_puntos);
          tabla_G.appendChild(tr_G);
          g = g+2;
          if (i == 0 || i == 1){
            th_nombre.setAttribute("class","clasificados");
            th_puntos.setAttribute("class","clasificados")
          }
          if(i == 2){
            th_nombre.setAttribute("class","europa");
            th_puntos.setAttribute("class","europa")
          }
          if(i == 3){
            th_nombre.setAttribute("class","eliminado");
            th_puntos.setAttribute("class","eliminado")
          }
       }
       let h = 0;
       for (let i = 0; i < 4; i++) {
           let tr_H = document.createElement("tr");
           let th_nombre =document.createElement("th");
           let th_puntos = document.createElement("th");
           th_nombre.innerHTML = data.grupos.H[h];
           th_puntos.innerHTML = data.grupos.H[h+1];
           tr_H.appendChild(th_nombre);
           tr_H.appendChild(th_puntos);
           tabla_H.appendChild(tr_H);
           h = h+2;
           if (i == 0 || i == 1){
            th_nombre.setAttribute("class","clasificados");
            th_puntos.setAttribute("class","clasificados")
          }
          if(i == 2){
            th_nombre.setAttribute("class","europa");
            th_puntos.setAttribute("class","europa")
          }
          if(i == 3){
            th_nombre.setAttribute("class","eliminado");
            th_puntos.setAttribute("class","eliminado")
          }
        }
    let cruces_cotavos = Object.values(data.octavos)
    for (let i = 0; i < cruces_cotavos.length; i++) {
      if (cruces_cotavos[i].length == 5){
        let th_O = document.createElement("th");
        let tr_0 = document.createElement("tr")
        th_O.innerHTML = cruces_cotavos[i][0] +" "+ cruces_cotavos[i][1] +" : "+ cruces_cotavos[i][3] +" "+ cruces_cotavos[i][4]
        tr_0.appendChild(th_O)
        tabla_octavos.appendChild(tr_0)
      }
      if (cruces_cotavos[i].length == 7){
        let th_O = document.createElement("th");
        let tr_0 = document.createElement("tr")
        th_O.innerHTML = cruces_cotavos[i][0] +" "+ cruces_cotavos[i][1] + "("+cruces_cotavos[i][5]+") : ("+cruces_cotavos[i][6]+")" + cruces_cotavos[i][3] +" "+ cruces_cotavos[i][4]
        tr_0.appendChild(th_O)
        tabla_octavos.appendChild(tr_0)
      }
    }
    let cruces_cuartos = Object.values(data.cuartos)
    for (let i = 0; i < cruces_cuartos.length; i++) {
      if (cruces_cuartos[i].length == 5){
        let th_C = document.createElement("th");
        let tr_C = document.createElement("tr")
        th_C.innerHTML = cruces_cuartos[i][0] +" "+ cruces_cuartos[i][1] +" : "+ cruces_cuartos[i][3] +" "+ cruces_cuartos[i][4];
        tr_C.appendChild(th_C)
        tabla_Cuartos.appendChild(tr_C)
      }
      if (cruces_cuartos[i].length == 7){
        let th_C = document.createElement("th");
        let tr_C = document.createElement("tr")
        th_C.innerHTML = cruces_cuartos[i][0] +" "+ cruces_cuartos[i][1] + "("+cruces_cuartos[i][5]+") : ("+cruces_cuartos[i][6]+")" + cruces_cuartos[i][3] +" "+ cruces_cuartos[i][4]
        tr_C.appendChild(th_C)
        tabla_Cuartos.appendChild(tr_C)
      }
    }
    let cruces_semis = Object.values(data.semis)
    for (let i = 0; i < cruces_semis.length; i++) {
      if (cruces_semis[i].length == 5){
        let th_S = document.createElement("th");
        let tr_S = document.createElement("tr")
        th_S.innerHTML = cruces_semis[i][0] +" "+ cruces_semis[i][1] +" : "+ cruces_semis[i][3] +" "+ cruces_semis[i][4];
        tr_S.appendChild(th_S)
        tabla_semis.appendChild(tr_S)
      }
      if (cruces_cuartos[i].length == 7){
        let th_S = document.createElement("th");
        let tr_S = document.createElement("tr")
        th_S.innerHTML = cruces_semis[i][0] +" "+ cruces_semis[i][1] + "("+cruces_semis[i][5]+") : ("+cruces_semis[i][6]+")" + cruces_semis[i][3] +" "+ cruces_semis[i][4]
        tr_S.appendChild(th_S)
        tabla_Cuartos.appendChild(tr_S)
      }
    }
    let final = Object.values(data.final)
    for (let i = 0; i < final.length; i++) {
      if (final[i].length == 5){
        let th_F = document.createElement("th");
        let tr_F = document.createElement("tr")
        th_F.innerHTML = final[i][0] +" "+ final[i][1] +" : "+ final[i][3] +" "+ final[i][4];
        tr_F.appendChild(th_F)
        tabla_final.appendChild(tr_F)
      }
      if (final[i].length == 7){
        let th_F = document.createElement("th");
        let tr_F = document.createElement("tr")
        th_F.innerHTML = final[i][0] +" "+ final[i][1] + "("+final[i][5]+") : ("+final[i][6]+")" + final[i][3] +" "+ final[i][4]
        tr_F.appendChild(th_F)
        tabla_final.appendChild(tr_F)
      }
    }
    let tr_campeon = document.createElement("tr");
    tr_campeon.innerHTML = data.final.campeon
    tr_campeon.setAttribute("class","campeon_champion")
    tabla_final.appendChild(tr_campeon)
  
  }
    )

borrar.addEventListener("click",borrar_fun)
function borrar_fun() {
  window.location.reload()
}

