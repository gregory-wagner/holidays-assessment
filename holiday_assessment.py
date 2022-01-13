from datetime import datetime
import json
from os import name
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    name: str
    date: datetime.date
      
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return self.name+ '(' + self.date.strftime('%Y-%m-%d') + ')'
    
    def __repr__ (self):
        return str(self) 
        
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
    
    def __str__(self):
        rep = ", ".join([str(x) for x in self.innerHolidays])
        return rep
   
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        if isinstance(holidayObj, Holiday):
            self.innerHolidays.append(holidayObj)
            print(holidayObj,' has been added.')

    def findHoliday(self, HolidayName, HolidayDate):
        # Find Holiday in innerHolidays
        # Return Holiday
        holiday = filter(lambda holiday: holiday.name == HolidayName and holiday.date == HolidayDate, self.innerHolidays)
        print(holiday)

    def removeHoliday(self, HolidayName, HolidayDate):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        holiday = filter(lambda holiday: holiday.name == HolidayName and holiday.date == HolidayDate, self.innerHolidays)
        if holiday in self.innerHolidays:
            print((holiday),' has been removed.')
            del HolidayName
            del HolidayDate
            

    def read_json(filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.
        with open('holidays.json','r') as filelocation:
            data = json.loads(filelocation)
            filelocation.addHoliday(data)

    def save_to_json(filelocation):
        # Write out json file to selected file.
        with open('holidays.json','w') as filelocation:
            data = json.dumps(filelocation)
        
    def scrapeHolidays():
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.
        def getHTML(url):
            response = requests.get(url)
            return response.text

        holidays = []

        for i in range(2020,2025):
            try:
                page = f'https://www.timeanddate.com/holidays/us/{i}'    
                html = getHTML(page)
                soup = BeautifulSoup(html,'html.parser')
                table = soup.find('tbody')
                for row in table.find_all('tr'):
                    try:
                        cells = row.find_all_next('td')
                        holiday = {}
                        holiday['name'] = cells[1].text
                        holiday['date'] = row.find('th', attrs={'class': 'nw'}).text
                        holiday['year'] = i
                        holidays.append(holiday)
                    except:
                        pass
            except:
                pass
        self.innerHolidays.append(holidays)   

    def numHolidays():
        Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results



def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
    holidayname = 'Christmas'
    holidaydate = datetime.strptime('2023-12-25','%Y-%m-%d')
    holidayname2 = 'Halloween'
    holidaydate2 = datetime.strptime('2023-10-31','%Y-%m-%d')
    holiday1 = Holiday(holidayname, holidaydate)
    holiday2 = Holiday(holidayname2, holidaydate2)
    holidaylist = HolidayList()
    holidaylist.addHoliday(holiday1)
    holidaylist.addHoliday(holiday2)
    print(holidaylist)
    holidaylist.removeHoliday(holidayname2,holidaydate2)
    #Questions: findHoliday only prints out <filter object...> and removeHoliday not printing anything



if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





