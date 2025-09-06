import cv2
import os

def extract_frames(video, fps=24):
    cap = cv2.VideoCapture(video)
    
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return
    
    output_folder = 'frames'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_filename = f"{output_folder}/{frame_count + 1}.png"
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
        
        cv2.waitKey(int(1000 / fps))  
    
    cap.release()
    print(f" {frame_count} frames extracted to ./frames.")

video = 'video.mp4'
extract_frames(video, fps=24) #Replaced "video" with "video_path" before fix, i may just be dumb
