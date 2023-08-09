import streamlit as st
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'
# Titre de l'application
st.title("ImageTextify: Convertisseur de Texte à partir d'Images")

# Téléchargement de l'image
image = st.file_uploader("Téléchargez une image contenant du texte", type=["jpg", "png", "jpeg"])

# Bouton pour extraire le texte
if st.button("Extraire le texte"):
    if image is not None:
        # Lecture de l'image avec PIL
        img = Image.open(image)

        # Utilisation de Tesseract pour extraire le texte
        extracted_text = pytesseract.image_to_string(img)

        # Affichage du texte extrait
        st.subheader("Texte extrait de l'image :")
        st.code(extracted_text, language="text")
    else:
        st.warning("Veuillez télécharger une image.")
