import logging
from datetime import datetime

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