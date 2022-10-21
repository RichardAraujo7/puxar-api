import "./App.css";
import Axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [data, setDate] = useState([]);
  useEffect(() => {
    Axios.get("https://jsonplaceholder.typicode.com/posts")
      .then((res) => {
        console.log("Puxando de :", res.data);
        setDate(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  const arr = data.map((data, index) => {
    return (
      <tr>
        <td>{data.id}</td>
        <td>{data.title}</td>
        <td>{data.body}</td>
      </tr>
    );
  });

  return (
    <div className="App">
      <h1>Puxando api com axios</h1>
      <table>
        <tr>
          <th>ID</th>
          <th>Título</th>
          <th>Corpo</th>
        </tr>
        {arr}
      </table>
    </div>
  );
}

export default App;
