import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import pickle

style.use('ggplot')

images = []
blue = np.array([])
green = np.array([])
red = np.array([])

for i in range(15):
    image = cv2.imread('ph/{}.jpg'.format(i))
    images.append(image)

for image in images:
    blue = np.append(blue, image[10, 10][0])
    green = np.append(green, image[10, 10][1])
    red = np.append(red, image[10, 10][2])

# r g b
ys = np.array([i for i in range(15)])
xs = np.vstack([red, green, blue]).T

xs_train, xs_test, ys_train, ys_test = train_test_split(xs, ys, test_size=0.1)

# first approach
# clf = LinearRegression(n_jobs=-1)

# tree works reallly well, but has discrete output
# clf = tree.DecisionTreeRegressor()

# well enough
# clf = RandomForestRegressor()

# pretty nice working algorithm
clf = GradientBoostingRegressor(n_estimators=300, learning_rate=0.01, max_depth=2)
clf.fit(xs, ys)

# saving train data
with open('v4gradient.pickle', 'wb') as f:
    pickle.dump(clf, f)

# load train data
# pickle_in = open('last_version.pickle', 'rb')
# clf = pickle.load(pickle_in)

# find bug in 6.jpg it shows 12ph instead, 10.jpg -> 12.2ph, solved it (it was test data)
# load test image, count all of the pixels color and make mean
test_image = cv2.imread('ph/test1.png')

height = np.size(test_image, 0)
width = np.size(test_image, 1)
r, g, b = 0, 0, 0
for i in range(height):
    for j in range(width):
        b += test_image[i][j][0]
        g += test_image[i][j][1]
        r += test_image[i][j][2]

r_mean, g_mean, b_mean = r / (width * height), g / (width * height), b / (width * height)
print('r = {r_mean}, g = {g_mean}, b = {b_mean}'.format(**locals()))

test = np.vstack([r_mean, g_mean, b_mean]).T
ph_predict = clf.predict(test)
print("PH predict {}".format(ph_predict))

plt.scatter(blue, ys, c='b')
plt.scatter(green, ys, c='g')
plt.scatter(red, ys, c='r')
plt.plot(xs, ys)
plt.xlabel('RGB color')
plt.ylabel('PH')
# plt.show()

# check if images are correct
# while True:
#     i = 0
#     for i in range(len(images)):
#         cv2.imshow('{}.ph'.format(i), images[i])
#         i += 1
#     k = cv2.waitKey(0)
#     if k == 27:
#         exit(0)
