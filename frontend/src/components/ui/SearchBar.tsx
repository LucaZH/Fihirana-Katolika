import { FC } from "react";

const SearchBar: FC = () => {
  return (
    <input
      type="search"
      placeholder="Search"
      className="p-2 border-b-2 w-full"
    />
  );
};
export default SearchBar;
