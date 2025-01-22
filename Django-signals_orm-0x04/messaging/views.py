from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .models import Message
from .forms import MessageForm


def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account and related data have been deleted.")
        return redirect("home")
    
@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # Extract sender and receiver
            sender = request.user
            receiver_id = form.cleaned_data['receiver_id']  # Ensure your form includes receiver_id
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