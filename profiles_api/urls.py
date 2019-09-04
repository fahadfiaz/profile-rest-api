from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, LoginViewSet, UserProfileFeedViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='loin')
router.register('feed', UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]
