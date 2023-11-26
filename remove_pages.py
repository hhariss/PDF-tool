import PyPDF2, sys

def remove_pages(input, output, pages_to_remove):
      if len(input) > 1:
            print('There must be only one input when removing pages', file=sys.stderr)
            sys.exit(1)
      
      with open(input, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()
            
            for page_num in range(len(reader.pages)):
                  if page_num+1 not in pages_to_remove:
                        writer.add_page(reader.pages[page_num])

            with open(output, 'wb') as output_file:
                  writer.write(output_file)