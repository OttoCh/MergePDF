import os
import sys
from PyPDF2 import PdfFileMerger
# from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

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

# def get_size_format(b, factor=1024, suffix="B"):
#     """
#     Scale bytes to its proper byte format
#     e.g:
#         1253656 => '1.20MB'
#         1253656678 => '1.17GB'
#     """
#     for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
#         if b < factor:
#             return f"{b:.2f}{unit}{suffix}"
#         b /= factor
#     return f"{b:.2f}Y{suffix}"

# if(doCompression == True):
#     # Compress the result pdf
#     initial_size = os.path.getsize(outputDir + '/' + outputFilename)
#     try:
#         # Initialize the library
#         PDFNet.Initialize()
#         doc = PDFDoc(outputDir + '/' + outputFilename)
#         # Optimize PDF with the default settings
#         doc.InitSecurityHandler()
#         # Reduce PDF size by removing redundant information and compressing data streams
#         Optimizer.Optimize(doc)
#         doc.Save(outputDir + '/' + outputFilename, SDFDoc.e_linearized)
#         doc.Close()
#     except Exception as e:
#         print("Error compress_file=", e)
#         doc.Close()

#     compressed_size = os.path.getsize(outputDir + '/' + outputFilename)
#     print("Compression result:")
#     print("Initial: " + get_size_format(initial_size))
#     print("Compressed: " + get_size_format(compressed_size))
