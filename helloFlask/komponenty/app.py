from distutils.log import debug
from unicodedata import name
from PIL import Image
from random import randint
from flask import Flask, send_file, request, redirect, url_for, render_template
from io import BytesIO
app = Flask(__name__)



def serve_pil_image(img):
	img_io = BytesIO()
	img.save(img_io, 'JPEG', quality=70)
	img_io.seek(0)
	return send_file(img_io, mimetype='image/jpeg')



@app.route('/')
def home():
 return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)
