# app/api/search.py
from flask import Blueprint, jsonify, request, render_template
from werkzeug.utils import secure_filename

import os
from app import db, config
from app.schema import Image

images_blueprint = Blueprint('images', __name__)

@images_blueprint.route('/', methods=['GET'])
def get_images():
    images = Image.query.all()
    images = [image.to_dict() for image in images]
    images = sorted(images, key=lambda k: k['created_at'], reverse=True) 
    return render_template("index.html", images=images)

@images_blueprint.route('/', methods=['POST'])
def create_image():

    _file = request.files['image']
    print('username')
    username = request.form.get('username')
    if username is None:
        return jsonify({"error": "username needs to be provided"}), 403

    filename = secure_filename(_file.filename)
    filepath_write = os.path.join(config.BaseConfig.UPLOAD_FOLDER, filename)
    filepath_read = os.path.join(config.BaseConfig.VIEW_FOLDER, filename)
    _file.save(filepath_write)

    image = Image(filepath_read, request.form['username'])
    image.save()
    db.session.commit()

    images = Image.query.all()
    return jsonify({
        "images": [image.to_dict() for image in images]
    })
