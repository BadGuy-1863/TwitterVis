#Work In Progress, build from here
import os
from skimage.measure import compare_ssim as ssim
import cv2

def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    s = ssim(imageA, imageB)
    return s


test = cv2.imread("#bernie2020.png")

# convert the images to grayscale
test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

rootdir = 'C:/Users/there/PycharmProjects/Misc/TwitterXSports/src/ims'
dummy = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        comp = cv2.imread(file)
        comp = cv2.cvtColor(file, cv2.Color_BGR2Gray)
        dummy.append(compare_images(test,comp))
print(dummy)

# loop over the images
'''for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
compare_images(bernie, bernie, "Bernie vs. Bernie")
compare_images(bernie, trump, "Bernie vs. Trump")'''