import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
# inputs = sys.argv[1:]
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('mergedPDFs.pdf')
#     print('Merger done')
# pdf_combiner(inputs)

# with open('dummy.pdf', mode='rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     # print(page)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
