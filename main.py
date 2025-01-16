from yt_dlp import YoutubeDL
import os

playlist_url = 'https://www.youtube.com/playlist?list=PLRlwPks-XodI3CcKCpDaxlHQ9qB3R4ooc'

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Youtube_Downloads')
os.makedirs(desktop_path, exist_ok=True)

cookies_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'cookies.txt')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),
    'ignoreerrors': True,
    'verbose': True,
    'cookiefile': cookies_path
}

def download_playlist():
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Download completed! Files saved to: {desktop_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_playlist()