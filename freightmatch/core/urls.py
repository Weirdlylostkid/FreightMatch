from django.urls import path
from .views import UploadRoutes, Chatbot

urlpatterns = [
    path('upload-routes/', UploadRoutes.as_view(), name='upload-routes'),
    path('chatbot/', Chatbot.as_view(), name='chatbot'),
]