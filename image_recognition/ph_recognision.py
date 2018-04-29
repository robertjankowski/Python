import cv2
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean

style.use('ggplot')

images = []
blue = np.array([])
green = np.array([])
red = np.array([])
blue = []


def best_fit_slope_intercept(xs, ys):
    tmp1 = mean(xs) * mean(ys) - mean(xs * ys)
    tmp2 = mean(xs) * mean(xs) - mean(xs * xs)
    m = tmp1 / tmp2
    b = mean(ys) - m * mean(xs)
    return m, b


for i in range(15):
    image = cv2.imread('ph/{}.jpg'.format(i))
    images.append(image)

for image in images:
    blue = np.append(blue, image[10, 10][0])
    green = np.append(green, image[10, 10][1])
    red = np.append(red, image[10, 10][2])

ys_blue = np.array([i for i in range(15)])
ys_green = ys_blue
ys_red = ys_blue

# predition only for blue, so blue is my xs
m_blue, b_blue = best_fit_slope_intercept(blue, ys_blue)
y_blue_predict = m_blue * blue + b_blue

# green
m_green, b_green = best_fit_slope_intercept(green, ys_green)
y_green_predict = m_green * green + b_green

# red
m_red, b_red = best_fit_slope_intercept(red, ys_red)
y_red_predict = m_red * red + b_red

# incorrect model, need to be changed
# load test image
test_image = cv2.imread('ph/test.png')
blue_test = test_image[10][10][0]
green_test = test_image[10][10][1]
red_test = test_image[10][10][2]

ph_blue = m_blue * blue_test + b_blue
ph_green = m_green * green_test + b_green
ph_red = m_red * red_test + b_red

ph = (ph_blue + ph_green + ph_red) / 3
print(ph)

plt.scatter(blue, ys_blue, c='b')
plt.plot(blue, y_blue_predict, 'black')
# plt.plot(red, y_red_predict, c='r')
# plt.plot(green, y_green_predict, c='g')
# plt.scatter(green, ys_green, c='g')
# plt.scatter(red, ys_green, c='r')
plt.scatter(blue_test, ph_blue, c='y')
plt.xlabel('RGB color')
plt.ylabel('PH')
plt.sh
# check if images are correct
# while True:
#     i = 0
#     for i in range(len(images)):
#         cv2.imshow('{}.ph'.format(i), images[i])
#         i += 1
#     k = cv2.waitKey(0)
#     if k == 27:
#         exit(0)
