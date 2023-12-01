import PyPDF2

def merge_pages(input, output):
      merger = PyPDF2.PdfWriter()
      
      for pdf in input:
            merger.append(pdf)

      merger.write(output)
      merger.close()