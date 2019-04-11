
# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import CameraServer.ftp_camera_client
async def listen(websocket, path):
    await websocket.send("Hello")
    while True:
        message = await websocket.recv()
        message = message.strip()
        print("Message received: " + message)
        if(message == "{start}"):
            print("Taking photo")
            fileName = CameraServer.ftp_camera_client.send_file()
            await websocket.send(fileName)
        elif (message == "{end}"):
            print("Closing connection to FTP")
            CameraServer.ftp_camera_client.close_connection()




start_server = websockets.serve(listen, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()