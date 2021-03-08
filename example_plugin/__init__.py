from pymine.api.abc import AbstractPlugin
import pymine.add_plugin


class MyExamplePlugin(AbstractPlugin):
    def __init__(self, server, plugin_yml):
        self.server = server
        self.config = plugin_yml

    @server.api.register.on_packet("handshaking", 0x00)
    async def my_packet_handler(stream, placket):
        server.console.debug("EXAMPLE PLUGIN: Handshake packet received!")

    @server.api.register.on_server_start
    async def my_server_start_handler():
        server.console.debug("EXAMPLE PLUGIN: Ayyy server do be ready tho ngl")

    @server.api.register.on_server_stop
    async def my_server_stop_handler():
        server.console.debug("EXAMPLE PLUGIN: bishhh you better be starting this server right back up or else")

    async def teardown(self):
        server.console.debug("EXAMPLE PLUGIN: being teared down...")


async def setup(server, plugin_yml):
    pymine.add_plugin(MyExamplePlugin(server, plugin_yml))


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
