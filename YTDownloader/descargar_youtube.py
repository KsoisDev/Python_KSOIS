from yt_dlp import YoutubeDL

def descargar_video(url, formato):
    if formato == "mp4":
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": "%(title)s.%(ext)s",
        }
    elif formato == "mp3":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",  # máxima calidad MP3
            }],
        }
    else:
        print("Formato no válido. Usa mp3 o mp4.")
        return

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Pega el enlace de YouTube: ").strip()
    formato = input("¿Qué formato quieres? (mp3/mp4): ").strip().lower()
    descargar_video(url, formato)
