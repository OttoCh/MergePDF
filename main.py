import os
import sys
from PyPDF2 import PdfFileMerger

inputDir = './input'
outputDir = './output'
orderFile = './order.txt'
outputFilename = "result.pdf"
doCompression = True

orderList = []

for filename in os.listdir(inputDir):
    print(filename)

# read order of merger from a file
with open(orderFile) as f:
    contents = f.readlines()
    for line in contents:
        orderList.append(line.strip())

print("Order of file:")
print(orderList)

merger = PdfFileMerger()

for filename in orderList:
    merger.append(inputDir + '/' + filename)

merger.write(outputDir + '/' + outputFilename)
merger.close()
