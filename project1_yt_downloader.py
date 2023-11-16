# pip install pytube  # instaleaza pachetul pytube

from pytube import YouTube # importa din pytube YouTube
import os

ask_user = True # am creat o variabila True pentru a face while loop

while ask_user is True: # cat timp variabila este True loop-ul va continua
    question = input("Ce format vrei sa descarci, Video, Mp4 sau Mp3. Scrie Q pentru a iesi: ").lower() # cerem input de la utilizator
    if question == "video": # daca raspunsul este video va rula urmatorul cod
        link = input("Video link: ") # cere input de la user cu link-ul de pe youtube
        yt = YouTube(link) # am creat o variabila noua unde folosim importul YouTube si intre () link-ul adaugat de user
        print(yt.title) # printam titlul video-ul
        print(yt.views) # printam cati view-uri are video-ul
        print(yt.author) # printam autorul video-ului
        video = yt.streams.get_highest_resolution().download("D:\IT\YT_Download\Video") # folosim o variabila noua unde ii spunem programului sa descarce ce-a mai mare rez # descarcam iar intre () ii spunem path-ul unde sa descarce. daca nu trecem nimic va descarca in folderul unde este fisierul
        print("DONE!") # un mesaj ca video-ul a fost descarcat
    elif question == "mp4": # daca imputul este mp4 va rula urmatorul program
        link = input("MP4 link: ") # cere input de la user cu link-ul de pe youtube
        yt = YouTube(link) # am creat o variabila noua unde folosim importul YouTube si intre () link-ul adaugat de user
        print(yt.title) # printam titlul video-ul
        print(yt.views) # printam cati view-uri are video-ul
        print(yt.author) # printam autorul video-ului
        video = yt.streams.filter(only_audio=True).first().download("D:\IT\YT_Download\Mp4")  # descarcam doar audio si ii spunem unde sa descarce fisierul
        new_name = os.path.splitext(video) # scriem o noua variabila unde facem splt-ul numelui
        os.rename(video, new_name[0] + '.mp4') # schimbam numele fisierului, noul nume + '.mp4'
        print("DONE!") # un mesaj ca video-ul a fost descarcat
    elif question == "mp3":
        link = input("MP3 link: ")
        yt = YouTube(link)
        print(yt.title)
        print(yt.views)
        print(yt.author)
        video = yt.streams.filter(only_audio=True).first().download("D:\IT\YT_Download\Mp3")  # descarcam doar audio si ii spunem unde sa descarce fisierul
        new_name = os.path.splitext(video)
        os.rename(video, new_name[0] + '.mp3')
        print("DONE!")
    elif question == "q":
        print("La revedere!")
        quit()
else:
    question = input("Ce format vrei sa descarci, Video, Mp4 sau Mp3. Scrie Q pentru a iesi: ").lower() # cerem input de la utilizator