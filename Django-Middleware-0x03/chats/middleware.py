import logging
from datetime import datetime
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response =  get_response
        logging.basicConfig(
            filename="requests.log",
            level=logging.INFO,
            format="%(message)s",
        )
        
    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        # Pass the request to the next middleware or view
        response = self.get_response(request)
        return response
    
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        """
        Initializing the middleware
        """
        self.get_respone = get_response

    def __call__(self, request):
        current_time = datetime.now().hour

        if current_time < 9 or current_time >=18:
            return HttpResponseForbidden("Access to the chat is restricted outside 9 AM to 6 PM.")
        
        response = self.get_respone
        return response