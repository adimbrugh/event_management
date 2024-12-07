

from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include


router = DefaultRouter()

router.register('users', UserViewSet)
router.register('events', EventViewSet)

urlpatterns = [
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('',include(router.urls)),
]

urlpatterns += router.urls