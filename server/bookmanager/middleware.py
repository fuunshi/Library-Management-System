from django.http import JsonResponse
from django.conf import settings
from rest_framework.authtoken.models import Token

class TokenAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Skip authorization for certain views, if needed
        if getattr(view_func, 'skip_authorization', False):
            return None

        # Check if 'Authorization' header is present in the request
        authorization_header = request.headers.get('Authorization', None)

        if not authorization_header:
            return JsonResponse({'error': 'Authorization header not present'}, status=401)

        # Extract the token from the header
        _, token = authorization_header.split()

        # Verify the token
        try:
            token_obj = Token.objects.get(key=token)
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # Attach the user to the request for further processing
        request.user = token_obj.user

        return None
