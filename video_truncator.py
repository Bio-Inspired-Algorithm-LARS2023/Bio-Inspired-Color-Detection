import cv2

def truncate_video(video_path, start_time, end_time, output_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second and frame count of the video
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the start and end frame indices based on the specified times
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    # Validate the frame indices
    if start_frame < 0:
        start_frame = 0
    if end_frame > frame_count - 1:
        end_frame = frame_count - 1

    # Set the current frame position to the start frame
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Create VideoWriter object to save the truncated video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    # Read and write frames until the end frame is reached
    for i in range(start_frame, end_frame + 1):
        success, frame = video.read()

        if not success:
            print("Failed to read the video")
            break

        # Write the frame to the output video
        output_video.write(frame)

        # Display progress
        print(f"Processed frame {i+1}/{end_frame+1}")

    # Release the video objects
    video.release()
    output_video.release()

    print(f"Truncated video saved as: {output_path}")


# Provide the path to your input video file
video_path = "your-video-path.mp4"

# Specify the start and end times for truncation in seconds
start_time = 16
end_time = 46

# Provide the output path for the truncated video
output_path = "your-output-path.mp4"

truncate_video(video_path, start_time, end_time, output_path)
