PROJECT_ID = "sb-prototipos-xops"
REGION = "us-central1"
INSTANCE = "motor-coberturas"
DATABASE = "postgres"
TABLE_NAME = "vector_store_demo_cv"
DB_USER = "postgres"
DB_PASSWORD = "motor-coberturas"

import uuid
import asyncio


from google.cloud import aiplatform
aiplatform.init(project=PROJECT_ID, location=REGION)


from langchain_google_cloud_sql_pg import PostgresEngine 
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_cloud_sql_pg import PostgresVectorStore
from langchain_google_cloud_sql_pg.indexes import IVFFlatIndex
from langchain.chains import RetrievalQA
from langchain_google_vertexai import VertexAI


#! CAMBIAR A VERSION ESTABLE Y FIJA


llm = VertexAI(model_name="gemini-pro")
embedding = VertexAIEmbeddings(
    model_name="textembedding-gecko@latest", project=PROJECT_ID
)

# Conexión
engine = PostgresEngine.from_instance(
        project_id=PROJECT_ID, 
        region=REGION, 
        instance=INSTANCE, 
        database=DATABASE, 
        user=DB_USER, 
        password=DB_PASSWORD
    )

# Creación de tabla #! NO CORRER SI YA EXISTE
engine.init_vectorstore_table(
    table_name=TABLE_NAME,
    vector_size=768,
)

# Conexión a la VS y su respectiva calibración con el modelo de embeddings
store = PostgresVectorStore.create_sync(
    engine=engine,
    table_name=TABLE_NAME,
    embedding_service=embedding,
)



# Ingestar los textos con id único, metadata y calculo de los embeddings
all_texts = [
    """NATALIA HERNANDEZ Tipo: estudios, Texto: Pregrado en Matemáticas Universidad de los Andes 2017-2022 Opción en Matemática Computacional Universidad de los Andes 2017-2022, Valor: 
    Tipo: estudios, Texto: Diplomado en Inteligencia Artificial Universidad del Rosario 2022, Valor: 
    Tipo: estudios, Texto: Bootcamp en Ciencia de Datos Make it Real 2021, Valor: 
    Tipo: estudios, Texto: Bootcamp en Desarrollo de aplicaciones móviles Keepcoding 2023-2024 Opción en Lengua y Cultura Portuguesa Universidad de los Andes 2017-2022""", 
    """CARLOS SANTIAGO VANEGAS Tipo: estudios, Texto: PREGRADO EN INGENIERÍA MECATRÓNICA Universidad Militar Nueva Granada 2016 Presente Bogotá, Colombia
    Tipo: estudios, Texto: BACHILLER ACADÉMICO Institución Educativa San José de Orito 2005-2015 Orito, Putumayo, COL."""
    ]
metadatas = [{"len": len(t)} for t in all_texts]
ids = [str(uuid.uuid4()) for _ in all_texts]
store.add_texts(all_texts, metadatas=metadatas, ids=ids)


# Query por similaridad
query = "Natalia"
docs = store.similarity_search(query)
print(docs)

# Query por similaridad del vector
query_vector = embedding.embed_query(query)
docs = store.similarity_search_by_vector(query_vector, k=2)
print(docs)

# # Ingesta de un solo registro
# txt = 'Habia una vez una iguana, que tenia cara de rana'
# store.add_texts([txt], metadatas=[{"len":len(txt)}], ids=[str(uuid.uuid4())])





# Instanciar el retriever
retriever = store.as_retriever(search_kwargs={'k': 1})
query = "Natalia?"
retriever.get_relevant_documents(query)




# Tener una serie de retrievers en diferentes bases
# Retriever de resumen
# Retriever de herramientas
# Retriever educación


# Augmentation
# Reranking


# Generate (responder y dar un resum de la hoja de vida)



# Cadena de RAG Basico
qa_stuff = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=retriever,
    verbose=True,
)

query = "Que estudio NAtalia?, responde en español"

qa_stuff.run(query)