import { FC, ReactNode, useEffect, useState } from "react";
import { Link } from "react-router-dom";
const API_URL = "http://localhost:5000/api/";
const Fihirana: FC<{ fihirana: string }> = ({ fihirana }) => {
  const [hira, setHira] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(API_URL + fihirana)
      .then((response) => response.json())
      .then((data) => {
        setHira(data.data);
        setLoading(false);
      });
  }, [fihirana]);

  if (loading) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h1>{fihirana}</h1>
      <ul>
        {hira.map((boky, index) => (
          <li key={index}>
            <Link to={`/${fihirana}/${Object.values(boky)[1]}`}>
              <p>{Object.values(boky)[1] as ReactNode}</p>
              <span>{Object.values(boky)[0] as ReactNode}</span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};
export default Fihirana;
