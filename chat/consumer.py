from channels.generic.websocket import WebsocketConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        user_id = self.scope['user'].username
        self.room_group_name = f'group_{user_id}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def websocket_receive(self, text_data):
        text_data = json.loads(text_data['text'])
        group = f'group_{text_data["to_username"]}'
        async_to_sync(self.channel_layer.group_send)(
            group, {
                'type': 'chat_message',
                'message': text_data['message']
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

    def websocket_disconnect(self, event):
        pass