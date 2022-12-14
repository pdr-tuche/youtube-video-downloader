from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("ih, deu treta no download do seu video...")
  print("Download completo !! =)")

link = input("manda o link do video aqui pae -> URL: ")
Download(link)