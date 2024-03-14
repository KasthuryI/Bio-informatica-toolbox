"""
Upload page script
"""
from flask import Flask, request, render_template


app = Flask(__name__)


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
        f = request.files["file"]
        f.save("file_uploading/"+f.filename)

        with open("file_uploading/"+f.filename, "r") as file:
            for line in file:
                if line.startswith("@"):
                    return render_template("succes_upload_page.html", name=f.filename)
                else:
                    return render_template("failed_upload_page.html", name=f.filename)
