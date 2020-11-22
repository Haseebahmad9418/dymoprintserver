from flask import *
import os
app = Flask(__name__)  
uploadfolder="/home/pi/queue"
i=0
@app.route('/piFileUpload') 
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST']) 
def success():
    global i
    if (request.method == 'POST'):
        f = request.files['file']
        path=uploadfolder+"/"+f.filename
        print(path)
        if(os.path.isfile(path)):
            s=str(i)+f.filename
            print(s)
            i+=1
            f.save(os.path.join(uploadfolder,s))
            return render_template("success.html", name = s)
        else:
            print("running else bock")
            f.save(os.path.join(uploadfolder,f.filename))
            return render_template("success.html", name = f.filename)

@app.route("/piQueueLength",methods=['GET'])
def hello_name():
    list=[]
    listdir=os.listdir(uploadfolder)
    l1=len(listdir)
    return jsonify({"Queue length":l1})

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug = True)