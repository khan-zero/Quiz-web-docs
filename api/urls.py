from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, CustomTokenObtainPairView

urlpatterns = [
    path('quiz-list/', views.QuizListView.as_view(), name='quiz-list'),
    path('quiz-detail/<int:pk>/', views.QuizDetailView.as_view(), name='quiz-detail'),
    path('submit/', views.SubmitAnswerView.as_view(), name='submit'),
    path('quiz-result/<int:pk>/', views.QuizResultView.as_view(), name='quiz-result'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-custom/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair_custom'),
]

