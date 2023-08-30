# import required libraries
from vidgear.gears import NetGear
from imutils import build_montages
from threading import Thread
import cv2

class Stream:
    def __init__(self):
        self.options = {"multiserver_mode": True}
        self.data = []
        self.running = False
        self.rgb_frame = []
        self.flir_frame = []
        self.temperature = ""


    def __connection(self):
        self.client =  NetGear(
        address="0.0.0.0",
        port=(5577, 5578),
        protocol="tcp",
        pattern=1,
        receive_mode=True,
        logging=True,
        max_retries=100,
        **self.options) 
        print("connection created")
        while self.running:
            try:
                # receive data from network
                self.data = self.client.recv()
                # check if data received isn't None
                if self.data is None:
                    break
                # extract unique port address and its respective frame and received data
                unique_address, extracted_data, frame = self.data
                if unique_address == "5577":
                    self.rgb_frame = frame
                if unique_address == "5578":
                    self.flir_frame = frame
            except KeyboardInterrupt:
                break
                self.client.close()
              

    def start(self):
        self.running = True
        Thread(target=self.__connection).start()
     

    def stream_rgb(self):
        while self.running:
            if len(self.rgb_frame) > 0 :
                ret, buffer = cv2.imencode('.jpg', self.rgb_frame)
                stream_frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + stream_frame + b'\r\n')
    
    def stream_flir(self):
         while self.running:
            if len(self.rgb_frame) > 0:
                ret, buffer = cv2.imencode('.jpg', self.flir_frame)
                stream_frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + stream_frame + b'\r\n')