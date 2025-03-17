from flask import Flask, render_template, request, send_file
import os,convertor

app = Flask('Convertor')

ALLOWED_EXTENSIONS = ['pdf','docx','txt','jpg','png']
UPLOADER_FOLDER = convertor.FOLDER
app.config['UPLOADER_FOLDER'] = UPLOADER_FOLDER
app.secret_key = '1234567890'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods = ['POST','GET'])
def submit():
    file = request.files['file']
    conversion_type = request.form['conversion']
    
    file_extension = file.filename.split('.')[1]
    
    if file_extension not in ALLOWED_EXTENSIONS:
        return 'Our programm dont support your file'


    if conversion_type == 'pdf_to_word' and file_extension != "pdf":
        return "For convertation you need to paste .pdf file"
    elif conversion_type == "word_to_pdf" and file_extension != "docx":
        return "For convertation you need to paste .docx file"
    # todo дописати і інші розширення

    file_path = os.path.join(app.config['UPLOADER_FOLDER'],file.filename)
    file.save(file_path)

    if conversion_type == "jpg_to_png":
        converted_filename = convertor.jpg_to_png(file_path)
    # todo дописати і інші розширення

    return send_file(converted_filename, as_attachment=True)


app.run(debug=True)