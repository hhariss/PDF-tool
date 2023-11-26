import sys, argparse
import remove_pages, merge_pages

def main():
      parser = argparse.ArgumentParser(description='Manipulate a PDF file')
      parser.add_argument('-i', '--input', type=str, nargs='*', help='Path to input file')
      parser.add_argument('-o', '--output', type=str, help='Path to output file')      
      parser.add_argument('-r', '--remove', nargs='*', help='Remove pages')
      parser.add_argument('-m', '--merge', action='store_true', help='Remove pages')
      parser.add_argument('other_args', nargs=argparse.REMAINDER, help='Remaining arguments')
      
      args = parser.parse_args()
      
      if args.remove:
            remove_pages(args.input, args.output, args.remove)
      else:
            print('Nonee')
      # elif args.merge:
      #       # merge_pages(args.input, args.output)
      # else:
      #       print('Must merge or remove', file=sys.stderr)

if __name__ == "__main__":
      main()