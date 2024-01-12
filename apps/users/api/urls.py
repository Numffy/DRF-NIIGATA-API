from django.urls import path
from apps.users.api.api import user_api_view,user_detai_api_view
urlpatterns = [
   path('users/',user_api_view, name='user_api'),
   path('users/<int:pk>/', user_detai_api_view, name='user_detail_view')
]