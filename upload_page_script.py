"""
Upload page script
"""
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def root():
    return render_template("uploadpage.html")

@app.route("/about")
def about():
    return render_template("about")

@app.route("/succes", methods=["post"])
def succes():
    if request.method == "POST":
        f = request.files["file"]
        f.save("file_uploading/"+f.filename)

        with open("file_uploading/"+f.filename, "r") as file:
            for line in file:
                if line.startswith("@"):
                    return render_template("succes_upload_page.html", name=f.filename)
                else:
                    return render_template("failed_upload_page.html", name=f.filename)

