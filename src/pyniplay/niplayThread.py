import subprocess
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

class Niplay:
    def __init__(self, music_path: str, replay: Optional[int] = None,
                 volume: Optional[float] = None, fade_in: Optional[int] = None ,
                 max_workers = 1
                 ):

        self.exePath =  r"D:\MaxLife\Programming\2025Projects\CS-Rider\NiPlay\src\NiPlay\bin\Debug\net9.0\NiPlay.exe"
        self._music_path = music_path
        self._args= self.arg_caculate(volume ,fade_in ,replay  )
        self.PID = None
        self._process = None
        self._startInfo = None
        self.executor = ThreadPoolExecutor(max_workers=max_workers)


    def arg_caculate(self, volume, fade_in, replay):
        total_args = [self.exePath , self._music_path]
        if volume is not None: total_args += [f"volume:{volume}"]
        if fade_in is not None: total_args += [f"fadein:{fade_in}"]
        if replay is not None: total_args += [f"replay:{replay}"]
        return total_args

    def _popen_warper(self):
        self._process = subprocess.Popen(self._args)
        self.PID = self._process.pid

    def start(self):
        """
        you need this to play the music ,
        :return:
        """
        if self._startInfo is None: #
            self._startInfo = self.executor.submit(self._popen_warper)
        return self

    def kill(self , do_print = True ):
        if self._process and self._process.poll() is None:
            self._process.terminate()
            if do_print : print("NiPlay Thread being terminated.")
        else:
            if do_print : print("NiPlay Already Finished before")

    def restart(self):
        self.kill()
        self._startInfo = None
        self.start()

    def repeat_start(self):
        self._startInfo = None
        self.start()

