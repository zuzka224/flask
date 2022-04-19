from distutils.log import debug
from unicodedata import name
from PIL import Image
from random import randint
from flask import Flask, send_file, request, redirect, url_for, render_template, send_from_directory
from io import BytesIO
from ves import *
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

def serve_pil_image(img):
	img_io = BytesIO()
	img.save(img_io, 'JPEG', quality=70)
	img_io.seek(0)
	return send_file(img_io, mimetype='image/jpeg')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  """
    Tato funkcia bude odpovedat na vsetky ostatne HTTP poziadavky, pre ktore nemame specialnu funkciu. Bude hladat subory v priecinku public.
  """
  if (len(path) == 0):  # ak nezadany ziaden subor, teda cesta / chceme index.html
    return send_from_directory('public', 'index.html')

  return send_from_directory('public', path)


@app.route('/render', methods=['post'])
def render():
  """
    Tato funkcia dostane v HTTP poziadavke zdrojovy kod pre VES a pozadovanu sirku, vyrenderuje obrazok a vrati ho ako HTTP odpoved
  """
  ves = request.form.get(
      'ves')  # nacitanie hodnoty ktoru sme dostali v poziadavke
  # nacitanie hodnoty ktoru sme dostali v poziadavke
  width = request.form.get('width')
  print(ves)
  # img = render_ves(ves, width) # tu posleme VES riadky do funkcie render_ves z projektu z prvého polroka
  img = render_ves(ves, "img")
  return serve_pil_image(img)  # vratime vyrenderovany obrazok ako jpg




@app.route('/')
def home():
 return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)
