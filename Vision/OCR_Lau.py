import os
from PIL import Image
from pdf2image import convert_from_path

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import JsonOutputParser


archivo_pdf = "/home/juanfe/GitHub/Docs/Vision/NOTA DE COBERTURA NIT 900231393 ALSAR INDUSTRIAL SAS 2024-2025.pdf"
imagenes = convert_from_path(pdf_path=archivo_pdf, first_page=1, last_page=1)

for i, imagen in enumerate(imagenes):
    imagen.save(f"/home/juanfe/GitHub/Docs/Vision/imagen_{i + 1}.jpg", "JPEG")



os.environ["GOOGLE_API_KEY"] = ""
llm = ChatGoogleGenerativeAI(model="gemini-pro-vision", temperature=0.0)
parser = JsonOutputParser()
chain =  llm | parser





def img_processing(imagen, prompt):

    hmessage = HumanMessage(
        content=[
            {
                "type": "text",
                "text": prompt,
            },
            {"type": "image_url", "image_url": imagen},
        ]
    )

    result = chain.invoke([hmessage])
    return result



img = Image.open('/home/juanfe/GitHub/Docs/Vision/imagen_1.jpg')


prompt = """
Eres un analista de seguros.
Recibiras una imagen de una nota de un clausulado de un seguro.
Allí encontraras una tabla donde estan las coberturas y los topes de cada cobertura (montos de dinero en pesos colombianos).
Quiero que conviertas esta tabla donde se ecnuentran las coberturas en un json.
Donde cada tag del json es una cobertura (fila) y el valor es el texto del tope (valor asegurable, el intervalo que te indica el archivo)
"""


result = img_processing(img, prompt)

result


{
    'nit':"",
    "coberturas": {
        "...":"..."
    }
}