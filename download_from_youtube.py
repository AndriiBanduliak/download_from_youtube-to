from pytube import YouTube
import ffmpeg

URL = "https://www.youtube.com/watch?v=Y_sXzI0clxs"
DOWNLOAD = "download"

def download_video(url):
    yt = YouTube(url)
    #yt.streams.get_audio_only().download(DOWNLOAD) #download audio only
    #yt.streams.get_highest_resolution().download(DOWNLOAD) #download video only 
    '''for steam in yt.streams:
        print(steam)'''
    steam_video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    #print(steam_video)
    stream_video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    stream_video.download(DOWNLOAD, 'video')
    if not stream_video.is_progressive:
        stream_audio = yt.streams.get_audio_only()
        stream_audio.download(DOWNLOAD, 'audio')
        combine(DOWNLOAD + '/audio.mp4', DOWNLOAD + '/video.mp4')


def combine(audio, video):
    audio_stream = ffmpeg.input(audio)
    video_stream = ffmpeg.input(video)
    ffmpeg.output(audio_stream, video_stream, DOWNLOAD + '/result.mp4').run()
    


if __name__ == "__main__":
    download_video(URL)
    