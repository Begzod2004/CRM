from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import  *

router = DefaultRouter()
router.register('director',DirectorViewset)
router.register('manager',ManagerViewset)

urlpatterns = [
    path('',include(router.urls))
]
