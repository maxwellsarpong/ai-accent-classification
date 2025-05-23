import requests
import os
from moviepy import VideoFileClip

# Function to extract audio from a video URL and save it as an MP3 file
# This function downloads a video from a given URL, extracts the audio, and saves it as an MP3 file.
def extract_audio_from_mp4_url(video_url: str, output_audio_path: str = "output_audio.mp3"):
    video_filename = "temp_video.mp4"

    # Step 1: Download video
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(video_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
    else:
        raise Exception(f"Failed to download video. Status code: {response.status_code}")

    # Sanity check: ensure the file is not empty
    if os.path.getsize(video_filename) == 0:
        os.remove(video_filename)
        raise Exception("Downloaded file is empty. Invalid video URL or content.")

    video = None
    try:
        try:
            video = VideoFileClip(video_filename)
        except OSError as e:
            raise Exception(f"Failed to read video file with ffmpeg. Check if ffmpeg is installed and the video is valid.\nOriginal error: {e}")

        if not video.audio:
            raise Exception("No audio stream found in the video.")
        video.audio.write_audiofile(output_audio_path)
        print(f"Audio saved to {output_audio_path}")
    finally:
        if video:
            video.close()
        if os.path.exists(video_filename):
            os.remove(video_filename)