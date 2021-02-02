from pymine.server import server


@server.api.events.on_packet("handshaking", 0x00)
async def example_handle_handshake(stream, packet):
    server.logger.debug("Handshake packet received (example plugin speaking!)")

    return True, stream


@server.api.events.on_server_ready
async def on_server_ready():
    server.logger.info("AYYY SERVER DO BE READY THO NGL?")

    
@server.api.events.on_server_stop
async def on_server_stop():
    server.logger.info("bish you better start this server back up")


async def setup(server, plugin_yml):
    server.logger.info("setup coroutine called for the example plugin!")
    server.logger.debug(str(plugin_yml))


async def teardown(server):
    server.logger.info("teardown coroutine called for the example plugin!")
