import updown

TOKEN = 'hogehogehoge'
download_folder = 'C:\\hogehoge'
list_folder = updown.list_folder(updown.dropbox.Dropbox(TOKEN),'','')

for fname in list_folder.keys():
    print(fname)
    with open(download_folder+'\\'+fname,'wb') as f:
        f.write(updown.download(updown.dropbox.Dropbox(TOKEN),'','',fname))
    updown.delete(updown.dropbox.Dropbox(TOKEN),'','',fname)
