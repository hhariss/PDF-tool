import PyPDF2, sys

def remove_pages(input, output, pages_to_remove):
      if len(input) > 1:
            print('Error: There must be only one input path when removing pages', file=sys.stderr)
            sys.exit(1)
      
      with open(input[0], 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()
            
            for page_num in range(len(reader.pages)):
                  if page_num+1 not in pages_to_remove:
                        writer.add_page(reader.pages[page_num])
            
            writer.write(output)
            writer.close()