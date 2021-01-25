import updown
import sys

args = sys.argv
folder_path = args[1]
fname = args[2]
TOKEN = 'hogehogehoge'


updown.upload(updown.dropbox.Dropbox(TOKEN),folder_path+'/'+fname,'','',fname)
