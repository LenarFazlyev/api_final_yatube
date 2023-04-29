from rest_framework import permissions

# Зря что-ли столько времени было потрачено )
MESSAGE: dict = {
    'Post': 'поста',
    'Comment': 'коммента',
}


class OwnerOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого {viewset_class} запрещено!!!'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        self.message = self.message.format(
            viewset_class=MESSAGE[type(obj).__name__]
        )
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
