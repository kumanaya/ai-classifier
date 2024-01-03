import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configurações do modelo
MODEL_SAVE_PATH = "models/pug.h5"
INPUT_SHAPE = (224, 224, 3)
NUM_CLASSES = 2
LEARNING_RATE = 0.001
EPOCHS = 10
BATCH_SIZE = 32
TRAIN_DATA_DIR = "data/train"  # Diretório de treinamento

def build_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    return model

def main():
    model = build_model(INPUT_SHAPE, NUM_CLASSES)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Configurar o gerador de imagens para treinamento
    train_datagen = ImageDataGenerator(rescale=1./255)

    # Carregar dados de treinamento
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DATA_DIR,
        target_size=INPUT_SHAPE[:2],
        batch_size=BATCH_SIZE,
        class_mode='sparse')  # Use 'sparse' se estiver usando rótulos numéricos

    # Treinar o modelo
    model.fit(train_generator, epochs=EPOCHS)

    # Salvar o modelo
    model.save(MODEL_SAVE_PATH)

if __name__ == "__main__":
    main()
