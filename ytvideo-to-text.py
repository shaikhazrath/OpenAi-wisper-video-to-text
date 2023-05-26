import pytube
import moviepy.editor as mp
import os
import whisper

def extract_audio(video_url, output_path):
    # Create a YouTube object and get the video
    yt = pytube.YouTube(video_url)
    video = yt.streams.first()

    # Download the video as an mp4 file
    video_file = video.download()

    # Set the output audio file path
    audio_file = output_path + "/audio.wav"

    # Convert the downloaded video to audio
    clip = mp.VideoFileClip(video_file)
    clip.audio.write_audiofile(audio_file, codec="pcm_s16le")

    # Perform audio-to-text conversion
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    formatted_text = result["text"].replace('. ', '.\n\n')
    with open('output.txt', 'w') as file:
        file.write(formatted_text)



    # Delete the temporary video and audio files
    clip.close()
    if os.path.exists(video_file):
        os.remove(video_file)
    if os.path.exists(audio_file):
        os.remove(audio_file)

# Example usage
video_url = "https://www.youtube.com/watch?v=DRpo9_x27zM"
output_path = "./"

extract_audio(video_url, output_path)
