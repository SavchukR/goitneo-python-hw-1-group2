from datetime import datetime, timedelta
from collections import defaultdict
import calendar

def get_birthdays_per_week(users: {}) -> None:
    """
        Based on input dictionary print peoples who's birthday is within next week

        Logic:
            In case today is Monday - we print all birthdays for next 7 days ignoring weekends
            
            In case today is not Monday - we print all birthdays for next 7 days moving weekend birthday to Monday

        Args:
            users (dictionary): Birthday catalog (name and date)
            
                Format: 
                
                { "name": "<name>", "birthday": datetime() },
                
                Sample:
                
                { "name": "Bill Foolkland", "birthday": datetime(1955, 10, 28) },
        
        Output:
            Print in console who's birthday within this week
            
            Sample:
                
                Monday: Bob, Lily Gates, Lily Evans
                Tuesday: Geremy Evans
                Wednesday: Geremy Gates
                Thursday: Karter Gates
                Friday: Karter Gates
    """
    # const
    DAY_OF_WEEK_CODE_FRIDAY = 4
    DAY_OF_WEEK_CODE_MONDAY = 0

    today_date = datetime.today().date()
    
    is_monday = today_date.weekday()
    
    date_range_upper_limit = today_date + timedelta(days=7)
    
    birthdays_todo = defaultdict(list)

    for user in users:
        
        name = user["name"]
        
        if name == "":
            print(f"Warning: name is empty. Birthday: {str(birthday)}")

        birthday_str = user["birthday"]
        
        try:
            birthday = birthday_str.date()
        except:
            raise(f"Something wrong with date for value {birthday_str}")
        
        birthday_this_year = birthday.replace(year=today_date.year)


        # case: today_date is monday
        # calculate all birthday up to Friday (ignore Sat,Sun)
        if is_monday and (today_date <= birthday_this_year 
                          and birthday_this_year < date_range_upper_limit):
            
            weekday_code = birthday_this_year.weekday()

            if weekday_code <= DAY_OF_WEEK_CODE_FRIDAY:
                weekday_name = calendar.day_name[weekday_code]
            
            birthdays_todo[weekday_name].append(name)
        
        # case: today_date is not monday
        # calculate all birthday for 7 days (Sat,Sun move to monday)
        if (not is_monday) and (today_date <= birthday_this_year 
                                and birthday_this_year < date_range_upper_limit):
            
            weekday_code = birthday_this_year.weekday()

            if weekday_code <= DAY_OF_WEEK_CODE_FRIDAY:
                weekday_name = calendar.day_name[weekday_code]
            else:
                # move birthday to Monday
                weekday_name = calendar.day_name[DAY_OF_WEEK_CODE_MONDAY]
            
            birthdays_todo[weekday_name].append(name)

    # print results
    
    for dow,names in birthdays_todo.items():
        
        list_str = ", ".join(names)
        
        print(f"{dow}: {list_str}")
