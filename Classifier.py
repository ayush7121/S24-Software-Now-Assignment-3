import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Base class 1: GUI for handling Tkinter application
class GUIBase:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Classifier")
        self.root.geometry("500x500")

    def display_message(self, message):
        label = Label(self.root, text=message)
        label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        return file_path

# Base class 2: AI model handler
class ModelHandler:
    def __init__(self, model_path):
        self._model = None  # Initialize as None; actual model is loaded lazily
        self.model_path = model_path
    
    # Encapsulation: Using a property to control access to the model
    @property
    def model(self):
        if self._model is None:
            # Lazy loading of the model
            self._model = tf.keras.applications.MobileNetV2(weights='imagenet')
        return self._model

    def preprocess_image(self, img_path):
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        return img_array

    def predict_image(self, img_array):
        preds = self.model.predict(img_array)  # Using property decorator here
        decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0]
        return decoded_preds[0][1]  # Return the label of the top prediction

# Derived class that uses multiple inheritance from GUIBase and ModelHandler
class ImageClassifierApp(GUIBase, ModelHandler):
    def __init__(self, root, model_path):
        # Multiple inheritance: Initialize both GUIBase and ModelHandler
        GUIBase.__init__(self, root)
        ModelHandler.__init__(self, model_path)
        
        # Adding UI Elements
        self.display_message("Welcome to Image Classifier")
        self.upload_button = tk.Button(root, text="Upload Image", command=self.load_image)
        self.upload_button.pack()

        self.result_label = Label(root, text="Upload an image to classify.")
        self.result_label.pack()

    def load_image(self):
        file_path = self.upload_image()  # GUIBase method
        if file_path:
            img_array = self.preprocess_image(file_path)  # ModelHandler method
            result = self.predict_image(img_array)  # Method overriding example: predict_image behavior can be modified
            self.result_label.config(text=f"Prediction: {result}")

# Main function to run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageClassifierApp(root, model_path=None)  # Polymorphism: different behavior for different classes
    root.mainloop()
