from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Content, Course, Rating
from .serializers import (CourseSerializer,
                          CourseEnrollSerializer,
                          ContentSerializer,
                          RatingSerializer)


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

    @action(methods=['GET'],
            detail=True,
            url_path='content',
            serializer_class=ContentSerializer)
    def get_course_content(self, request, pk=None, *args, **kwargs):
        contents = Content.objects.filter(course_id=pk)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def get_view_name(self):
        return f'Курсы и регистрация'


class CourseRatingCreateView(CreateAPIView):
    serializer_class = RatingSerializer
    queryset = RatingSerializer

    def perform_create(self, serializer):
        if Rating.objects.filter(course_id=self.request.data.get('course'), reviewer=self.request.user).exists():
            raise ValidationError('Вы оставляли оценку для этого курса')
        else:
            serializer.save(reviewer=self.request.user)
