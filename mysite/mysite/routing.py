from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import chat.routing
import chat.consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
    "channel": ChannelNameRouter({
        "thumbnails-generate": chat.consumers.GenerateConsumer,
        # "thunbnails-delete": consumers.DeleteConsumer,
    }),
})