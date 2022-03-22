import os
import sys
from PyPDF2 import PdfFileMerger

inputDir = './input'
outputDir = './output'
orderFile = './order.txt'

orderList = []

# read order of merger from a file
with open(orderFile) as f:
    contents = f.readlines()
    for line in contents:
        orderList.append(line.strip());

print("Order of file:")
print(orderList)

merger = PdfFileMerger()

for filename in orderList:
    merger.append(inputDir + '/' + filename)

merger.write(outputDir + '/' + 'result.pdf')
merger.close()