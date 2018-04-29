import numpy as np
import argparse
import cv2

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    # specify colors, in different order BGR
    # blue, green, yellow, grey
    boundaries = [
        ([86, 31, 4], [220, 88, 50]),
        ([17, 15, 100], [50, 56, 200]),
        ([25, 146, 190], [62, 174, 250]),
        ([103, 86, 65], [145, 133, 128])
    ]

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(0)
