def read_data(filename):
  """Transforms iClicker csv into an iClicker nested list."""

  # Open
  file = open(filename, 'r')

  # Read
  lines = file.readlines()

  # Close
  file.close()

  # Prepare data
  # print(lines)
  # print(lines[1])
  iClicker = []

  # Convert the lines in the file into sublists
  for line in lines[1:]:
    # Strip string function
    # Remove the \n from the end of each row
    line = line.strip()

    # Split string function
    line = line.split(',')

    slist = []
    slist.append(line[0])
    scores = line[1:]

    for item in scores:
        if item == "" or item == "0":
          slist.append(0)
        elif item == "1":
          slist.append(1)
      
    iClicker.append(slist) 

  return iClicker

iClicker_22fa = read_data("22fa_clicker.csv")

print(iClicker_22fa)
