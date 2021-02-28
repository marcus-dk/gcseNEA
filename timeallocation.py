# Separate File for Time Allocation Logic

# Class checks through JSON data and sees if inputted 
# preferences collide with previously inputted data.

def checkavailability(jsondata, inputdata):
  day = "day"+inputdata[0]
  slot = inputdata[1]
  try:
    daydata = jsondata[day]
    slotdata = daydata[slot]

  except KeyError:
    print("You have inputted your preferences in an incorrect format, please try again.")
    return 0

  if slotdata[0] == "0":
    available = True
  elif slotdata[0] == "1": 
    available = False
  else:
    print("An error has occurred.")
    quit()
  
  return available

# Class checks if parentID already has an allocated time slot
def duplicate(jsondata, parentID):
  dupe = False
  for day, slots in jsondata.items():
    for slot, list in slots.items():
      if list[0] == "0":
        continue
      elif list[0] == "1":
        dupe = True
      else:
        print("An error has occurred")
        quit()
  return dupe


# Class is called after checkavailability, uses logic created by me
# to decide best time if preferences not available and returns result, 
# or allocates preferred time if slot is available and returns result. 
def allocatetime(jsondata, inputdata, parentID):
  day = "day"+inputdata[0]
  slot = inputdata[1]
  daydata = jsondata[day]
  allocateindicator = daydata[slot]
  allocateindicator[0] = "1"
  allocateindicator[1] = parentID 
  daydata[slot] = allocateindicator
  jsondata[day] = daydata

  return jsondata

# calls duplication - if True we delete  
def canceltime(jsondata, inputdata, parentID):
  dupe = duplicate(jsondata, parentID)
  if dupe == True:
    # find and delete
    return True
  else: 
    print("You do not have a meeting appointment, therefore there is nothing to cancel.")
    return False

# calls cancel - calls allocation
def reallocatetime(jsondata, inputdata, parentID):
  pass

# looks for time - prints
def showtime(jsondata, parentID):
  pass

# checks parentID - if authorised, prints full json
def printtimetable(jsondata, parentID):
  pass