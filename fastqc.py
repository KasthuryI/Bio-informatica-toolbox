import subprocess
import os

def run_fastqc(filename):
    path_root = os.getcwd()
    path_fastqc = r"\tools\fastqc_v0.12.1\FastQC"
    path_output = r"\file_uploading\\"

    command = ["java",
                "-Xmx250m",
                "-Dfastqc.unzip=true",
                "-Dfastqc.delete=true",
                r"-Dfastqc.output_dir=" + path_root + path_output,
                "-classpath",
                ".;./sam-1.103.jar;./jbzip2-0.9.jar",
                "uk.ac.babraham.FastQC.FastQCApplication",
                path_root + path_output + "SRR18574453.fastq"] #filename]
    print(path_root + path_output)

    os.chdir(path_root + path_fastqc)

    subprocess.run(command)

    os.chdir(path_root)
    return print("QC complete")


# class van de tool maken met methode run, change dir. Basis parameters class: change output dir, command?