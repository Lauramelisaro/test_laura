import google.generativeai as genai
import PIL.Image


genai.configure(api_key="")

model = genai.GenerativeModel("gemini-pro-vision")
img = PIL.Image.open('/home/juanfe/Pruebas/Vision/image.jpg')

# response = model.generate_content(img)

# response.text


response = model.generate_content(["Que hay en esta imagen", img], stream=True)
response.resolve()
response.text