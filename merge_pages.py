import PyPDF2

def merge_pages(input, output):
      merger = PdfWriter()
      
      for pdf in input:
            merger.append(pdf)
            
      merger.write(output)
      merger.close()