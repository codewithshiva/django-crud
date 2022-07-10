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
<form action='/add/' method='post'>
  <input
     type="text"
     name="Title"
     required="required"
     placeholder="Enter Movie Title"
  />
  <input
     type="date"
     name="ReleaseDate"
     required="required"
     placeholder="Enter Release Date"
     />
     <input
     type="text"
     name="Genre"
     required="required"
     placeholder="Enter Genre"
     />
      <input
     type="number"
     name="Price"
     required="required"
     placeholder="Enter Price"
     />
      <input
     type="number"
     name="Ratings"
     required="required"
     placeholder="Enter Ratings"
     />
     <button type="submit">Add</button>
</form>
    </div>
  );
}

export default App;
