from moviepy.editor import VideoFileClip
import os

def konvèti_videyo_an_gif(chemin_videyo, chemen_gif, max_dire=10):
  
    if not os.path.exists(chemin_videyo):
        print(f"Erè: Fichye {chemin_videyo} pa ekziste.")
        return
    videyo_clip = VideoFileClip(chemin_videyo)
    videyo_clip = videyo_clip.subclip(0, min(videyo_clip.duration, max_dire))
    videyo_clip.write_gif(chemen_gif)
    
    print(f"Konvèsyon an fèt avèk siksè. GIF a nan {chemen_gif}")

if __name__ == "__main__":
    chemin_videyo = r"C:\Users\ING BP\Desktop\Projet2\PRJT\input.mp4"
    chemen_gif = r"C:\Users\ING BP\Desktop\Projet2\PRJT\output.gif"
    max_dire = 10
    
    konvèti_videyo_an_gif(chemin_videyo, chemen_gif, max_dire)
