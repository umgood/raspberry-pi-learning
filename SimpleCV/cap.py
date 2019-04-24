import SimpleCV as scv
import time

cam=scv.Camera()
display=scv.Display(resolution=(800,600))
while display.isNotDone():

	img=cam.getImage()
	peaks=img.huePeaks()
	peak_one=peaks[0][0]
	hue=img.hueDistance(peak_one)
	hue.show()
	time.sleep(5)
