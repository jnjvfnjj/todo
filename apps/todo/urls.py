from rest_framework.routers import DefaultRouter

from apps.todo.views import TodoViewSet

router = DefaultRouter()
router.register('',TodoViewSet, 'api_todo')

urlpatterns = router.urls