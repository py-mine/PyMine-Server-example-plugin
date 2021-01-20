from pymine.api.server import on_server_ready, on_server_stop
from pymine.api.packet import handle_packet


@handle_packet('handshaking', 0x00)
async def example_handle_handshake(stream, packet):
    print('Hello this is the example packet handler speaking how may I take your order sir')

    return True, stream


@on_server_ready
async def on_server_ready():
    print('AYYY SERVER DO BE WORKING THO NGL')


@on_server_stop
async def on_server_stop():
    print('*bish you better start this server back up*')


async def setup():
    print('setup function called for the example plugin!')
