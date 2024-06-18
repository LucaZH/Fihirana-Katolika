import { createBrowserRouter } from "react-router-dom";
import Hira from "./page/Hira";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Hira />,
  },
]);
