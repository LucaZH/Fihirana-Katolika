import { ReactNode, useEffect, useState } from "react";
import { Link } from "react-router-dom";

const API_URL = "http://localhost:5000/api/fihirana/";

function ListFihirana() {
  const [fihirana, setFihirana] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => {
        setFihirana(data.data);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <main>
      <h1 className="text-5xl text-center m-10">Liste des Fihirana</h1>
      <div className="grid grid-cols-3 gap-10 text-center m-10">
        {fihirana.map((boky, index) => (
          <Link to={`/${Object.keys(boky)[0]}`}>
            <p className="bg-blue-200 p-10 rounded-md" key={index}>
              {Object.values(boky)[0] as ReactNode}
            </p>
          </Link>
        ))}
      </div>
    </main>
  );
}
export default ListFihirana;
