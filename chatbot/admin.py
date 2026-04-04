from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import (
    Usuario,
    PerfilDeAcesso,
    Pergunta,
    Resposta,
    Conversa,
    Categoria,
    Documento,
    CategoriaDocumento
)

admin.site.register(Usuario)
admin.site.register(PerfilDeAcesso)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Conversa)
admin.site.register(Categoria)
admin.site.register(Documento)
admin.site.register(CategoriaDocumento)