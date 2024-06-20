import { FC, useEffect, useState } from "react";

const API_URL = "http://localhost:5000/api/";

const Hira: FC<{ fihirana: string; hira: string }> = ({ fihirana, hira }) => {
  const [Nhira, setNHira] = useState<
    { title: string; page: string; content: string[] } | undefined
  >();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(API_URL + fihirana + "/" + "/hira?title=" + hira)
      .then((response) => response.json())
      .then((data) => {
        setNHira(data.data);
        setLoading(false);
      });
  }, [hira, fihirana]);
  const Newfihirana = fihirana
    .replace(/_/g, " ")
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(" ");

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <main className="p-16">
      <h1 className="text-4xl">{Newfihirana}</h1>
      <div className="text-justify">
        <h2 className="text-3xl">{Nhira?.title}</h2>
        <p>
          {Newfihirana}: {Nhira?.page}
        </p>
        <div className="space-y-4 py-6">
          {Nhira?.content.map((item, index) => (
            <p key={index}>{item}</p>
          ))}
        </div>
      </div>
    </main>
  );
};
export default Hira;
