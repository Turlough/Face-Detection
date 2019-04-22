import cv2
import numpy as np
import sys
import mjpg

# https://github.com/opencv/opencv/tree/master/data/haarcascades
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
URL = 'http://172.16.92.210:8081'
stream = mjpg.Mjpg()


def process_image(jpg):

	img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
	image_np = np.array(img)

	gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

	faces = cascade.detectMultiScale(gray, 1.3, 5)
	for rect in faces:
		(x, y, w, h) = rect
		image_np = cv2.rectangle(image_np, (x, y), (x + w, y + h), (0, 255, 0), 2)


	cv2.imshow("image", image_np)
	key = cv2.waitKey(1)
	if key == ord('q'):
		stream.stop()
		cv2.destroyAllWindows()


if __name__ == '__main__':
	if len(sys.argv) > 0:
		URL = sys.argv[1]

	stream.get_frames(URL, process_image, True)