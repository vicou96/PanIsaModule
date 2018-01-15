#!/usr/bin/python
# -*- coding: utf-8 -*-

##Copyright (c) 2017 Benoit Valot and Panisa Treepong
##benoit.valot@univ-fcomte.fr
##UMR 6249 Chrono-Environnement, Besançon, France
##Licence GPL
import csv

# Est utilisé dans panISa.py pour afficher les couples.
def writeCSV(output,couples):
    tabName=["Chromosome","Left position", "Clip read left", "Direct repeats","Right position", "Clip read rigth", \
            "Inverted repeats","Left sequences","Right sequences"]
    with output as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(tabName)
        for i, c in enumerate(couples):
            towrite = []
            spamwriter.writerow([
                c.chrom,
                str(c.posend.pos),
                str(len(c.posend.clipend)),
                str(c.dr),
                str(c.posstart.pos+1),
                str(len(c.posstart.clipstart)),
                str(c.ir),
                str(c.cons5prime),
                str(c.cons3prime)])
        if c.ir is None:
            towrite.append("No IR")
        else:
            towrite.append(c.ir)
        towrite.extend([c.cons5prime, c.cons3prime])

def writetabular(output,couples):
    tabName=["Chromosome","Left position", "Clip read left", "Direct repeats","Right position", "Clip read rigth", \
            "Inverted repeats","Left sequences","Right sequences"]

    for i, c in enumerate(couples):
        towrite = []
      
        #Ecris les différentes variables de couples.
        output.write("Chromosome" + "\n")
        output.write(c.chrom)

        output.write("\n")
        output.write("\n")

        output.write("Left position" + "\n")
        output.write(str(c.posend.pos))

        output.write("\n")
        output.write("\n")

        output.write("Clip read left" + "\n")
        output.write(str(len(c.posend.clipend)))

        output.write("\n")
        output.write("\n")

        output.write("Direct repeats" + "\n")
        output.write(c.dr)

        output.write("\n")
        output.write("\n")

        output.write("Right position" + "\n")
        output.write(str(c.posstart.pos + 1))

        output.write("\n")
        output.write("\n")

        output.write("Clip read rigth" + "\n")
        output.write(str(len(c.posstart.clipstart)))

        output.write("\n")
        output.write("\n")

        output.write("Inverted repeats" + "\n")
        output.write(c.ir)

        output.write("\n")
        output.write("\n")

        output.write("Left sequences" + "\n")
        output.write(c.cons5prime)

        output.write("\n")
        output.write("\n")

        output.write("Right sequences" + "\n")
        output.write(c.cons3prime)

        output.write("\n")
        output.write("\n")


        if c.ir is None:
            towrite.append("No IR")
        else:
            towrite.append(c.ir)
        towrite.extend([c.cons5prime, c.cons3prime])

if __name__=='__main__':
    import doctest
    doctest.testmod()
