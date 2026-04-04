from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# -------------------------
# PERFIL DE ACESSO
# -------------------------

class PerfilDeAcesso(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    descricao_perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao_perfil


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        PerfilDeAcesso,
        on_delete=models.CASCADE,
        related_name="usuarios"
    )

    nome = models.CharField(max_length=100)

    email = models.EmailField(
        max_length=150,
        unique=True
    )

    senha = models.CharField(max_length=255)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    ultimo_acesso = models.DateTimeField(
        null=True,
        blank=True
    )

    def set_senha(self, senha):
        self.senha = make_password(senha)

    def check_senha(self, senha):
        return check_password(senha, self.senha)

    def __str__(self):
        return self.nome

# -------------------------
# PERGUNTA
# -------------------------

class Pergunta(models.Model):

    descricao_pergunta = models.TextField()

    def __str__(self):
        return self.descricao_pergunta[:50]


# -------------------------
# RESPOSTA
# -------------------------

class Resposta(models.Model):

    intencao = models.CharField(max_length=100)
    tempo_resposta = models.DurationField()

    def __str__(self):
        return self.intencao


# -------------------------
# CONVERSA
# -------------------------

class Conversa(models.Model):

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    pergunta = models.ForeignKey(
        Pergunta,
        on_delete=models.SET_NULL,
        null=True
    )

    resposta = models.ForeignKey(
        Resposta,
        on_delete=models.SET_NULL,
        null=True
    )

    data_conversa = models.DateField()
    horario_conversa = models.TimeField()

    avaliacao = models.BooleanField(default=False)

    def __str__(self):
        return f"Conversa {self.id}"


# -------------------------
# CATEGORIA
# -------------------------

class Categoria(models.Model):

    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria


# -------------------------
# DOCUMENTO
# -------------------------

#class Documento(models.Model):

 #   data_insercao = models.DateTimeField(auto_now_add=True)

  #  categorias = models.ManyToManyField(
  #      Categoria,
  #      through='CategoriaDocumento'
 #   )

  #  def __str__(self):
  #      return f"Documento {self.id}"
    
class Documento(models.Model):
    nome = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    arquivo = models.FileField(
        upload_to="documentos/",
        null=True,
        blank=True
    )

    data_insercao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome if self.nome else f"Documento {self.id}"

# -------------------------
# RELAÇÃO DOCUMENTO-CATEGORIA
# -------------------------

class CategoriaDocumento(models.Model):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE
    )