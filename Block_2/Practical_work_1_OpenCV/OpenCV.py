import cv2

img_path=r'C:\Users\bytil\Desktop\Block_2\Practical_work_1_OpenCV\room.jpg'
img=cv2.imread(img_path)

if img is None:
    print("Error: Could not read image. Check file path and permissions.")
else:
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(7,7),0)

    cv2.imshow('Original Image',img)
    cv2.imshow('Gray and Blurred',blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    last=img_path.rfind("\\")
    folder=img_path[:last]
    output=folder+"\\room_processed.jpg"

    cv2.imwrite(output,blur)
    print(f"Saved to:{output}")

    saved=cv2.imread(output)
    if saved is not None:
        cv2.imshow('Saved Processed Image',saved)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Could not read saved image.")