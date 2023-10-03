import cv2
import pytesseract
import PIL
import os

# configuração do PIL para OCR
PIL_CONFIG = r"--psm 6 --oem 3"

class CartridgeImage:
    def __init__(self, img_path) -> None:
        """Construtor do objeto CartridgeImage, correspondente a uma imagem de cartucho

        Args:
            img_path: diretório da imagem
        """
        self.img_path = img_path
        self.img_id = get_file_name(img_path)
        self.img = get_img(img_path)
        self.img_txt = ''
        
        
    def extract_text(self):
        """Extrai o texto da imagem do cartucho
        """
        txt = get_text(self.img)
        self.img_txt = txt
    
    
    def resume(self):
        """resume o objeto em seus atributos
        """
        print(
            'id:', self.img_id,
            '\npath:', self.img_path,
            '\ntext:', self.img_txt,
            '\n'
            )
    

def get_text(img):
    """_summary_

    Args:
        img: imagem, em formato de np.array do open cv

    Returns:
        img_text: texto da imagem correspondente
    """
    img_text = pytesseract.image_to_string(img)
    
    return img_text


def get_img(img_path):
    """Obtém a imagem em formato de np.array, a partir de seu diretório

    Args:
        img_path: caminho/diretório da imagem

    Returns:
        img: imagem dem formato de np.array
    """
    img = cv2.imread(img_path)
    
    return img


def get_file_name(file_path):
    """Obtém o nome do arquivo

    Args:
        file_path: diretório do arquivo

    Returns:
        file_name: nome do arquivo
    """
    file_name_plus_extension = os.path.basename(file_path)
    file_name = os.path.splitext(file_name_plus_extension)[0]
    
    return file_name