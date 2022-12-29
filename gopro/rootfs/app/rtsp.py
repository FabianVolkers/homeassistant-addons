import subprocess
import socket
import os
import signal

class RTSPStream:
    def __init__(self, source, destination, name):
        self.source = source
        self.destination = destination
        self.name = name

    def send_rtsp(self):
        print("Starting RTSP Stream")
        subprocess.Popen([
            "ffmpeg",
            "-i",
            "udp://127.0.0.1:8555",
            "-fflags",
            "nobuffer",
            "-f:v",
            "mpegts",
            "-probesize",
            "8192",
            "-f",
            "rtsp",
            "-rtsp_transport",
            "tcp",
            "rtsp://127.0.0.1:18554/Fabis-Gopro.stream"
        ])

if __name__ == "__main__":
    print("Starting RTSP Stream")
    p = subprocess.Popen([
        "ffmpeg",
        "-i",
        "udp://127.0.0.1:8555",
        "-fflags",
        "nobuffer",
        "-f:v",
        "mpegts",
        "-probesize",
        "8192",
        "-f",
        "rtsp",
        "-rtsp_transport",
        "tcp",
        "rtsp://127.0.0.1:18554/Fabis-Gopro.stream"
    ])

    while True:
        pass

    os.killpg(os.getpgid(p.pid), signal.SIGTERM)