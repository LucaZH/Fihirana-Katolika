import { ReactNode, useEffect, useState } from "react";

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
    <div>
      <h1>Liste des Fihirana</h1>
      <ul>
        {fihirana.map((boky, index) => (
          <li key={index}>{Object.values(boky)[0] as ReactNode}</li>
        ))}
      </ul>
    </div>
  );
}
export default ListFihirana;
