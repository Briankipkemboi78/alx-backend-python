from django.urls import path, include
from rest_framework.routers import SimpleRouter  # Use SimpleRouter instead of DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import ConversationViewSet, MessageViewSet, UserCreateView

# Main router
router = SimpleRouter()  # Use SimpleRouter here
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router
conversations_router = NestedSimpleRouter(router, r'conversations', lookup='conversation')
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Authentication router (Separate from the nested router logic)
auth_router = SimpleRouter()  # SimpleRouter here as well
auth_router.register(r'users', UserCreateView, basename='users')

# URL patterns
main_api_urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversations_router.urls)),  # Include the nested router
]

auth_api_urlpatterns = [
    path('', include(auth_router.urls)), 
]
