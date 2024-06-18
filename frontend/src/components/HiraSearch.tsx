import { useState, useEffect } from "react";

interface Hira {
  title: string;
}

interface HiraData {
  [fihiranaName: string]: Hira[];
}

function HiraSearch() {
  const [searchTerm, setSearchTerm] = useState("");
  const [data, setData] = useState<HiraData | null>(null);

  useEffect(() => {
    if (searchTerm) {
      fetch(`/api/hira/?search=${encodeURIComponent(searchTerm)}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.json();
        })
        .then((json) => {
          console.log("lklj", json);
          if (json.status === "success") {
            setData(json.data);
          } else {
            console.error(json.message);
          }
        })
        .catch((e) => console.error("Failed to fetch hira:", e));
    }
  }, [searchTerm]);

  return (
    <div>
      <input
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search for hira"
      />
      {data && (
        <div>
          {Object.entries(data).map(([fihiranaName, hiraList]) => (
            <div key={fihiranaName}>
              <h2>{fihiranaName}</h2>
              {hiraList.map((hira, index) => (
                <p key={index}>{hira.title}</p>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default HiraSearch;
