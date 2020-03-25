from django.urls import path, include
from rest_framework import routers
from . import views

router =  routers.DefaultRouter()
router.register('users', views.UserViewset)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]