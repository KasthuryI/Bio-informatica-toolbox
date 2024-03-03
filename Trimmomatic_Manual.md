Trimmomatic Manual
Requirements
Trimmomatic requires Java version 1.8 or higher.

Installation
To install Trimmomatic, go to http://www.usadellab.org/cms/?page=trimmomatic and download a binary release zip of Trimmomatic of version 0.39 or higher. Unpack the zip in a convenient folder.

Once installed and unpacked, you can acces Trimmomatic using the terminal of your OS.

**In- and output**
Trimmomatic works with FASTQ, using phred + 33 or phred + 64 quality scores. The FASTQ can be either uncompressed or zipped. The use of the gzip format is determined based on the .gz extension.

**Usage**
To use Trimmomatic, go to the terminal of your OS. The command needed to run Trimmomatic depends on if your data is single- or paired end. 

**Single-end**
If your data is single end, use te following example:
**java -jar trimmomatic-0.39.jar SE -phred33 "input.fq.gz" "output.fq.gz" ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36**

Single ended data only takes 1 input, a fastq file, and gives 1 output back, a trimmed version of the sequence. You will need to change input.fq.gz to the name of your desired fastq file. You can also change the name of the output.fq.gz to your desired name, but this is optional. 

You can also change the extension of your output. If you want it to be uncompressed, use .fq of fastq. If you want it to be compressed in a gzip, use .fq.gz or .fastq.gz.

**Paired end**
If your data is paired end, use this example:

java -jar trimmomatic-0.39.jar PE "input_forward.fq.gz" "input_reverse.fq.gz" "output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz" "output_reverse_unpaired.fq.gz" ILLUMINACLIP:TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36

Paired ended data takes 2 inputs, the forward sequence and the backward sequence. This command gives you 4 outputs, a paired sequence, where both reads survived the processing, and unpaired sequence, where only a read survived but not its partner read, of the forward- and backward sequence.

**Steps**
In the example arguments are also a few steps. They do the following:

• **ILLUMINACLIP:** Cuts adapters and other illumina-specific sequences from the read (ILLUMINACLIP:TruSeq3-PE.fa:2:30:10) 

• **LEADING:** Cuts bases off the start of a read, if it is below a threshold quality (LEADING:3) 

• **TRAILING:** Cuts bases of the end of a read, if it is below a threshold quality. (TRAILING:3) 

• **SLIDINGSHOW:** Performs a sliding window trimming, cuts if the average quality within the window is bellow a threshold (SLIDINGWINDOW:4:15) The first argument is the size of the window. The argument is the threshold quality.

• **MINLEN:** Drop the read if it is below the specified length. (MINLEN:36)


These are the steps used in the example command line, but those are not all. There are a few more:

• **CROP:** Cuts the read to a specified length. (CROP:10) • HEADCROP: Cuts the bases off the end of a read if below a threshold quality. (HEADCROP:15) 

• **TOPHRED33:** Converts the quality score to Phred-33 • TOPHRED64: Converts the quality score to Phred-64

If no phred score is specified, Trimmomatic will default to phred + 33.

**Output**
Once you have performed the command, an output file will be created in the directory you are currently in. This output file can be a uncompressed FASTQ or a gzipped FASTQ, depending on how you specified the output in your command. This output can be used in programms like FastQC to recheck the quality of the sequence.