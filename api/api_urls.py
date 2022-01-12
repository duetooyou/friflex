from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CourseView, CourseRatingCreateView


router = DefaultRouter()
router.register('courses', CourseView, basename='all_courses')


urlpatterns = [
    path('', include(router.urls)),
    path('tokens/', TokenObtainPairView.as_view()),
    path('tokens/refresh/', TokenRefreshView.as_view()),
    path('course/rating/', CourseRatingCreateView.as_view())
]
