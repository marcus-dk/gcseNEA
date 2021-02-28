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
    


  # Function uses timeallocation.py to
  # determine allocated time slots
  def timeallocation(self):

    # checkavailability - if available - timeallocation
    pass


  # Simple Data Input
  # Gets us the time preferences of appointment
  def timeinput(self, parentID, times, jsondata):
    duplicate = ta.duplicate(jsondata, parentID)
    if duplicate == 1:
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
        if self.daypref and self.slotpref:
          
          if (self.daypref in ["1", "2", "3"]) and (self.slotpref in times):
            self.daypref = int(self.daypref) - 1
            available = ta.checkavailability(jsondata, self.inputdata)

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
    self.choice = input("[1] Reserve a time for your meeting with your child's teacher\n[2] Change your existing meeting time\n[3] Cancel your existing meeting\n[4] View your time\n1,2,3,4: ")

    print(f"You have chosen {self.choice}, you will be redirected...\n\n")

    while 1: 
      if self.choice:

        if self.choice == "1":
          self.timeinput(parentID, times, jsondata)

        elif self.choice == "2":
          # Reallocation Function
          break

        elif self.choice == "3":
          # Cancel Function
          break

        elif self.choice == "4":
          # Timetable View function
          break

        else:
          print("You have inputted an invalid response, please try again")
          break

      else:
        print("You have inputted an invalid response, please try again")
        break


  # "Login System" for parents, asks for ID in the specified format
  def landingpage(self, times, jsondata):

    print("This is the Scheduling System for the upcoming Parents Evening")
    self.parentID = input("Please enter your parentID: ")

    self.mainmenu(self.parentID, times, jsondata)


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