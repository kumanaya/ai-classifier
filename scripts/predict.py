import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Carregue o modelo treinado
model = tf.keras.models.load_model('models/pug.h5')

# Função para prever se a imagem é uma pizza de muçarela
def predict(image_path):
    # Carregue a imagem e redimensione para o tamanho esperado pelo modelo
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    
    # Normalize a imagem
    img /= 255.0
    
    # Faça a previsão usando o modelo
    prediction = model.predict(img)
    
    # Converta a previsão em uma resposta (por exemplo, "É pizza de muçarela" ou "Não é pizza de muçarela")
    if prediction[0][0] > 0.5:
        return "É um pug"
    else:
        return "Não é um pug"

# Caminho para a imagem que você deseja testar
image_path = 'data/test/pug/0.jpg'

# Faça a previsão
result = predict(image_path)
print(result)
