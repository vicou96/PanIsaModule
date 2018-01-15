# About this module
This project is a tool meant to be implemented on a Galaxy instance, an open, web-based platform for accessible, reproducible, and transparent computational biomedical research.

# panISa
panISa is a software to search insertion sequence (IS) on resequencing data (bam file) in bacteria.

## Idea
The principle of panISa is to search Insertion Sequence on NGS data without knowledge of potential IS present in the bacterial strain.
To achieve that, the software identified a signature of insertion in the alignment by counting clip read at start and end position.
These reads overlapped on the direct repeat due to IS insertion.
Finally, using a reconstruction of the beginning of both side of the IS, the software valided the IS by searching inverted repeat region

## Requirements
The program used the python library **pysam** (>0.9), included in the Galaxy instance.
samtools is also required.


You need to install the **emboss** package:
http://emboss.sourceforge.net

In debian, type:
> sudo apt-get install samtools<br />
> sudo apt-get install emboss

## Install PanIsa as a tool
For more informations about tools, please visit: https://galaxyproject.org/tools/#using-tools

Start by cloning the project under the folder tools, located in your main Galaxy folder.

Galaxy recognizes installed tools by reading the tool_conf.xml tool configuration file. Thus, letting Galaxy know about the new tool is as easy as adding a few lines to the tool_conf.xml file located in the config/ directory of the Galaxy installation. New tools can either be added to existing sections or added to new sections defined in the following way:

Markup :  `code()`
 <section name="Panisa" id="mTools">
    <tool file="panisa/panisa.xml" />
 </section>

## Recommandation
panISa works well with the alignment from **bwa** software.


## Development
The program is currently in developpemnt, but return some result.