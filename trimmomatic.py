import subprocess

class Trimmomatic:
    """
    A class used to call trimmomatic.
    """
    def __init__(self):
        """
        This function sets the default values for trimmomatic objects.
        """
        self.illuminaclip = "ILLUMINACLIP:TruSeq3-SE:2:30:10"
        self.leading = "LEADING:3"
        self.trailing = "TRAILING:3"

    def run_trimmomatic(self):
        """
        This function calls the tool trimmomatic and creates an output file in the specified place.
        """
        command = [
        "java", "-jar",
        r"tools\Trimmomatic-0.39\trimmomatic-0.39.jar",
        "SE",
        r"file_uploading\SRR18574453.fastq" #file moet nog een variabele worden
        r"C:\Users\Gebruiker\Downloads\OUTPUT.fq", #naam input_output
        self.illuminaclip,
        self.leading,
        self.trailing
        ]

        subprocess.run(command)

trim_object = Trimmomatic()
trim_object.run_trimmomatic()

#TO DO: oplossing naam
#TO DO pad veranderen output data
#TO DO: opties voor gebruiker toevoegen
