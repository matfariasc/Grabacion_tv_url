from ffmpy3 import FFmpeg
import datetime
import time
import os
import errno

# variables entorno
canal = sys.argv[1] #nombre de canal
url = sys.argv[2] #URL
# fucion


def ffmpeg_path(inputs_path, outputs_path):
    a = FFmpeg(
        inputs={inputs_path: None},
        outputs={outputs_path: f'-c copy -reset_timestamps 1 -segment_atclocktime 1 -segment_time 3800 -t 01:00:00 -f segment -strftime 1 ',
                 }
    )
    a.run()

parent_dir = "/var/www/html/tv.cl"
path = os.path.join(parent_dir,canal)


try:
    os.mkdir(path)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise



formato = "/var/www/html/tv.cl/"+canal+"/"+"1_%Y%m%d_%H%M01"+'.mp4'

try:
    ffmpeg_path(url, formato)
except:
    print("error de cordinacion con la hora, intentando nuevamnete en el siguiente cron")

