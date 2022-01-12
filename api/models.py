from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Course(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name="Название курса")
    student = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                verbose_name='Слушатель курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Список курсов'

    def __str__(self):
        return f'{self.name}'


class Rating(models.Model):
    GRADE_CHOICE = (('1', 'one'),
                    ('2', 'two'),
                    ('3', 'three'),
                    ('4', 'four'),
                    ('5', 'five'))

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name='Курс',
                               related_name='course_rating')
    reviewer = models.ForeignKey(get_user_model(),
                                 on_delete=models.CASCADE,
                                 verbose_name='Автор оценки',
                                 related_name='course_reviewer')
    grade = models.TextField(choices=GRADE_CHOICE,
                             verbose_name='Оценка')

    class Meta:
        unique_together = ('reviewer', 'course')
        verbose_name = 'Оценка'
        verbose_name_plural = 'Список оценок'

    def __str__(self):
        return f'{self.reviewer} оценил курс {self.course} на {self.grade}'


class BaseContent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Время создания содержимого')

    class Meta:
        abstract = True


class Text(BaseContent):
    description = models.TextField(max_length=500,
                                   verbose_name='Текстовое описание')

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текстовое содержимое'

    def __str__(self):
        return f'Описание {self.description}'


class File(BaseContent):
    pdf_file = models.FileField(upload_to='files',
                                verbose_name='PDF')

    class Meta:
        verbose_name = 'PDF'
        verbose_name_plural = 'Список PDF файлов'

    def __str__(self):
        return f'PDF файл {self.pdf_file}'


class Link(BaseContent):
    url = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Список ссылок'

    def __str__(self):
        return f'Ссылка {self.url}'


class Content(models.Model):

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='contents')
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE,
                              related_name='%(class)s',
                              verbose_name='Создатель контента курса')
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'file',
                                         'link')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Содержимое курса'
        verbose_name_plural = 'Список содержимого курса'

    def __str__(self):
        return f'{self.course} {self.content_type}'
