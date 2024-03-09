from django.urls import path
from .views import (
    IndexView,
    DocumentListView,
    DocumentDetailView,
    DocumentCreateView,
    DocumentUpdateView,
    DocumentDeleteView,
    privacy_policy,
    terms_of_service
)

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('documents/', DocumentListView.as_view(), name='documents'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('documents/create/', DocumentCreateView.as_view(), name='document_create'),
    path('documents/<int:pk>/update/', DocumentUpdateView.as_view(), name='document_update'),
    path('documents/<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
]