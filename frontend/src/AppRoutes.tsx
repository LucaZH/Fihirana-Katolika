import PHira from "./page/PHira";
import HiraWrapper from "./page/HiraWrapper";

import { BrowserRouter, Route, Routes } from "react-router-dom";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<PHira />} />
        <Route path="/:fihirana/:hira" element={<HiraWrapper />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
