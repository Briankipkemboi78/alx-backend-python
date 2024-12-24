from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create views for obtaining JWT token and refreshing it
class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass