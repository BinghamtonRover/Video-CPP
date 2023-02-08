from lib.network import ProtoServer
from lib.network.generated.Protobuf.video_pb2 import *

#udpServer = UdpServer(8001)
#udpServer.start()
server = ProtoServer(8001)
server.start()
#ProtoServer.start()

#server.on_data("CameraStatus",8001)
