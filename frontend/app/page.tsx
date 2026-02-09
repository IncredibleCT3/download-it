import Image from "next/image";
import searchbar from "./Components/SearchBar";
import SearchBar from "./Components/SearchBar";
import Title from "./Components/Title";
import Table from "./Components/Table";
import DownloadBtn from "./Components/DownloadBtn";

export default function Home() {
  return (
    <div className="flex justify-center items-center align-top min-h-screen flex-col">
      <Title />
      <SearchBar />
      <Table />
    </div>
  );
}
