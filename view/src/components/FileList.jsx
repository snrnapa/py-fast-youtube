import useSWR from 'swr';
import { useState } from 'react';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import { ArrowClockwise, CloudArrowDown, Trash } from 'phosphor-react';

const FileList = () => {
  const api_host = import.meta.env.VITE_API_HOST;
  const [reloadCount, setReloadCount] = useState(0);

  //ファイルを削除する
  const deleteFile = (e) => {
    const targetFileName = e.target.value;
    const apiEndpoint = api_host + '/delete_file/' + targetFileName;

    fetch(apiEndpoint);

    setReloadCount(reloadCount + 1);
  };

  //全ファイルの削除
  const deleteAll = () => {
    const apiEndpoint = api_host + '/delete_all';

    fetch(apiEndpoint);

    setReloadCount(reloadCount + 1);
  };
  const selfRefresh = () => {
    setReloadCount(reloadCount + 1);
  };

  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error, isLoading } = useSWR(api_host + '/file_info', fetcher, {
    refreshInterval: 5000,
  });

  const downloadAll = async () => {
    const apiEndpoint = api_host + '/download_all';

    try {
      const response = await fetch(apiEndpoint);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'all_files.zip'; // ダウンロードするファイル名を指定
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (error) {
      console.error('Failed to download file:', error);
    }
  };

  return (
    <div className="space-y-6 bg-gray-500 rounded ">
      {isLoading ? (
        <p>loading...</p>
      ) : error ? (
        <p>failed to load</p>
      ) : (
        <div className="p-4  space-y-3 rounded overflow-hidden shadow-lg">
          <p className="text-3xl font-mono">File List</p>
          <div className="flex justify-center space-x-5 ">
            <CloudArrowDown size={50} onClick={downloadAll} />
            <IconButton onClick={selfRefresh}>
              <ArrowClockwise size={42} />
            </IconButton>
            <IconButton onClick={deleteAll}>
              <Trash size={42} />
            </IconButton>
          </div>
          {data.map((file) => {
            return (
              <div
                key={file.no}
                className="flex flex-col justify-center rounded border  shadow-lg bg-gray-700 "
              >
                <p className="text-xl text-white">{file.title}</p>
                <div>
                  <a
                    className="text-blue-200"
                    href={api_host + '/get_file/' + file.title}
                  >
                    download
                  </a>

                  <Button value={file.title} onClick={deleteFile}>
                    delete
                  </Button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default FileList;
