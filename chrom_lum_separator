import cv2
import numpy as np

def process_video(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second and frame count of the video
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create VideoWriter objects to save the processed videos
    red_output_path = "crominance_red_output.mp4"
    blue_output_path = "crominance_blue_output.mp4"
    luminance_output_path = "luminance_output.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    # Create video writers for each output
    red_output_video = cv2.VideoWriter(red_output_path, fourcc, fps, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    blue_output_video = cv2.VideoWriter(blue_output_path, fourcc, fps, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    luminance_output_video = cv2.VideoWriter(luminance_output_path, fourcc, fps, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    # Process each frame of the video
    for i in range(frame_count):
        success, frame = video.read()

        if not success:
            print("There was an error reading the video")
            break

        # Apply Gaussian blur to reduce noise
        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

        # Convert the blurred frame to YCrCb color space
        ycrcb_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2YCrCb)

        # Extract the Y, Cr, and Cb channels
        Y, Cr, Cb = cv2.split(ycrcb_frame)

        # Set Cr and Cb components to zero for red output
        zeros = np.zeros_like(Cr)
        Cr_zeroed = cv2.merge([Cr, Cr, Cr])

        # Set Cr and Cb components to zero for blue output
        Cb_zeroed = cv2.merge([Cb, Cb, Cb])
        Y_zeroed = cv2.merge([Y, Y, Y])

        # Save the image with the bounding boxes
        if i%100==0:
            image_title = 'Original_'+str(int(i/100))+'.png'
            cv2.imwrite(image_title, frame)
            image_title = 'Cblue_'+str(int(i/100))+'.png'
            cv2.imwrite(image_title, Cb_zeroed)
            image_title = 'Cred_'+str(int(i/100))+'.png'
            cv2.imwrite(image_title, Cr_zeroed)
            image_title = 'Y_'+str(int(i/100))+'.png'
            cv2.imwrite(image_title, Y_zeroed)

        # Save the individual channels as videos
        red_output_video.write(Cr_zeroed)
        blue_output_video.write(Cb_zeroed)
        luminance_output_video.write(Y_zeroed)

        # Display progress
        print(f"Processed frame {i+1}/{frame_count}")

    # Release the video objects
    video.release()
    red_output_video.release()
    blue_output_video.release()
    luminance_output_video.release()

    print(f"Processed videos saved as: {red_output_path}, {blue_output_path}, {luminance_output_path}")


# Provide the path to your video file
video_path = "your-video-path.mp4"

process_video(video_path)
