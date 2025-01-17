import logging
from datetime import datetime
import time
from collections import defaultdict
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
        
        response = self.get_respone(request)
        return response
    

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_message_count = defaultdict(list)


    def __call__(self, request):
        if request.method == 'POST' and 'message' in request.POST:
            ip_address = request.META.get("REMOTE_ADDR")
            current_time = time.time()


            self.ip_message_count[ip_address] = [
                timestamp for timestamp in self.ip_message_count[ip_address]
                if current_time - timestamp < 60
            ]

            if len(self.ip_message_count[ip_address]) >= 5:
                return HttpResponseForbidden("You have exceeded the message limit of 5 messages per minute.")
            self.ip_message_count[ip_address].append(current_time)

        response = self.get_response(request)

        return response
        

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role not in ['admin', 'moderator']:
                return HttpResponseForbidden("You do not have permission to access this page.")
            else:
                return HttpResponseForbidden("You need to be logged in to access this page.")
            
        response = self.get_response(request)
        return response
