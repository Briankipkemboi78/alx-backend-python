from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'profile_picture']


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model."""
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()  # Assuming `message_body` is a CharField for the message content.

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']
        read_only_fields = ['sent_at']

    def validate_message_body(self, value):
        """ Custom validation for the message body. """
        if len(value) < 1:
            raise serializers.ValidationError("Message body cannot be empty.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model."""
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True, source='messages_set')
    
    # Custom method field to get the number of messages
    message_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'message_count', 'created_at']
        read_only_fields = ['created_at']

    def get_message_count(self, obj):
        """ Custom method to return the message count for the conversation. """
        return obj.messages.count()

    def validate(self, data):
        """ Custom validation for the conversation. """
        if len(data['participants']) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return data
