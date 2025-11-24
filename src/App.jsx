import { baseDatos } from "./base_datos"

export default function App() {
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
      {
        baseDatos.map(activo => (
          <tr key={activo.id}>
            <td>{activo.id}</td>
            <td>{activo.nombreActivo}</td>
            <td>{activo.ubicacion}</td>
            <td>{activo.estado}</td>
          </tr>
        ))
      }
    </tbody>
  </table>
 )
}