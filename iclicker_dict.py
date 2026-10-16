iClicker = {'Alex': [0, 0, 1, 1, 1, 1],
 'Erin': [1, 1, 1, 0, 0],
 'Mika': [0, 1, 1, 1, 1]}

def most_recent(slist):
  """
  Given a student’s list of iClicker data, return the index (“# sessions ago”) of their most recent attendance.
  """
  for i in range(len(slist)):
    if slist[i] == 1:
      return i

  return None

for key in iClicker:
  print(key + ": " + str(most_recent(iClicker[key])) + " sessions ago")