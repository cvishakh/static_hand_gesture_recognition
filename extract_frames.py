import cv2
import os

#List of video paths
video_paths = [
    "C:/Users/visha/Documents/ProjectThesis/Dataset/Video/v_sign_2.mp4"
]

#Directory to save frames
output_dir = "C:/Users/visha/Documents/ProjectThesis/Dataset/"

#Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

#Number of frames to extract (roughly 100 frames)
desired_frame_count = 100

#Process each video
for video_path in video_paths:
    #Get the video filename without extension for creating unique folder names
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    #Create a folder for each video's frames
    video_folder = os.path.join(output_dir, video_name)
    os.makedirs(video_folder, exist_ok=True)
    
    #Initialize video capture
    vidcap = cv2.VideoCapture(video_path)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = max(1, total_frames // desired_frame_count)  #Calculate frame interval

    success, image = vidcap.read()
    count = 0  #Frame counter
    saved_count = 0  #Counter for saved frames
    
    #Read and save frames at the calculated interval
    while success and saved_count < desired_frame_count:
        if count % interval == 0:  #Save every 'interval' frame
            frame_path = os.path.join(video_folder, f"{saved_count}.png")
            cv2.imwrite(frame_path, image)
            saved_count += 1  #Increment saved frame counter

        count += 1
        success, image = vidcap.read()  #Read the next frame
    
    print(f"Frames extracted for {video_name}, total frames saved: {saved_count}")

print("All frames extracted successfully.")
