# Separate File for Time Allocation Logic

# Class checks if parentID already has an allocated time slot
def duplicate(jsondata, parentID):
  dupe = False
  x = 0
  y = 0
  for day, slots in jsondata.items():
    x += 1
    for slot, lists in slots.items():
      y += 1
      if lists[1] == parentID:
        location = [day,slots,x,y,slot]
        return location
      elif lists[1] != parentID:
        continue
      else:
        print("An error has occurred")
        quit()
  return False

def checkslot(inputdata, jsondata):
  availability = True
  x = "day"+inputdata[0]
  day = jsondata[x]
  slot = day[inputdata[1]]
  if slot[0] == "1":
    availability = False

  return availability


# Class checks through JSON data and sees if inputted 
# preferences collide with previously inputted data.

def checkavailability(jsondata, inputdata, parentID):
  dupe = duplicate(jsondata, parentID)
  if dupe == False:
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
  else: 
    print("You already have a time reserved, cancel this time first")

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
def canceltime(jsondata, parentID):
  dupe = duplicate(jsondata, parentID)

  if dupe != False:
    day = dupe[0]
    slot = dupe[-1]
    daydata = jsondata[day]
    allocateindicator = daydata[slot]
    allocateindicator[0] = "0"
    allocateindicator[1] = ""
    daydata[slot] = allocateindicator
    jsondata[day] = daydata

  else: 
    print("You do not have a meeting appointment, therefore there is nothing to cancel.")
    return False


# looks for time - prints
def showtime(jsondata, parentID):
  location = duplicate(jsondata, parentID)
  if location == False:
    return False
  else:
    print(f"Your appointment is on day {location[2]}, during {location[-1]} under the name {parentID}")
    return True

# checks parentID - if authorised, prints full json
def printtimetable(jsondata, parentID):
  if parentID == "admin":
    for day, slots in jsondata.items():
      print(f"{day}:")
      for slot, list in slots.items():
        print(f"\t{slot}: {list}")
