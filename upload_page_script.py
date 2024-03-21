from trimmomatic import Trimmomatic
filename = ""

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
        filename = f.filename

        with open("file_uploading/"+f.filename, "r") as file:
            for line in file:
                if line.startswith("@"):
                    return render_template("succes_upload_page.html", name=f.filename)
                else:
                    return render_template("failed_upload_page.html", name=f.filename)
                
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


#Trim opties doorgeven
#Wanneer op start wordt geklikt moet trimmomatic uitgevoerd worden en daarna moeten de nieuwe plotjes weergegeven worden