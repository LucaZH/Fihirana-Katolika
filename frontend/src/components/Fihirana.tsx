import { FC, ReactNode, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import HiraSearch from "./HiraSearch";
import SearchBar from "./ui/SearchBar";
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
      <h1 className="text-5xl mx-16 mb-10 mt-10">
        {fihirana
          .replace(/_/g, " ")
          .split(" ")
          .map(
            (word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
          )
          .join(" ")}
      </h1>
      <div className="mx-16 w-full">
        <SearchBar />
      </div>

      <div className="flex flex-col gap-6 mx-16 mt-4">
        {hira.map((boky, index) => (
          <div key={index} className="bg-blue-100 p-4">
            <Link to={`/${fihirana}/${Object.values(boky)[1]}`}>
              <p>{Object.values(boky)[1] as ReactNode}</p>
              <span>Page: {Object.values(boky)[0] as ReactNode}</span>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};
export default Fihirana;
