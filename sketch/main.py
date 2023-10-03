import cv2
import pytesseract
import PIL

def get_imgs_path():
    img_1 = 'samples/01.jpeg'
    img_2 = 'samples/02.jpeg'
    img_3 = 'samples/03.jpeg'
    img_4 = 'samples/04.jpeg'
    
    return [
        img_1,
        img_2,
        img_3,
        img_4
    ]
    
def read_imgs(imgs_path):
    imgs = []
    
    for img_path in imgs_path:
        img = cv2.imread(img_path)
        imgs.append(img)
        
    return imgs

def show_img(img):
    cv2.imshow('imagem', img)
    cv2.waitKey(0)
    

def apply_contrast_mask(img):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retrval, img_out = cv2.threshold(grayscale, 55, 255, cv2.THRESH_BINARY)
    
    return img_out

def get_text(img_path):
    my_config = r"--psm 6 --oem 3"
    img_text = pytesseract.image_to_string(PIL.Image.open(img_path), config = my_config)
    
    return img_text

def start_app():
    imgs_path = get_imgs_path()
    for img in imgs_path:
        print(get_text(img))
    

def test():
    imgs_path = get_imgs_path()
    imgs = read_imgs(imgs_path)
    
    c = 1
    
    for img in imgs:
        black_white_img = apply_contrast_mask(img)
        cv2.imwrite(str(c) + '.jpg', black_white_img)
        c = c + 1

start_app()