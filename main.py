import sys, argparse
from remove_pages import remove_pages
from merge_pages import merge_pages

def main():
      parser = argparse.ArgumentParser(description='Manipulate a PDF file')
      parser.add_argument('-i', '--input', type=str, nargs='*', required=True, help='Path to input file(s)')
      parser.add_argument('-o', '--output', type=str, required=True, help='Path to output file')      
      parser.add_argument('-r', '--remove', type=int, nargs='*', help='Remove pages')
      parser.add_argument('-m', '--merge', action='store_true', help='Merge pages')
      
      args = parser.parse_args()
      
      if not args.input or not args.output:
            print('Error: Need to specify input and output paths', file=sys.stderr)
            sys.exit(1)
            
      if args.remove and args.merge:
            print('Error: Cannot do both removing and merging', file=sys.stderr)
            sys.exit(1)
      
      if args.remove:
            remove_pages(args.input, args.output, args.remove)
      elif args.merge:
            merge_pages(args.input, args.output)
      else:
            print('Error: Must merge or remove', file=sys.stderr)

if __name__ == "__main__":
      main()