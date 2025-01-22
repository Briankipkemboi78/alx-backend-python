from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account and related data have been deleted.")
        return redirect("home")