from rest_framework import serializers
from .models import Documento
from .models import Pergunta
from .models import Conversa
from .models import PerfilDeAcesso
from .models import Usuario

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ['id', 'nome', 'arquivo', 'data_insercao']
        

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilDeAcesso
        fields = '__all__'
        

class UsuarioSerializer(serializers.ModelSerializer):

    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'perfil',
            'nome',
            'email',
            'senha',
            'data_cadastro',
            'ultimo_acesso'
        ]

        read_only_fields = [
            'data_cadastro',
            'ultimo_acesso'
        ]

    def create(self, validated_data):
        senha = validated_data.pop("senha")

        usuario = Usuario(**validated_data)
        usuario.set_senha(senha)
        usuario.save()

        return usuario



class PerguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pergunta
        fields = '__all__' 

class ConversaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversa
        fields = '__all__'       
        
        
        