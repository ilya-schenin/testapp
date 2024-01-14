from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from jwt import InvalidTokenError, decode

User = get_user_model()


class JWTAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        jwt = self.get_token_from_scope(scope)
        token = self.decode_token(jwt)
        scope['user'] = await self.get_user(int(token['user_id']))

        return await self.app(scope, receive, send)

    @staticmethod
    def get_token_from_scope(scope):
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            auth_header = headers[b'authorization'].decode('utf-8')
            _, token = auth_header.split()
            return token
        else:
            return None

    @staticmethod
    def decode_token(token):
        decoded_payload = decode(jwt=token, options={"verify_signature": False}, algorithms=['HS256'])
        return decoded_payload

    @staticmethod
    @database_sync_to_async
    def get_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return AnonymousUser()
