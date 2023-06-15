import os
from moviepy.editor import *

def video_to_gif(input_path, output_path):
    video = VideoFileClip(input_path)
    video.write_gif(output_path)

def batch_convert_video_to_gif(folder_path):
    output_folder = os.path.join(folder_path, "gif")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith((".mp4", ".mov", ".avi")):
            input_path = os.path.join(folder_path, filename)
            output_filename = os.path.splitext(filename)[0] + ".gif"
            output_path = os.path.join(output_folder, output_filename)
            video_to_gif(input_path, output_path)

# 示例用法
folder_path = "your_folder_path"
batch_convert_video_to_gif(folder_path)
