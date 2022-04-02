from PIL import Image
from random import randint
from flask import Flask, send_file, request
from io import BytesIO
app = Flask(__name__)



def serve_pil_image(img):
	img_io = BytesIO()
	img.save(img_io, 'JPEG', quality=70)
	img_io.seek(0)
	return send_file(img_io, mimetype='image/jpeg')


zakladna_stranka = """
<!DOCTYPE html>
<html>
<head>
	<title>Vector Script GUI</title>

	<link rel="stylesheet" type="text/css" href="style.css">


	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.css"
		integrity="sha256-46qynGAkLSFpVbEBog43gvNhfrOj+BmwXdxFgVK/Kvc=" crossorigin="anonymous" />
</head>
<body>
<header id="header">VECTOR SCRIPT GUI</header>
<section id="form_text">
	<form method="POST" action="/render">
		
		<textarea name="ves"></textarea>
		<button class="btn">Zobraziť</button>
	</form>
</section>
<section>
	<img id="output" />
</section>
<script type="text/javascript" src="script.js" ></script>
</body>
</html>
"""



@app.route('/', methods=['GET', 'POST'])
def base():
 return zakladna_stranka

base()
