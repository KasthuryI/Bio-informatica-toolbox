import subprocess
# from upload_page_script import *

class Trimmomatic:
    """
    A class used to call trimmomatic.
    """
    def __init__(self, minlen, crop, file):
        """
        This function sets the default values for trimmomatic objects.
        """
        self.illuminaclip = "ILLUMINACLIP:TruSeq3-SE:2:30:10"
        self.leading = "LEADING:3"
        self.trailing = "TRAILING:3"
        self.minlen = minlen
        self.crop = crop
        self.filename = file

    def run_trimmomatic(self):
        """
        This function calls the tool trimmomatic and creates an output file in the specified place.
        """
        command = [
        "java", "-jar",
        r"tools\Trimmomatic-0.39\trimmomatic-0.39.jar",
        "SE",
        r"file_uploading\SRR18574453.fastq", #file moet nog een variabele worden
        # r"file_uploading\"" + self.filename,
        r"trimmomatic_output\OUTPUT.fq",
        self.illuminaclip,
        self.leading,
        self.trailing,
        self.minlen,
        self.crop
        ]

        subprocess.run(command)
    


trim_object = Trimmomatic()
trim_object.run_trimmomatic()

#TO DO: oplossing naam inputfile
#TO DO: opties voor gebruiker toevoegen

# Vragen voor end of sprint:
# Opties doorgeven, hoe?
# Filename doorgeven, hoe?