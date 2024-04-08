"""
Title: Module main.py
Author: Mirte Draaijer, Ivar Lottman, Kasthury Inparajah, Storm Steller
Date: 1-4-2024
Version: 1.0
Summary: This module functions as the main module of the website.
It contains functions for serving static pages,
and it contains 2 functions for using FastQC and Trimmomatic.
"""

from flask import Flask, request, render_template, session, send_file
# impport class tools from respective"s scripts
from trimmomatic import Trimmomatic
from fastqc import FastQC
import os

# limmits imput to fq and fastq files
ALLOWED_EXTENSIONS = {"fq", "fastq"}
# session keys
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
app.secret_key = "TRIMTASTISCHE_TIJGERS"


def allowed_file(file):
    """
    this function part of file uploading it checks if the given
    file is allow thruw a boolean check with the global ALLOWED_EXTENSIONS
    list
    Param: file string
    Return: True or False boolean
    """
    return file.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def root():
    """
    This function is used to serve the root of the website
    Param: Function call /
    Return: Renders homepage.html
    """
    return render_template("homepage.html")


@app.route("/homepage")
def homepage():
    """
    This function is used to serve the homepage
    Param: Function call /homepage
    Return: Renders homepage.html
    """
    return render_template("homepage.html")


@app.route("/about")
def about():
    """
    This function is used to serve the about page
    Param: Function call /about
    Return: Renders about.html
    """
    return render_template("about.html")


@app.route("/uploadpage")
def uploadpage():
    """
    This function is used to serve the upload page
    Param: Function call /uploadpage
    Return: Renders uploadpage.html
    """
    return render_template("uploadpage.html")


@app.route("/fastqc")
def fastqc():
    """
    This function is used to serve the fastqc page
    Param: Function call /fastqc
    Return: Renders fastqc.html
    """
    return render_template("fastqc.html")


@app.route("/trimmomatic")
def trimmomatic():
    """
    This function is used to serve the trimmomatic page
    Param: Function call /trimmomatic
    Return: Renders trimmomatic.html
    """
    return render_template("trimmomatic.html")


@app.route("/contactpage")
def contactpage():
    """
    This function is used to serve the contact page
    Param: Function call /contactpage
    Return: Renders contactpage.html
    """
    return render_template("contactpage.html")


@app.route("/how_does_it_work")
def how_does_it_work():
    """
    This function is used to serve the how does iet work page
    Param: Function call /how_does_it_work
    Return: Renders how_does_it_work.html
    """
    return render_template("how_does_it_work.html")


@app.route("/disclaimer")
def disclaimer():
    """
    This function is used to serve the disclaimer page
    Param: Function call /disclaimer
    Return: Renders disclaimer.html
    """
    return render_template("disclaimer.html")


@app.route("/succes", methods=["post"])
def succes():
    """
    This function is used for uploading and visualizing the first
    fastq or fq file. if the request method is post it requests the file
    and checks if its a valid file thruw the allow_file function and an extra
    "@" in file open check and when succesful is then uploaded into
    the uploading folder. it then calls on the FastQC class to generate
    the fastqc plots and filepath that is passed onto the succes page.
    the plots are located in the static folder along with the original
    fastqc rapport.

    conditions for failed invalid file exctensions or first line in file
    did not start with an "@"

    param: function call form /succes in the upload_page.html
    return: Renders succes upload page
    return: Renders failed upload page
    """

    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            session["filename"] = file.filename
            session["path_folder"] = file.filename.replace(".fastq", "_fastqc/")

            file.save("file_uploading/"+file.filename)
            with open("file_uploading/"+file.filename, "r") as files:

                for line in files:
                    # extra check
                    if line.startswith("@"):
                        # fastqc tool
                        file_name_fastqc = FastQC(file.filename)
                        file_name_fastqc.run(r"/file_uploading")
                        # getting basic statics
                        with open("static/"+session["path_folder"]+"fastqc_data.txt", "r") as data_files:
                            data_list = []
                            for line in data_files:
                                if "#" in line:
                                    continue
                                if "Basic" in line:
                                    continue
                                if ">>END_MODULE" not in line:
                                    data_list.append(line.strip())
                                else:
                                    break
                            session["original_stats"] = data_list
                        return render_template("succes_upload_page.html",
                                               name=session["filename"], original=session["path_folder"], data=session["original_stats"])

                    else:
                        return render_template("failed_upload_page.html", name=session["filename"])

        else:
            return render_template("failed_upload_page.html", name=file.filename)


@app.route("/options_page", methods=["GET", "POST"])
def options():
    """
    This function uses the trimmomatic tool to trim the
    fastq file into an fq file. wich is then run truw fastq to
    to genarate plots and a file patch wich is past on to the compare
    page. the plots and the original fastqc rapport can are located in the
    static folder.
    reason for plots not rendering can be excessive trimming
    param: function call /options_page initated on the succes page
    using trim data butten.
    return: renderd compare page.
    """

    if request.method == "POST":
        # trim data requests
        crop_value = request.form["crop"]
        minlen_value = request.form["minlen"]
        sliding_show = request.form["sliding"]
        trailing_value = request.form["trailing"]
        leading_value = request.form["leading"]

        # running trimmomatic with data requests and session path
        trim_object = Trimmomatic(leading_value, trailing_value, sliding_show, minlen_value, crop_value, session["filename"])
        trim_object.run_trimmomatic()

        # running fastqc on the newly trimmed data
        trim_output_file = FastQC("OUTPUT.fq")
        trim_output_file.run(r"/trimmomatic_output")
        compare_path = "OUTPUT_fastqc/"

        # loop to get the basic statistics plot
        with open("static/"+compare_path+"fastqc_data.txt", "r") as compare_file:
            compare_list = []
            for line in compare_file:
                if "#" in line:
                    continue
                if "Basic" in line:
                    continue
                if ">>END_MODULE" not in line:
                    compare_list.append(line.strip())
                else:
                    break
            session["comp_stats"] = compare_list
            print(session["comp_stats"])

        return render_template("compare.html",
                               original=session["path_folder"], compare=compare_path,
                               data=session["original_stats"], comp_data=session["comp_stats"])

    if request.method == "GET":
        return render_template("options_page.html")


@app.route("/compare", methods=["get"])
def download_file():
    file_path = os.getcwd() + "/trimmomatic_output/OUTPUT.fq"
    return send_file(
        file_path,
        download_name="trimmed-" + session["filename"],
        as_attachment=True
    )
