import cv2
import numpy as np

# Carregar a imagem 'teste.jpg'
image = cv2.imread('imgs/teste.jpg')

def segment_color(image, lower_bound, upper_bound):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# Definir os limites para a cor roxa, roxo claro e roxo escuro
lower_purple_light = np.array([130, 50, 50])    # Limite inferior para roxo claro
upper_purple_light = np.array([160, 255, 255])   # Limite superior para roxo claro

lower_purple_dark = np.array([125, 50, 50])     # Limite inferior para roxo escuro
upper_purple_dark = np.array([130, 255, 255])    # Limite superior para roxo escuro

lower_magenta = np.array([140, 50, 50])          # Limite inferior para magenta
upper_magenta = np.array([160, 255, 255])         # Limite superior para magenta

lower_lilac = np.array([125, 50, 70])             # Limite inferior para lilás
upper_lilac = np.array([140, 255, 255])           # Limite superior para lilás

# Aplicar a segmentação das cores
mask_light = segment_color(image, lower_purple_light, upper_purple_light)
mask_dark = segment_color(image, lower_purple_dark, upper_purple_dark)

# Combinar as máscaras
segmented_image = cv2.bitwise_or(mask_light, mask_dark)

# Salvar a imagem resultante na pasta imgs
cv2.imwrite('imgs/resultado_roxo.jpg', segmented_image)

# Exibir as imagens
cv2.imshow('Original', image)
cv2.imshow('Segmented', segmented_image)

# Aguardar até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()
