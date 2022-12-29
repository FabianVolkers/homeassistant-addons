from goprocam.GoProCamera import GoPro
from goprocam import constants
import logging

logger = logging.getLogger(__name__)
print("gopro.py")
print(__name__)

class GoProDevice(GoPro):
    def __init__(self):
        super().__init__()

    @property
    def stream_address(self):
        if self.whichCam() == constants.Camera.Interface.GPControl:
            return "ffmpeg -f mpegts -i udp://" + self.ip_addr + ":8554 -b 800k -r 30"
        elif self.whichCam() == constants.Camera.Interface.Auth:
            return "ffmpeg -i http://" + self.ip_addr + "live/amba.m3u8"


    def stream(self, quality=""):
        """Starts the GoPro live feed and sends keepalive packages.
        quality: high/medium/low
        """
        print(f"Starting gopro feed with quality {quality}")
        self.livestream("start")
        if self.whichCam() == constants.Camera.Interface.GPControl:
            if "HERO4" in self.infoCamera("model_name"):
                if quality == "high":
                    self.streamSettings("2400000", "6")
                elif quality == "medium":
                    self.streamSettings("1000000", "4")
                elif quality == "low":
                    self.streamSettings("250000", "0")
            else:
                if quality == "high":
                    self.streamSettings("4000000", "7")
                elif quality == "medium":
                    self.streamSettings("1000000", "4")
                elif quality == "low":
                    self.streamSettings("250000", "0")
            print("Sending keepalive")
            self.KeepAlive()

if __name__ == "__main__":
    logger.info("Starting gopro live feed")
    gopro = GoProDevice()
    logger.debug(gopro)
    gopro.stream(quality="medium")