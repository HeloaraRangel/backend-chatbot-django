from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


from chatbot.models import Chunk

# modelo de embedding
modelo = SentenceTransformer('all-MiniLM-L6-v2')


# Extrair texto do PDF
def extrair_texto_pdf(caminho_pdf):

    reader = PdfReader(caminho_pdf)

    texto = ""

    for pagina in reader.pages:

        conteudo = pagina.extract_text()

        if conteudo:
            texto += conteudo

    return texto


# Dividir texto em chunks
def dividir_chunks(texto, tamanho=400):

    lista_chunks = []

    for i in range(0, len(texto), tamanho):

        parte = texto[i:i+tamanho]

        lista_chunks.append(parte)

    print("Total de chunks:", len(lista_chunks))

    return lista_chunks



# 🧠 Pipeline completo
def processar_documento(documento):

    print("Processando documento...")

    caminho_pdf = documento.arquivo.path

    texto = extrair_texto_pdf(caminho_pdf)

    lista_chunks = dividir_chunks(texto)

    vetores = modelo.encode(lista_chunks)

    for i, chunk_texto in enumerate(lista_chunks):

        Chunk.objects.create(
            conteudo=chunk_texto,
            ordem=i,
            documento=documento,
            vetor=vetores[i].tolist()
        )

    print("Documento vetorizado com sucesso!")