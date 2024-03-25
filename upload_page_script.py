"""
Upload page script
"""

from flask import Flask, request, render_template
#from trimmomatic import Trimmomatic
from fastqc import class_fastqc
ALLOWED_EXTENSIONS = {"txt","fastq"}

app = Flask(__name__)

def allowed_file(file):
    """
    function part of file uploading
    """
    return file.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def root():
    return render_template("homepage.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/uploadpage")
def uploadpage():
    return render_template("uploadpage.html")

@app.route("/fastqc")
def fastqc():
    return render_template("fastqc.html")

@app.route("/trimmomatic")
def trimmomatic():
    return render_template("trimmomatic.html")

@app.route("/contactpage")
def contactpage():
    return render_template("contactpage.html")

@app.route("/how_does_it_work")
def how_does_it_work():
    return render_template("how_does_it_work.html")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")

@app.route("/succes", methods=["post"])
def succes():
    """
    This function uploads a file to the file uploading directory

    Param: upload form in the upload html page
    Return: Confermation HTML page
    """
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            file_name = file.filename
            file.save("file_uploading/"+file.filename)

            # testing string to jinja code
            first_file_path = file_name.replace(".fastq", "_fastqc/")
            test_path = "../static/"+first_file_path+"Images/adapter_content.png"
            print(test_path)

            with open("file_uploading/"+file.filename, "r") as files:
                for line in files:
                    if line.startswith("@"):
                        file_name_fastqc = class_fastqc(file_name)
                        file_name_fastqc.run()
                        return render_template("succes_upload_page.html", name=file_name,test=test_path)
                    else:
                        return render_template("failed_upload_page.html", name=file_name)

        else:
            return render_template("failed_upload_page.html", name=file.filename)

@app.route("/options_page", methods=["GET", "POST"])
def options():
    if request.method == "GET": 
        return render_template("options_page.html")
    elif request.method == "POST":
        crop_value = request.form["crop"]
        minlen_value = request.form["minlen"]
        trim_object = Trimmomatic(minlen_value, crop_value, filename)
        trim_object.run_trimmomatic
        return render_template("options_page.html") #DIT MOET DE PAGINA WORDEN MET DE NIEUWE PLOTJES
