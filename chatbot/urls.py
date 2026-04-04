from rest_framework.routers import DefaultRouter
from .views import DocumentoViewSet, ConversaViewSet
from .views import PerguntaViewSet, ConversaViewSet
from .views import (
    UsuarioViewSet,
    PerfilViewSet
)

router = DefaultRouter()

router.register('documentos', DocumentoViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('perfis', PerfilViewSet)


router.register('conversa', ConversaViewSet, basename='conversa')
router.register('pergunta', PerguntaViewSet)


urlpatterns = router.urls