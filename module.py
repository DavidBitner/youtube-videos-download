import pytube


def choose_directory():
    directory = input('Input the directory were the videos are going to: ')
    return directory


def download(directory='C:/Users/David/Desktop/Videos'):
    while True:
        video_url = input('Youtube URL: [0 to end] ')
        if video_url == '0':
            break
        youtube = pytube.YouTube(video_url)
        print(f'Downloading: {youtube.title}')
        video = youtube.streams.get_highest_resolution()
        video.download(directory)
        print('Download finished')


# main
d = choose_directory()
download(d)
print('Goodbye')
