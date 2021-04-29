# GCSE NEA 2021, code written by: Marcus Sorensen
# Github Repository: https://github.com/marcus-dk/gcseNEA
 
# Importing Necessary Libraries and Files
import json
import timeallocation as ta


# Main Class for Parent's Evening Scheduling System
class SchedulingProgram:

  # JSON related functions allowing for loading and dumping of data
  def jsonOpen(self, jsonfile="timetable.json"):
    with open(jsonfile) as file:
      jsondata = json.load(file)
    return jsondata

  def jsonClose(self, jsondata, jsonfile="timetable.json"):
    with open(jsonfile, "w") as file:
      json.dump(jsondata, file, sort_keys=True, indent=2) 
    

  # Simple Data Input
  # Gets us the time preferences of appointment
  def timeinput(self, parentID, times, jsondata):
    duplicate = ta.duplicate(jsondata, parentID)
    if duplicate != False:
      print("You have already reserved a meeting time.\nYou can not reserve another slot. If you wish to change your time you can cancel your time and then reserve a new one.")
      self.mainmenu(parentID, times, jsondata)

    print("To be allocated a time slot for your meeting you must input your preferences regarding what day and slot you'd like to have the meeting.\nPlease do so below")

    for slot, time in times.items():
      print(slot,"="+"\t"+time[0]+" - "+time[1])
    
    while 1:
      self.daypref = input("What day would you prefer to have your meeting? Day [1],[2], or [3]: ")
      self.slotpref = input("What time slot would you prefer to reserve? [Enter as shown above (ex. slot2)]: ")
      self.inputdata = [self.daypref, self.slotpref]

      while 1:
        if (self.daypref in ["1","2","3"]) and (self.slotpref in times):

          available = ta.checkslot(self.inputdata, jsondata)
          if available == False:
            print("Your slot is already taken, please try again.")
            quit()
          
          self.daypref = int(self.daypref) - 1
          available = ta.checkavailability(jsondata, self.inputdata, parentID)

          if available == 0:
            self.mainmenu(parentID, times, jsondata)

          elif available == True:
            jsondata = ta.allocatetime(jsondata, self.inputdata, parentID)
            print("You have been allocated your meeting.")
            self.jsonClose(jsondata)
            self.mainmenu(parentID, time, jsondata)
          else: 
            print("Sadly this slot is already occupied. Please enter an alternate time slot. Sorry for any inconvenience")
            break
        
      else:
        print("You have inputted an invalid response, please try again")
        break


  # Main Landing Page of Program
  # Allows user to navigate the program
  def mainmenu(self, parentID, times, jsondata):

    print(f"\nWelcome {parentID}, what are you looking to do?")
    if parentID != "admin":
      self.choice = input("[1] Reserve a time for your meeting with your child's teacher\n[2] Cancel your existing meeting\n[3] View your time\n1,2,3: ")
    else: 
      self.choice = input("[1] Reserve a time for your meeting with your child's teacher\n[2] Cancel your existing meeting\n[3] View your time\n[4] View the entire timetable\n1,2,3,4: ")
    print(f"You have chosen {self.choice}, you will be redirected...\n\n")

    while 1: 
      if self.choice:
        if parentID == "admin": # admin print all timetable
          if self.choice == "4":
            ta.printtimetable(jsondata, parentID)
            self.mainmenu(parentID, times, jsondata)

        if self.choice == "1": # allocate time
          self.timeinput(parentID, times, jsondata)
          
        elif self.choice == "2": # cancel time
          x = ta.canceltime(jsondata,parentID)
          if x == False:
            self.mainmenu(parentID, times, jsondata)
          else:
            print("Your appointment has been cancelled. ")
            self.jsonClose(jsondata)
            self.mainmenu(parentID, times, jsondata)

        elif self.choice == "3": # prints singular time
          x = ta.showtime(jsondata, parentID)
          if x == False:
            print("You do not have a time, therefore there is nothing to show")
            self.mainmenu(parentID, times, jsondata)
          else:
            self.mainmenu(parentID, times, jsondata)

        else:
          print("You have inputted an invalid response, please try again")
          quit()

      else:
        print("You have inputted an invalid response, please try again")
        quit()


  # "Login System" for parents, asks for ID in the specified format
  def landingpage(self, times, jsondata):

    print("This is the Scheduling System for the upcoming Parents Evening")
    self.parentID = input("Please enter your parentID: ")
    if self.parentID:
      self.mainmenu(self.parentID, times, jsondata)
    else: 
      print("You have entered erroneous data, please try again")
      quit()


  def __init__(self):

    # Gives us the times slots in an 
    # accessible manner
    self.times = {
      "slot1": ["5:00","5:20"],
      "slot2": ["5:20","5:40"],
      "slot3": ["5:40","6:00"],
      "slot4": ["6:00","6:20"],
      "slot5": ["6:20","6:40"],
      "slot6": ["6:40","7:00"],
      "slot7": ["7:00","7:20"],
      "slot8": ["7:20","7:40"],
      "slot9": ["7:40","8:00"]
      }

    self.jsondata = self.jsonOpen()

    self.landingpage(self.times, self.jsondata)

print("The following code is written by Marcus Sorensen.\nIt is written in February 2021 as part of his GCSE NEA for Computer Science\n\n")
run_SchedulingProgram = SchedulingProgram()
