import cv2
import glob

type_jpeg = "jpeg"
type_jpg = "jpg"
type_png = "png"

for filename in glob.glob('./images/*.' + type_jpg):
    img_o = cv2.imread(filename)
    img_g = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    size = img_o.shape[1]
    size_2 = int(size / 3)

    roi = img_o
    roi_90 = cv2.rotate(roi, cv2.ROTATE_90_CLOCKWISE)
    roi_180 = cv2.rotate(roi, cv2.ROTATE_180)
    roi_270 = cv2.rotate(roi, cv2.ROTATE_90_COUNTERCLOCKWISE)

    roi[size_2:size, size_2*2:size] = roi_90[size_2:size, size_2*2:size]
    roi[size_2:size, 0:size_2*2] = roi_180[size_2:size, 0:size_2*2]
    roi[0:size_2*2, 0:size_2] = roi_270[0:size_2*2, 0:size_2]

    if filename.find(type_jpeg):
        cv2.imwrite(filename.replace('./images', './augmentationImages').replace(type_jpeg, type_jpg), roi)
    elif filename.find(type_png):
        cv2.imwrite(filename.replace('./images', './augmentationImages').replace(type_png, type_jpg), roi)
    else:
        cv2.imwrite(filename.replace('./images', './augmentationImages'), roi)