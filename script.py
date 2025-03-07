#!/usr/bin/env python3



import sys



def read_file(filename):

  try:

    file = open(filename, 'r')

    lines = file.readlines()

    file.close()

    return lines

  except FileNotFoundError:

    return ["File not found!"]



def main():

  if len(sys.argv) != 2:

    print("Error: no file specified.")

    sys.exit()



  filename = sys.argv[1]

  lines = read_file(filename)



  for line in lines:

    print(line.strip())



  print(f"Number of lines: {len(lines)}")



if __name__ == "__main__":

  main()