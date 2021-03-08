# from pymine.server import server
#
#
# @server.api.events.on_packet("handshaking", 0x00)
# async def example_handle_handshake(stream, packet):
#     server.console.debug("EXAMPLE PLUGIN: Handshake packet received!")
#
#     return True, stream
#
#
# @server.api.events.on_server_ready
# async def on_server_ready():
#     server.console.info("EXAMPLE PLUGIN: AYYY SERVER DO BE READY THO NGL?")
#
#
# @server.api.events.on_server_stop
# async def on_server_stop():
#     server.console.info("EXAMPLE PLUGIN: bish you better start this server back up")
#
#
# async def setup(server, plugin_yml):
#     server.console.info("EXAMPLE PLUGIN: setup coroutine called!")
#
#
# async def teardown(server):
#     server.console.info("EXAMPLE PLUGIN: teardown coroutine!")
