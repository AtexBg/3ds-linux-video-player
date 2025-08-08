import cv2
import os

def crop():
    in_dir = 'frames'
    out_dir = 'cropped_frames'
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    for file in os.listdir(in_dir):
        if file.endswith('.png'):
            image_path = os.path.join(in_dir, file)
            image = cv2.imread(image_path)
            
            cropped_image = cv2.resize(image, (400, 240))
            
            output_image_path = os.path.join(out_dir, file)
            cv2.imwrite(output_image_path, cropped_image)
            print(f"Cropped to 400*240: {file}")
    
    print("Done :3")

crop()
