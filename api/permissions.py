from rest_framework.permissions import BasePermission


class OnCoursePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student.filter(id=request.user.id).exists()
