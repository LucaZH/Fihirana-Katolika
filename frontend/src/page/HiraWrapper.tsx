import { FC } from "react";
import { useParams } from "react-router-dom";
import Hira from "../components/Hira";

const HiraWrapper: FC = () => {
  const { fihirana, hira } = useParams<{ fihirana: string; hira: string }>();
  const safeFihirana = decodeURIComponent(fihirana ?? "");
  const safeHira = decodeURIComponent(hira ?? "");

  return <Hira fihirana={safeFihirana} hira={safeHira} />;
};

export default HiraWrapper;
