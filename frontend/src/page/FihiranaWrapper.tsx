import { FC } from "react";
import { useParams } from "react-router-dom";
import Fihirana from "../components/Fihirana";

const FihiranaWrapper: FC = () => {
  const { fihirana } = useParams<{ fihirana: string }>();
  const safeFihirana = decodeURIComponent(fihirana ?? "");

  return <Fihirana fihirana={safeFihirana} />;
};

export default FihiranaWrapper;
