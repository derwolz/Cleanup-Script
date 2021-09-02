import subprocess, os, logging
from datetime import datetime, timedelta
from os import scandir

######Inputs#####

log_file = r"./DeleteResults.log"
path_complete = "e:/Downloads/Complete/"
path_p4 ="e:/perforce/UE4-UserContent/4*/*/*"
daysold = 14

######Function####
def del_items(_path):
    delete_command = "Remove-Item -recurse \'"+ _path + "\' "
    returncode = subprocess.run(["powershell", "-Command", str(delete_command)],
        capture_output=True).returncode
    return returncode
    
######setting up logging########
logging.basicConfig( filename = log_file, filemode = 'a', level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s: %(message)s',\
    datefmt = '%m%d%Y %I:%M:%S %p' )

######establishing variables#####
today = datetime.now()
deletedate = today - timedelta(days=daysold)
deletedate = deletedate.timestamp()
Files = os.scandir(path_complete)
deleted_files = []

######The Work###################
del_items(path_p4)

with Files as entries:
    for file in entries:
        info = file.stat() 
        if info.st_mtime < deletedate:
            if del_items(path_complete + file.name) != 0:
                logging.debug(str(success.stderr)+"\n")
            else:
                deleted_files.append(file.name)
                
#####log results#################
for i in deleted_files:
    print('Deleted:' + str(i))
    logging.debug("Deleted: "+str(i))
print('completed projects deleted older than ' + str(daysold) + ' days old')
logging.debug("Last ran at: " + str(today))