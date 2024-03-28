"""
Upload page script
"""
from flask import Flask, request, render_template, session
from trimmomatic import Trimmomatic
from fastqc import class_fastqc

ALLOWED_EXTENSIONS = {"fq","fastq"}
app = Flask(__name__)
app.secret_key = "TRIMTASTISCHE_TIJGERS"

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
            session["filename"] = file.filename
            session["path_folder"] =  file.filename.replace(".fastq", "_fastqc/")

            file.save("file_uploading\\"+file.filename)

            with open("file_uploading/"+file.filename, "r") as files:

                for line in files:

                    if line.startswith("@"):
                        file_name_fastqc = class_fastqc(file.filename)
                        file_name_fastqc.run(r"\file_uploading")
                        return render_template("succes_upload_page.html", name=session["filename"],original=session["path_folder"])

                    else:
                        return render_template("failed_upload_page.html", name=session["filename"])

        else:
            return render_template("failed_upload_page.html", name=file.filename)

@app.route("/options_page", methods=["GET", "POST"])
def options():

    if request.method == "POST":
        crop_value = request.form["crop"]
        minlen_value = request.form["minlen"]
        sliding_show = request.form["sliding"]


        trim_object = Trimmomatic(sliding_show, minlen_value, crop_value, session["filename"])
        trim_object.run_trimmomatic()

        trim_output_file = class_fastqc("OUTPUT.fq")
        trim_output_file.run(r"\trimmomatic_output")
        compare_path = "OUTPUT_fastqc/"
        return render_template("compare.html", original=session["path_folder"], compare=compare_path)

    if request.method == "GET":
        return render_template("options_page.html")
