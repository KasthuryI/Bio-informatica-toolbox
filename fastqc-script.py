"""
Fastqc module

"""
import subprocess

command = ["java -Xmx250m -classpath", ".;./sam-1.103.jar;./jbzip2-0.9.jar", "uk.ac.babraham.FastQC.FastQCApplication", r"C:\Users\ivarl\Desktop\Bio-informatica-toolbox\tools\fastqc_v0.12.1\SRR18574453.fastq"]

commandstorm = ["java",
           "-Xmx250m",
           "-classpath",
           r".;./sam-1.103.jar;./jbzip2-0.9.jar",
           r"uk.ac.babraham.FastQC.FastQCApplication",
           r".\seq\SRR18574453.fastq",
           r"C:\Users\ivarl\Desktop\Bio-informatica-toolbox\tools\fastqc_v0.12.1\SRR18574453.fastq" ]
subprocess.run(commandstorm)
#subprocess.Popen(command,)
