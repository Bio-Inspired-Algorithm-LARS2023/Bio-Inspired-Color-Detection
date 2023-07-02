import cv2
import numpy as np

def process_video(video_path, Cr_min, Cr_max, Cb_min, Cb_max):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second and frame count of the video
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create VideoWriter object to save the processed video
    output_path = "color_filtered.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))), isColor=True)

    # Process each frame of the video
    for i in range(frame_count):
        success, frame = video.read()

        if not success:
            print("Failed to read the video")
            break

        # Apply Gaussian blur to reduce noise
        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

        # Convert the blurred frame to YCrCb color space
        ycrcb_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2YCrCb)

        # Extract the Y, Cr, and Cb channels
        Y, Cr, Cb = cv2.split(ycrcb_frame)

        # Create a mask based on the specified Cr and Cb ranges
        mask = ((Cr >= Cr_min) & (Cr <= Cr_max) & (Cb >= Cb_min) & (Cb <= Cb_max))

        # Set the intensity to 255 for the pixels within the color range, and 0 for the rest
        filtered_frame = np.where(mask, 255, 0).astype(np.uint8)

        # Convert the filtered frame to color image
        filtered_frame_color = cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)

        # Save the filtered frame to the output video
        output_video.write(filtered_frame_color)

        # Save the image with the bounding boxes
        if i%100==0:
            image_title = 'cor'+str(int(i/100))+'.png'
            cv2.imwrite(image_title, filtered_frame_color)

        # Display progress
        print(f"Processed frame {i+1}/{frame_count}")

    # Release the video objects
    video.release()
    output_video.release()

    print(f"Processed video saved as: {output_path}")


# Provide the path to your video file
video_path = "your-video-path.mp4"

# Set the desired Cr and Cb ranges
Cr_min = 90
Cr_max = 120
Cb_min = 130
Cb_max = 255

# Run
process_video(video_path, Cr_min, Cr_max, Cb_min, Cb_max)
