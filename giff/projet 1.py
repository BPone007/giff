
from moviepy.editor import VideoFileClip

def video_to_gif(input_path, output_path, fps=8):
  # Nou kreye objet video ah
    clip = VideoFileClip(input_path)

    clip.write_gif(output_path, fps=fps)
#itilizasyon fonksyon ahn 
input_video_path = 'videyo.mp4'

output_gif_path = 'animasyon.gif'

frame_rate = 8

video_to_gif(input_video_path, output_gif_path, frame_rate)
