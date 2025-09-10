from niplayThread import Niplay

task = Niplay(
    music_path=r"C:\Users\Max_Laptop\Music\【#8bit】＂ラビットホール＂ - DECO＊27【#チップチューン アレンジ ｜ #ラビットホール】 [mUkNS6W5Z54].mp3",
    volume=1.0,
    fade_in=2000,
    replay=3
).start()


from time import sleep
sleep(2)
print()

task.kill()
