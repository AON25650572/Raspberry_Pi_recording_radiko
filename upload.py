import updown
import sys

args = sys.argv
folder_path = args[1]
fname = args[2]
TOKEN = 'fzGKAI2TU6wAAAAAAAAAAQjP2w9F9mD6GSFa0sTRzQNuId_TT3q37p9AvhBHZs3L'


updown.upload(updown.dropbox.Dropbox(TOKEN),folder_path+'/'+fname,'','',fname)