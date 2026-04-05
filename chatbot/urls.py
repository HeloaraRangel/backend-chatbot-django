from rest_framework.routers import DefaultRouter
from .views import DocumentoViewSet
from .views import (
    UsuarioViewSet,
    PerfilViewSet
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PerguntaViewSet,
    ConversaViewSet,
    PerguntarAPIView
)

router = DefaultRouter()

router.register('documentos', DocumentoViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('perfis', PerfilViewSet)


# NOVOS endpoints
router.register('perguntas', PerguntaViewSet)
router.register('conversas', ConversaViewSet)



urlpatterns = router.urls

