# Adapted from datarepresentation

from flask import Flask

from tensorflow import keras

# Load model
model = keras.models.load_model("model.h5")

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route("/")
def home():
  return app.send_static_file('index.html')

# Test with curl "http://127.0.0.1:5000/predict/11
@app.route('/predict/<int:x>', methods=['GET'])
@app.route('/predict/<float:x>', methods=['GET'])
def predict(x):
  prediction = model.predict([x])
  return str(prediction[0][0])

# Run in debug mode
if __name__ == "__main__":
   app.run(debug=True)
