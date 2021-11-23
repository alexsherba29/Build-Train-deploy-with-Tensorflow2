from flask import Flask, request, redirect, render_template
from werkzeug.utils import  secure_filename
import os
import tensorflow as tf
import numpy as np
import cv2


food_classes = ['bread', 'dairy_product', 'dessert', 'egg', 'fried_food', 'meat', 
                'noodles_pasta', 'rice', 'seafood', 'soup', 'vegetable or fruit']


app = Flask(__name__, static_url_path='/static')

app.config["IMAGE_UPLOADS"] = './static'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]


#food_prediction_model = tf.keras.models.load_model('./deeplearning_model')


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]  

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True

    else:
        return False


@app.route("/", methods=["GET", "POST"])
def upload_image() :

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":

                return redirect(request.url)

            
            if allowed_image(image.filename):

                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                return redirect(f'/showing-image/{filename}')

            else:
                return redirect(request.url)

    return render_template("upload_images.html")



@app.route("/showing-image/<image_name>", methods=["GET", "POST"])
def showing_image(image_name):

    if request.method == 'POST':

        pass
    

    return render_template("showing_image.html", value=image_name)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))



    


