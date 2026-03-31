from django.db import models

# Create your models here.


from django.db import models


# -------------------------
# PERFIL DE ACESSO
# -------------------------

class PerfilAcesso(models.Model):
    descricao_perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao_perfil


# -------------------------
# USUARIO
# -------------------------

class Usuario(models.Model):

    perfil = models.ForeignKey(
        PerfilAcesso,
        on_delete=models.CASCADE
    )

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=255)

    data_cadastro = models.DateTimeField(auto_now_add=True)
    ultimo_acesso = models.DateTimeField(null=True, blank=True)

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