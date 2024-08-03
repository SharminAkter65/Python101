from PyPDF2 import PdfMerger



AllPDF = ["SharminAktersResume.pdf" , "Ethical_Study_on_Data_Analysis.pdf"]

Merger = PdfMerger()

for NPdf in AllPDF:
    Merger.append(NPdf)

Merger.write("Sharmin.pdf")

Merger.close()