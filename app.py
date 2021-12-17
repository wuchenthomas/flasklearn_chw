import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, send_file, session, url_for
from werkzeug.utils import secure_filename
import tablib
from testMaker import test5

# UPLOAD_FOLDER = 'static'
#
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route("/preview", methods=['POST', 'GET'])
# def preview():
#     dataset = tablib.Dataset()
#     if request.method == 'POST':
#         f1 = request.form['csvfile1']
#         print(f1)
#         return dataset.html
#         # return redirect(url_for('dashboard', csv=f1))
#
#
# @app.route("/dashboard/<csv>")
# def dashboard(csv):
#     dataset = tablib.Dataset()
#     with open(csv) as f:
#         dataset.csv = f.read()
#         return dataset.html


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    print('\\data')
    # if request.method == 'POST':
    print('\\data.post')
    f1 = request.files['csvfile1']
    print('f1')
    f2 = request.files['csvfile2']
    print('f2')
    ly1 = request.form['Layer1']
    ly2 = request.form['Layer2']
    RN1 = int(request.form['RFFE_Nr1'])
    RN2 = int(request.form['RFFE_Nr2'])
    LyNr1 = int(request.form['Layer_Nr1'])
    LyNr2 = int(request.form['Layer_Nr2'])
    Sh1 = int(request.form['skip_header_row1'])
    Sh2 = int(request.form['skip_header_row2'])
    data = test5(f1, f2, ly1, ly2, skip_header1=Sh1, skip_header2=Sh2, Layer_col1=LyNr1, Layer_col2=LyNr2,
                 RFFE_Nr1=RN1, RFFE_Nr2=RN2)
    print(data)
    return render_template('data.html', data=data)


# @app.route('/test2', methods=['GET', 'POST'])
# def dropdown():
#     # colours = ['Red', 'Blue', 'Black', 'Orange']
#     return render_template('test2.html')


@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# @app.route('/print', methods=['GET', 'POST'])
# def print():
#     slt_value = request.form.get('colour')
#     return str(slt_value)
#
#
# @app.route('/uploads/<name>', methods=['GET', 'POST'])
# def download_file(name):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)
