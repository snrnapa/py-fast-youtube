import './App.css';
import Downloader from './components/Downloader';
import FileList from './components/FileList';

function App() {
  return (
    <div className="space-y-10  ">
      <p className="text-3xl font-mono">YDL Application</p>

      <FileList />

      <Downloader />
    </div>
  );
}

export default App;
