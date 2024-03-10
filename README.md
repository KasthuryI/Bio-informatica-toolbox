# **Bio-informatics Toolbox Website: TrimTech**

### **Authors:** Ivar Lottman, Storm Steller, Kasthury Inparajah & Mirte Draaijer 
### **Version:** 0.1.1
### **Date:** 7/3/2024

___

## **Name and usage**
### **TrimTech**
#### This website is used for quality control and trimming FASTQ files before the mapping and coverage phase of the data.
#### We created this website because not all of the data produced by sequencing is 100% accurate and when you want to do mapping and covarage of a reference genome you want to use the accurate data. Therefore this tool was created to help in that process. 

#### It does this by visualising the FASTQ data with a tool called FASTQC and another tool called Trimommatic for trimming the FASTQ data based on input commands. 


## **Programmer/ICT user manual**
TO DO: MANUAL BASED ON HOW THE GUI WORKS ON THE WEBSITE


## **GUI input file**
THIS PART OF THE GUI IS FOR INPUT FILES


## **FASTQC based commands**

## **Trimmomatic**
### **In- and output**
#### Trimmomatic works with FASTQ, using phred - 33 or phred - 64 quality scores. The FASTQ can be either uncompressed or zipped. The use of the gzip format is determined based on the .gz extension.

#### Once you have performed the command, an output file will be created in the directory you are currently in. This output file can be an uncompressed FastQ or a gzipped FastQ, depending on how you specified the output in your command. This output can be used in programms like FastQC to recheck the quality of the sequence.

### **Usage**
#### To use Trimmomatic, go to the terminal of your OS. The command needed to run Trimmomatic depends on if your data is single- or paired end. 

### **Single-end**
#### If your data is single end, use te following example:
```java -jar trimmomatic-0.39.jar SE -phred33 "input.fq.gz" "output.fq.gz" ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36```

#### Single ended data only takes 1 input, a FastQ file, and gives 1 output back, a trimmed version of the sequence. You will need to change input.fq.gz to the name of your desired FastQ file. You can also change the name of the output.fq.gz to your desired name, but this is optional. 

#### You can also change the extension of your output. If you want it to be uncompressed, use .fq of fastq. If you want it to be compressed in a gzip, use .fq.gz or .fastq.gz.

### **Paired end**
#### If your data is paired end, use this example:

```java -jar trimmomatic-0.39.jar PE "input_forward.fq.gz" "input_reverse.fq.gz" "output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz" "output_reverse_unpaired.fq.gz" ILLUMINACLIP:TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36```

#### Paired ended data takes 2 inputs, the forward sequence and the backward sequence. This command gives you 4 outputs, a paired sequence, where both reads survived the processing, and  an unpaired sequence where only one read survived but not its partner read, of the forward- and backward sequence.

### **Trimommatic based commands**

#### The following arguments are mostly used in Trimmomatic:
#### • **ILLUMINACLIP:** Cuts adapters and other illumina-specific sequences from the read. (ILLUMINACLIP:TruSeq3-PE.fa:2:30:10) 

#### • **LEADING:** Cuts bases off the start of a read, if it is below a threshold quality. (LEADING:3) 

#### • **TRAILING:** Cuts bases of the end of a read, if it is below a threshold quality. (TRAILING:3) 

#### • **SLIDINGSHOW:** Performs a sliding window trimming, cuts if the average quality within the window is bellow a threshold (SLIDINGWINDOW:4:15) The first argument is the size of the window. The argument is the threshold quality.

#### • **MINLEN:** Drop the read if it is below the specified length. (MINLEN:36)

#### The following arguments are not used often, but it is good to know about them:
#### • **CROP:** Cuts the read to a specified length. (CROP:10) • HEADCROP: Cuts the bases off the end of a read if below a threshold quality. (HEADCROP:15) 

#### • **TOPHRED33:** Converts the quality score to Phred-33 • TOPHRED64: Converts the quality score to Phred-64. If no phred score is specified, Trimmomatic will default to phred + 33.


## **Installation** *(expanded manual)*

### **Install Java**
#### Please make sure to have installed Java on your computer since Jave is needed to run both FastQC and Trimmomatic. You can donwload Java from the following website: website: https://www.java.com/nl/. **Please note that Trimmomatic requires Java 1.8 or higher!**

### **FastQC**
#### This manual was written based on the official instructions for installing FastQC, so if you want you can follow those: https://raw.githubusercontent.com/s-andrews/FastQC/master/INSTALL.txt

#### **Installation**
#### **1.** Make sure you have downloaded Java. If not, please download Java from the following website:  https://www.java.com/nl/. 
#### **2.** Download FastQC (version 0.12.1 or higher) from the following website: https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc
#### **Make sure you download the correct version for your operating system (Linux, Windows or Mac)!**
#### **3.** When you have downloaded the FastQC file from the website, you need to unzip it.
#### **4.** After unzipping, FastQC is ready to go.

### **Trimommatic**
#### This manual was written based on the instructions for installing Trimmomatic, so if you want you can follow those: http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf

#### **Installation**
#### **1.** To install Trimmomatic, go to http://www.usadellab.org/cms/?page=trimmomatic and download a binary release zip of Trimmomatic of version 0.39 or higher. 
#### **2.** Unpack the zip in a convenient folder.
#### **3.** Once installed and unpacked, you can acces Trimmomatic using the terminal of your OS.


## **Systeem requirements**
### Working OS: Windows 10 or 11
### Linux Debian v12


## **Hardware requirements**
### No specific requirements


## **Installation Manual short**

### **Java** *(v1.8.0_401)*
#### Follow the install manual from the official Java website:
https://www.java.com/nl/download/

### **Python** *(v3.11.8)*
#### Follow the install manual from the official Python website:
https://www.python.org/downloads/

### **FastQC** *(v0.12.1)*
https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

### **Trimmomatic** *(v0.39)*
http://www.usadellab.org/cms/?page=trimmomatic

## **Module discription**
#### Commandline: Scriptname
TO DO: PER SCRIPT, WEBSITE SCRIPT, TOOL SCRIPT AND FLASK VERSION

## **DISCLAIMER: TrimTech only uses input from Illumina.**

## **Support**
### **Ivar Lottman:** i.lottman@st.hanze.nl
### **Storm Steller:** s.steller@st.hanze.nl
### **Kasthury Inparajah:** k.inparajah@st.hanze.nl
### **Mirte Draaijer:** mi.draaijer@st.hanze.nl


## **Acknowledgment**
TO DO