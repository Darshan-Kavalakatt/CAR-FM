from .shell import *

video_to_frames("/video/fish.mp4")
checklen()
fakes = remfakes()
delFiles(fakes)
checklen()