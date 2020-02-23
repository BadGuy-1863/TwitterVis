#Work In Progress, build from here
import os


from skimage.measure import compare_ssim as ssim
import cv2

def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    s = ssim(imageA, imageB)
    return s


test_color = cv2.imread("#bernie2020.png")

# convert the images to grayscale
test = cv2.cvtColor(test_color, cv2.COLOR_BGR2GRAY)
t = test[250:500, 100:700]

rootdir = 'C:/Users/there/PycharmProjects/Misc/TwitterXSports/src/ims/'
dummy = []
files_list = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        files_list.append(subdir + '/'+ file)
        cmp = cv2.imread(subdir + '/' + file)
        print(subdir + '/' + file)
        comp = cv2.cvtColor(cmp, cv2.COLOR_BGR2GRAY)
        c = comp[0:250, 0:600]
        dummy.append(compare_images(t,c))

cv2.imshow('test',test_color)
cv2.waitKey(0)
display = cv2.imread(files_list[dummy.index(max(dummy))])
cv2.imshow('most_similar',display)
cv2.waitKey(0)

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