from django.shortcuts import render, get_object_or_404
from .models import Message

def message_history_view(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    history = message.history.all().order_by('-edited_at')
    return render(request, 'message_history.html', {'message': message, 'history': history})
