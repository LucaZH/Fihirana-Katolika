import HiraWrapper from "./page/HiraWrapper";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ListFihirana from "./components/ListFihirana";
import FihiranaWrapper from "./page/FihiranaWrapper";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ListFihirana />} />
        <Route path="/:fihirana/:hira" element={<HiraWrapper />} />
        <Route path="/:fihirana" element={<FihiranaWrapper />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
