import cv2
import pytesseract
import PIL
import os
import re

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
        self.cartidge_type = ''
        
        
    def extract_cartidge_type(self):
        cartidge_type = Classifier.get_cartidge_type(self.img_txt)
        self.cartidge_type = cartidge_type
        
        
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
            '\ntype:', self.cartidge_type,
            '\n'
            )
    
    
class Classifier:
    def get_cartidge_type(label_txt):
        """Obtém o tipo do cartucho, a partir de texto do rótulo

        Args:
            label_txt (str): texto do rótulo do cartucho

        Returns:
            cartridge_type (str): tipo do cartucho
        """
        cartridge_type = ''
        
        if Classifier.is_type_664(label_txt):
            cartridge_type = '664'
        elif Classifier.is_type_667(label_txt):
            cartridge_type = '667'
        elif Classifier.is_type_57(label_txt):
            cartridge_type = '57'
        
        return cartridge_type
    
    
    def is_type_664(label_txt):
        """Verifica se cartucho é do tipo 664

        Args:
            label_txt (str): texto do rótulo do cartucho

        Returns:
            bool: veredito; verdadeiro, se o cartucho é desse tipo, e falso, caso contrário
        """
        match_label = re.search('664', label_txt)
        
        if match_label:
            return True

        return False
    
    
    def is_type_667(label_txt):
        """Verifica se cartucho é do tipo 667

        Args:
            label_txt (str): texto do rótulo do cartucho

        Returns:
            bool: veredito; verdadeiro, se o cartucho é desse tipo, e falso, caso contrário
        """
        match_label = re.search('667', label_txt)
        
        if match_label:
            return True

        return False
        
        
    def is_type_57(label_txt):
        """Verifica se cartucho é do tipo 57

        Args:
            label_txt (str): texto do rótulo do cartucho

        Returns:
            bool: veredito; verdadeiro, se o cartucho é desse tipo, e falso, caso contrário
        """
        match_label = re.search('57', label_txt)
        
        if match_label:
            return True

        return False


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