import './App.css';
import { useState, useEffect } from "react";
import axios from "axios";
function App() {
  const [movies, setmovies] = useState([])
  useEffect(()=>{
    async function getAllmovie(){
      try {
        const movies = await axios.get("http://127.0.0.1:8000")
        console.log(movies.data)
        setmovies(movies.data)
      } catch (error) {
        console.log(error)
      }
    }
    getAllmovie()
  }, [])
  return (
    <div className="App">
     <h1>Movies Table</h1>
     {
       movies.map((movie, i)=>{
         return (
          <table key={i}>
             <th>{movie.Title}</th>
             <th>{movie.ReleaseDate}</th>
             <th>{movie.Genre}</th>
             <th>{movie.Price}</th>
             <th>{movie.Ratings}</th>
             </table>
         )
       })
     }
     <h2>Add A Movie</h2>
<form>
  <input
     type="text"
     name="fullName"
     required="required"
     placeholder="Enteraname ..."
  />
  <input
     type="text"
     name="address"
     required="required"
     placeholder="Enter an addres ..."
     />
</form>
    </div>
  );
}

export default App;
