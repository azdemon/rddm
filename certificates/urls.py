from django.urls import path
from .views import IndexView, CertListView, CertDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='Templates_home'),
    path('list/', CertListView.as_view(), name='Templates_list'),
    path('list/<int:pk>', CertDetailView.as_view(), name='Templates_detail'),
]