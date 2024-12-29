import { useRef, useState } from 'react';
import Button from '@mui/material/Button';
import Swal from 'sweetalert2';
import { FileVideo, MusicNote } from 'phosphor-react';

const Downloader = () => {
  const api_host = import.meta.env.VITE_API_HOST;

  const urlRef = useRef();
  const [movieFlg, setMovieFlg] = useState(false);
  const [musicFlg, setMusicFlg] = useState(true);

  const downloadUrl = async () => {
    // const url = urlRef.current.value.slice(-11);
    const url = urlRef.current.value;

    // POSTメソッドのBodyのJsonを出力して確認
    console.log(
      JSON.stringify({ url: url, movie_flg: movieFlg, music_flg: musicFlg }),
    );
    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url: url,
        movie_flg: movieFlg,
        music_flg: musicFlg,
      }),
    };

    const apiEndpoint = api_host + '/yt_donwload';
    console.log(apiEndpoint);
    fetch(apiEndpoint, options);

    await Swal.fire({
      title: 'ダウンロードを開始します🥺🥺🥺',
      text: '',
      icon: 'info',
      confirmButtonText: 'OK',
      timer: 7000,
    });
    urlRef.current.value = '';
  };

  const handleMovieFlg = () => {
    setMovieFlg(!movieFlg);
  };
  const handleMusicFlg = () => {
    setMusicFlg(!musicFlg);
  };

  return (
    <div>
      <div className="p-4 space-y-3 rounded border  shadow-lg bg-gray-500">
        <p className="text-3xl font-mono">Target Youtube Url</p>
        <div className="space-x-5">
          <input
            className=" w-7/12 p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            type="text"
            ref={urlRef}
          ></input>
          <Button variant="contained" onClick={downloadUrl}>
            DownLoad
          </Button>
        </div>
        <div className=" flex justify-center  space-x-5 ">
          <label className="space-x-3 flex justify-center">
            <FileVideo size={42} />
            <input
              className="w-7 h-7"
              type="checkbox"
              checked={movieFlg}
              onChange={handleMovieFlg}
            />
          </label>
          <label className="space-x-3 flex justify-center">
            <MusicNote size={42} />
            <input
              className="w-7 h-7"
              type="checkbox"
              checked={musicFlg}
              onChange={handleMusicFlg}
            />
          </label>
        </div>
      </div>
    </div>
  );
};

export default Downloader;
