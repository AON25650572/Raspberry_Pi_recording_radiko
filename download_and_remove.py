import updown

TOKEN = 'fzGKAI2TU6wAAAAAAAAAAQjP2w9F9mD6GSFa0sTRzQNuId_TT3q37p9AvhBHZs3L'
download_folder = 'C:\\Users\\aon25\\Documents\\GitHub\\Raspberry_Pi_recording_radiko'
list_folder = updown.list_folder(updown.dropbox.Dropbox(TOKEN),'','')

for fname in list_folder.keys():
    print(fname)
    with open(download_folder+'\\'+fname,'wb') as f:
        f.write(updown.download(updown.dropbox.Dropbox(TOKEN),'','',fname))
    updown.delete(updown.dropbox.Dropbox(TOKEN),'','',fname)