import { useState, useEffect } from "react";
//import { baseDatos } from "../base_datos";

export default function Activos() {
  const [datos, setDatos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/activos"); // una funcion del navegador que nos permite conectarnos a Flask
    console.dir(fetch);
  }, []);

  return (
    <table className="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Nombre del activo</th>
          <th scope="col">Ubicacion</th>
          <th scope="col">Estado</th>
        </tr>
      </thead>

      <tbody>
        {datos.map((activo) => (
          <tr key={activo.id}>
            <td>{activo.id}</td>
            <td>{activo.nombreActivo}</td>
            <td>{activo.ubicacion}</td>
            <td>{activo.estado}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
