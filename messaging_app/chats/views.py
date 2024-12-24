from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for viewing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['participants']  # You can filter by participants
    ordering_fields = ['created_at']  # You can order conversations by creation date
    ordering = ['-created_at']  # Default ordering: most recent conversations first

    def perform_create(self, serializer):
        """
        Overriding the create method to set the user who created the conversation.
        """
        serializer.save()

    @action(detail=True, methods=['post'])
    def add_participants(self, request, pk=None):
        """
        Add participants to a conversation.
        """
        conversation = self.get_object()
        user_ids = request.data.get('user_ids', [])
        
        # Fetch users based on provided user IDs
        users = User.objects.filter(id__in=user_ids)
        if users.count() != len(user_ids):
            return Response({"error": "Some users do not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        conversation.participants.add(*users)
        conversation.save()

        return Response(ConversationSerializer(conversation).data, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for viewing, creating, and listing messages in a conversation.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['conversation', 'sender']  # You can filter messages by conversation and sender
    ordering_fields = ['timestamp']  # You can order messages by timestamp
    ordering = ['timestamp']  # Default ordering: oldest to newest

    def perform_create(self, serializer):
        """
        Overriding the create method to automatically associate a message with the current user.
        """
        serializer.save(sender=self.request.user)

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        """
        Send a new message to a conversation.
        """
        conversation = self.get_object()
        message_body = request.data.get('message_body', '')
        
        # Ensure message body is provided
        if not message_body:
            return Response({"error": "Message body cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new message within the conversation
        message = Message.objects.create(
            sender=request.user,
            conversation=conversation,
            message_body=message_body
        )

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)


