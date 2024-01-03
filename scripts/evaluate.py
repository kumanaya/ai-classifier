import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configurações para avaliação do modelo
MODEL_PATH = "models/pug.h5"
TEST_DATA_DIR = "data/test"  # Caminho para seus dados de teste
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def evaluate_model(model, test_data_dir, image_size, batch_size):
    test_datagen = ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(
        test_data_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='sparse')  # Use 'sparse' se estiver usando rótulos numéricos

    loss, accuracy = model.evaluate(test_generator)
    return loss, accuracy

def main():
    model = load_model(MODEL_PATH)

    # Configurar o gerador de imagens para teste
    test_datagen = ImageDataGenerator(rescale=1./255)

    # Carregar dados de teste
    test_generator = test_datagen.flow_from_directory(
        TEST_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='sparse')  # Use 'sparse' se estiver usando rótulos numéricos

    # Avaliar o modelo
    loss, accuracy = evaluate_model(model, TEST_DATA_DIR, IMAGE_SIZE, BATCH_SIZE)
    print(f"Test Loss: {loss}")
    print(f"Test Accuracy: {accuracy}")

if __name__ == "__main__":
    main()
