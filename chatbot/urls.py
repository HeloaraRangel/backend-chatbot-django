from rest_framework.routers import DefaultRouter
from .views import DocumentoViewSet

router = DefaultRouter()
router.register('documentos', DocumentoViewSet)

urlpatterns = router.urls