from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


app.config['UPLOADS'] = '/home/kali/Desktop/vishnu/cyber_forensics/backend/static/uploads'
app.config['ALLOWED_FILE_EXTENTIONS'] = ['txt','pcap'] #list of extentions allowed.


def allowed_file(filename):
   print(filename)

   if filename == '':
      return False

   if not '.' in filename:
      return False
   
   ext = filename.split(".")[-1]
   if ext.lower() in app.config['ALLOWED_FILE_EXTENTIONS']:
      return True

   return False




def allowed_file_size(size):
   # max size allowed in 1000MB

   if 'mb' in size.lower() and int(size[:-2].split('.')[0])+1>1000:
      return False
   
   return True



@app.route('/upload', methods = ['GET','POST'])
def upload_file_home():
   if request.method == 'POST':
      f = request.files['file']

      if not allowed_file(f.filename):
         print("Given file extention is not supported.")
         return redirect(request.url)

      if not allowed_file_size(request.cookies['filesize']):
         print("File size limit exeeded.")
         return redirect(request.url)

      fname = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOADS'], fname))
      print("File saved.")

      return redirect(request.url)
   return render_template('upload.html')

		
if __name__ == '__main__':
   app.run(debug = True)