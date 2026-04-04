from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Documento
from .serializers import DocumentoSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Pergunta, Conversa
from .serializers import PerguntaSerializer
from .serializers import ConversaSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from .models import Usuario, PerfilDeAcesso
from .serializers import UsuarioSerializer, PerfilSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = (MultiPartParser, FormParser)


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = PerfilDeAcesso.objects.all()
    serializer_class = PerfilSerializer


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
                    "perfil": usuario.perfil.descricao_perfil
                })

            else:

                return Response({
                    "erro": "Senha incorreta"
                }, status=status.HTTP_401_UNAUTHORIZED)

        except Usuario.DoesNotExist:

            return Response({
                "erro": "Usuário não encontrado"
            }, status=status.HTTP_404_NOT_FOUND)











class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


    
    
class ConversaViewSet(viewsets.ModelViewSet):
    queryset = Conversa.objects.all()
    serializer_class = ConversaSerializer

#class ConversaViewSet(viewsets.ViewSet):

 #   @swagger_auto_schema(
  #      request_body=PerguntaSerializer
   # )
    #@action(
    #    detail=False,
   #     methods=['post'],
   #     url_path='pergunta'
   # )
  #  def pergunta(self, request):
#
   #     serializer = PerguntaSerializer(data=request.data)
#
   #     if serializer.is_valid():
      #      serializer.save()

      #      return Response(
      #          {
   #                 "mensagem": "Pergunta salva com sucesso",
     #               "pergunta": serializer.data
      #          },
       #         status=status.HTTP_201_CREATED
        #    )

      #  return Response(
        #    serializer.errors,
        #    status=status.HTTP_400_BAD_REQUEST
      #  )
  
    # -------------------------
    # LISTAR CONVERSAS
    # -------------------------

    def list(self, request):

        conversas = Conversa.objects.all()

        serializer = ConversaSerializer(
            conversas,
            many=True
        )

        return Response(serializer.data)