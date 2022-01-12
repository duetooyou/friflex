from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseView, CourseRatingCreateView


router = DefaultRouter()
router.register('courses', CourseView, basename='all_courses')


urlpatterns = [
    path('', include(router.urls)),
    path('course/rating/', CourseRatingCreateView.as_view())
]
