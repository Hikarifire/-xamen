import csv


File= 0
if File==input("Escriba nombre del archivo: "):
        with open ("archivo", "x", ".csv",newline=" ") as File:
            escritor=csv.writer(File)
            escritor.writerow(File)