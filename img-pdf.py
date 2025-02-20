from PIL import Image
import os

def images_to_pdf(folder_path, output_folder, output_pdf_name ,width):
     # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Ruta completa del PDF de salida
    output_pdf = os.path.join(output_folder, output_pdf_name)
    # Obtener lista de archivos en la carpeta
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Ordenar archivos por su nombre numérico
    files.sort(key=lambda f: int(os.path.splitext(f)[0]))

    # Cargar imágenes
    image_list = []
    for file in files:
        img_path = os.path.join(folder_path, file)
        img = Image.open(img_path).convert("RGB")  # Convertir a RGB para compatibilidad con PDF
        # Ajustar el ancho manteniendo la relación de aspecto
        w_percent = width / float(img.size[0])  # Relación de escala
        new_height = int(float(img.size[1]) * w_percent)  # Escalar la altura proporcionalmente
        img_resized = img.resize((width, new_height), Image.LANCZOS)
        
        image_list.append(img_resized)

    # Guardar como PDF
    if image_list:
        image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])
        print(f"PDF guardado como: {output_pdf}")
    else:
        print("No se encontraron imágenes en la carpeta.")

def check_pdf(cad: str) -> str:
    if cad[-4:] != ".pdf":
        cad = cad + ".pdf"
        return cad
    else:
        return cad

# 📂 Parámetros
carpeta = "img"
ancho_fijo = 800
carpeta_doc = "doc"

nombre_pdf = input("Que nombre quieres para el documento pdf: ")
nombre_pdf = check_pdf(nombre_pdf)

images_to_pdf(carpeta, carpeta_doc, nombre_pdf,ancho_fijo)