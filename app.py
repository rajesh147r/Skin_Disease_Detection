from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.layers import Rescaling
from PIL import Image
import numpy as np

app = Flask(__name__)


model = load_model('./best_model (7).keras')


img_classes = ['Enfeksiyonel', 'Ekzama', 'Akne', 'Pigment', 'Benign', 'Malign']


IMG_SIZE = (400, 400)

def prepare_image(image):
    """Prepare the image for the model by resizing, rescaling, and expanding dimensions."""
    image = image.convert("RGB").resize(IMG_SIZE)
    image = img_to_array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            image = prepare_image(Image.open(file))
            predictions = model.predict(image)
            predicted_class = img_classes[np.argmax(predictions)]
            prediction = f"Predicted Disease: {predicted_class}"
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
