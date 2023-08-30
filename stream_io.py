from vidgear.gears import NetGear
import base64
import cv2

def send_frame(socketio,frame,port):
        # ret, buffer = cv2.imencode('.jpg', frame)
        frame_buffer = cv2.imencode('.jpg', frame)[1].tobytes()
        stream_frame =  base64.encodebytes(frame_buffer).decode("utf-8")
        if port == "5577":
            socketio.emit("rgb_video",stream_frame)
        if port == "5578":
             socketio.emit("flir_video",stream_frame)
        socketio.sleep(0)

def stream(socketio):
    # activate multiserver_mode
    options = {"multiserver_mode": True}
    # Define NetGear Client at given IP address and assign list/tuple of all unique Server((5577,5578) in our case) and other parameters
    # !!! change following IP address '192.168.x.xxx' with yours !!!
    client = NetGear(
        address="0.0.0.0",
        port=(5577, 5578),
        protocol="tcp",
        pattern=1,
        receive_mode=True,
        logging=True,
        **options
    )  
    while True:
        try:
            # receive data from network
            data = client.recv()

            # check if data received isn't None
            if data is None:
                break

            # extract unique port address and its respective frame and received data
            unique_port, extracted_data, frame = data
            send_frame(socketio,frame,unique_port)

        except KeyboardInterrupt:
            break