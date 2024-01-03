# Configurações para coleta de imagens
IMAGE_COLLECTION = {
    "SEARCH_QUERY": "pug",
    "IMAGE_FOLDER": "data/downloaded_images",
    "IMAGE_SIZE": (224, 224),
    "IMAGE_LIMIT": 10
}

# Configurações para o modelo de aprendizado de máquina
MODEL_CONFIG = {
    "MODEL_SAVE_PATH": "models/pug.h5",
    "INPUT_SHAPE": (224, 224, 3),
    "NUM_CLASSES": 2,
    "LEARNING_RATE": 0.001,
    "EPOCHS": 10,
    "BATCH_SIZE": 32
}
