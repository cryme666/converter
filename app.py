from flask import Flask, render_template, request, send_file
import os,convertor

app = Flask('Convertor')

ALLOWED_EXTENSIONS = ['xlsx','csv','txt','jpg','png']
UPLOADER_FOLDER = convertor.FOLDER
app.config['UPLOADER_FOLDER'] = UPLOADER_FOLDER
app.secret_key = '1234567890'

def clear_files(folder_path):
    for filename in os.listdir(folder_path):
        try:
            file_path = os.path.join(folder_path,filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete. Reason: {e}") 




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods = ['POST','GET'])
def submit():
    clear_files(app.config['UPLOADER_FOLDER'])
    file = request.files['file']
    conversion_type = request.form['conversion']
    
    file_extension = file.filename.split('.')[1]
    
    if file_extension not in ALLOWED_EXTENSIONS:
        return 'Our programm dont support your file'


    if conversion_type == 'excel_to_csv' and file_extension != "xlsx":
        return "For convertation you need to paste .xlsx file"
    elif conversion_type == "csv_to_excel" and file_extension != "csv":
        return "For convertation you need to paste .csv file"
    elif conversion_type == "txt_to_pdf" and file_extension != "txt":
        return "For convertation you need to paste .txt file"
    elif conversion_type == "jpg_to_png" and file_extension != "jpg":
        return "For convertation you need to paste .txt file"
    elif conversion_type == "png_to_jpg" and file_extension != "png":
        return "For convertation you need to paste .png file"


    file_path = os.path.join(app.config['UPLOADER_FOLDER'],file.filename)
    file.save(file_path)

    if conversion_type == "jpg_to_png":
        converted_filename = convertor.jpg_to_png(file_path)
    elif conversion_type == "excel_to_csv":
        converted_filename = convertor.excel_to_csv(file_path)
    elif conversion_type == "csv_to_excel":
        converted_filename = convertor.csv_to_excel(file_path)
    elif conversion_type == "txt_to_pdf":
        converted_filename = convertor.txt_to_pdf(file_path)
    elif conversion_type == "png_to_jpg":
        converted_filename = convertor.png_to_jpg(file_path)


    return send_file(converted_filename, as_attachment=True)



app.run(debug=True)