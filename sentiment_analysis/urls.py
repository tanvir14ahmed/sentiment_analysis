from django.contrib import admin
from django.urls import path
from sentiment_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/sentiment/', views.SentimentAnalysisAPIView.as_view(), name='sentiment_api'),
]
