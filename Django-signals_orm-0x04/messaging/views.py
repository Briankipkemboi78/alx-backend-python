from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message
from .forms import MessageForm

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # Extract sender and receiver
            sender = request.user
            receiver_id = form.cleaned_data['receiver_id']
            receiver = get_object_or_404(User, id=receiver_id)
            
            # Create the message
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=form.cleaned_data['content']
            )
            return JsonResponse({"status": "Message sent successfully"})
        else:
            return JsonResponse({"status": "Form validation failed", "errors": form.errors})

    return JsonResponse({"status": "Invalid request method"})

@login_required
def view_messages(request):
    # Retrieve messages for the logged-in user (filter messages by the receiver)
    messages = Message.objects.filter(receiver=request.user).select_related('sender')
    
    # Return the messages as JSON (or render them in a template)
    messages_data = [
        {
            "sender": message.sender.username,
            "content": message.content,
            "timestamp": message.timestamp
        }
        for message in messages
    ]
    
    return JsonResponse({"messages": messages_data})

