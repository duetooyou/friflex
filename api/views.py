from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Rating
from .serializers import (CourseSerializer,
                          CourseEnrollSerializer,
                          ContentSerializer,
                          RatingSerializer)
from .permissions import OnCoursePermission


class CourseView(ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @action(methods=['PUT'],
            detail=True,
            serializer_class=CourseEnrollSerializer,
            url_path='enroll')
    def register_on_course(self, request, *args, **kwargs):
        course = self.get_object()
        course.student.add(request.user)
        return Response({'Регистрация': 'Вы успешно записались на курс'})

    @action(permission_classes=[OnCoursePermission],
            methods=['GET'],
            detail=True,
            url_path='content',
            serializer_class=ContentSerializer)
    def get_course_content(self, request, *args, **kwargs):
        contents = self.get_object().contents
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def get_view_name(self):
        return f'Курсы и регистрация'


class CourseRatingCreateView(CreateAPIView):
    serializer_class = RatingSerializer
    queryset = RatingSerializer

    def perform_create(self, serializer):
        if Rating.objects.filter(course_id=self.request.data.get('course'),
                                 reviewer=self.request.user).exists():
            raise ValidationError('Вы оставляли оценку для этого курса')
        else:
            serializer.save(reviewer=self.request.user)

    def get_view_name(self):
        return f'Оценка курса'
