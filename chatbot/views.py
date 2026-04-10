from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Documento
from .serializers import DocumentoSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from .models import Usuario
from .serializers import UsuarioSerializer

from .serializers import PerguntarSerializer

from .models import Pergunta, Conversa, Resposta
from .serializers import (
    PerguntaSerializer,
    ConversaSerializer,
    RespostaSerializer
)


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = (MultiPartParser, FormParser)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # 🔐 LOGIN
    @action(detail=False, methods=['post'])
    def login(self, request):

        email = request.data.get("email")
        senha = request.data.get("senha")

        try:
            usuario = Usuario.objects.get(email=email)

            if usuario.check_senha(senha):

                usuario.ultimo_acesso = timezone.now()
                usuario.save()

                return Response({
                    "mensagem": "Login realizado com sucesso",
                    "usuario": usuario.nome,
                })

            else:

                return Response({
                    "erro": "Senha incorreta"
                }, status=status.HTTP_401_UNAUTHORIZED)

        except Usuario.DoesNotExist:

            return Response({
                "erro": "Usuário não encontrado"
            }, status=status.HTTP_404_NOT_FOUND)












# -------------------------
# PERGUNTAS
# -------------------------

class PerguntaViewSet(viewsets.ModelViewSet):

    queryset = Pergunta.objects.all().order_by('-id_pergunta')
    serializer_class = PerguntaSerializer


# -------------------------
# CONVERSAS
# -------------------------

class ConversaViewSet(viewsets.ModelViewSet):

    queryset = Conversa.objects.all().order_by('-id_conversa')
    serializer_class = ConversaSerializer


# -------------------------
# ENDPOINT PRINCIPAL DO CHAT
# -------------------------

from rest_framework.views import APIView


class PerguntarAPIView(APIView):

    def post(self, request):

        serializer = PerguntarSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        texto = serializer.validated_data["texto"]

        # cria conversa
        conversa = Conversa.objects.create()

        # cria pergunta
        pergunta = Pergunta.objects.create(
            texto_pergunta=texto,
            conversa=conversa
        )

        # resposta temporária (mock)
        resposta_texto = (
            "Resposta automática temporária. "
            "Depois será gerada pelo NLP/RAG."
        )

        resposta = Resposta.objects.create(
            texto_resposta=resposta_texto,
            pergunta=pergunta
        )

        return Response({

            "conversa_id": conversa.id_conversa,
            "pergunta": pergunta.texto_pergunta,
            "resposta": resposta.texto_resposta
        })