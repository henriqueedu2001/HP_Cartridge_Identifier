import os
import src.cartridge_classifier as cartridge_classifier

def start_app():
    """inicializa a aplicação"""
    print("--- HP_Cartridge_Identifier ---")
    print("Escola Politécnica da USP")
    classify_test()
    

def classify_test():
    imgs_path = [
        'assets/samples/01.jpeg',
        'assets/samples/02.jpeg',
        'assets/samples/03.jpeg',
        'assets/samples/04.jpeg'
    ]
    
    # obtenção das imagens em formato np.array
    imgs = [cartridge_classifier.CartridgeImage(img_path) for img_path in imgs_path]
    
    # extração do texto de cada imagem
    for img in imgs: img.extract_text()
    
    # texto de cada imagem
    for img in imgs: img.resume()
    
start_app()