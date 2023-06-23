from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load the pre-trained model
model = keras.models.load_model('./model_VGG16_2.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the image from the POST request
    image_file = request.files['image']

    # Preprocess the image
    image = Image.open(image_file)
    image = image.resize((224, 224))  # Resize the image to match the input size of the model
    image = np.array(image) / 255.0  # Normalize the pixel values
    image = np.expand_dims(image, axis=0)  # Add an extra dimension for batch size

    # Pass the preprocessed image to the model for prediction
    predictions = model.predict(image)

    # Get the predicted class
    predicted_class = np.argmax(predictions)

    # Return the prediction result
    class_names = ['class1', 'class2', 'class3']  # Replace with your own class names
    result = class_names[predicted_class]
    return result    

if __name__ == '__main__':
    app.run(debug=True)
    
