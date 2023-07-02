# Bio-Inspired Color Detection Algorithm

This repository contains three Python scripts associated to our bio-inspired color detection algorithm.

## Overview

1. **Video Processing (`video_processing.py`):** This script contains our algorithm implementation.

2. **Chrominance and Luminance Separation (`chrom_lum_separator.py`):** This script takes a video file as input and separates it into its red and blue chrominance and luminance components. The separated components are saved as individual video files.

3. **Video Truncation (`video_truncator.py`):** This script takes a video file, start and end times as inputs and truncates the video to this specified range. The truncated video is saved as a new video file.

## File paths - Corrections

Before running the scripts, you need to specify the paths to your video files and where you want the output images to be saved. 

Replace the following paths with the locations of your own video files:

- For video_processing.py:
  - Line 13: `output_path = "color_filtered.mp4"`
  - Line 62: `video_path = "your-video-path.mp4"`

- For chrom_lum_separator.py:
  - Line 13: `red_output_path = "crominance_red_output.mp4"`
  - Line 14: `blue_output_path = "crominance_blue_output.mp4"`
  - Line 15: `luminance_output_path = "luminance_output.mp4"`
  - Line 78: `video_path = "your-video-path.mp4"`

- For video_truncator.py:
  - Line 50: `video_path = "your-video-path.mp4"`
  - Line 57: `output_path = "your-output-path.mp4"`
