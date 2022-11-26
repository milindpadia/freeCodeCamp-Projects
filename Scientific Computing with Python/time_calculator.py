def add_time(start_time, duration_time, day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # function to get hours from time
    def get_hours(time):
        time = time.split()[0]
        return int(time.split(':')[0])

    # function to get minutes from time
    def get_minutes(time):
        time = time.split()[0]
        return int(time.split(':')[1])

    # function to get am or pm from time
    def get_am_pm(time):
        return time.split()[1].lower()

    # start time
    am_or_pm = get_am_pm(start_time)
    start_time_hours = get_hours(start_time)
    start_time_minutes = get_minutes(start_time)

    # duration time
    duration_time_hours = get_hours(duration_time)
    duration_time_minutes = get_minutes(duration_time)

    final_minutes = start_time_minutes + duration_time_minutes
    final_hours = start_time_hours + duration_time_hours

    no_of_days_later = 0
    if final_hours > 24:
        while final_hours > 24:
            final_hours -= 24
            no_of_days_later += 1
        if final_hours > 12:
            final_hours -= 12
            no_of_days_later += 1
            if am_or_pm == 'pm':
                am_or_pm = "AM"
            else:
                am_or_pm = 'PM'
        if final_minutes > 60:
            final_minutes -= 60
            final_minutes = "0"+str(final_minutes)
            final_hours += 1
            no_of_days_later += 1
            if am_or_pm == 'pm':
                am_or_pm = "AM"
            else:
                am_or_pm = 'PM'
            
            
    else:
        if am_or_pm == "am":
            if final_hours > 12:
                am_or_pm = "PM"
                final_hours -= 12
            else:
                am_or_pm = "AM"
            if final_minutes > 60:
                final_minutes -= 60
                final_minutes = "0"+str(final_minutes)
                final_hours += 1
                if final_hours >= 12:
                    am_or_pm = "PM"
        else:
            if final_hours > 12:
                am_or_pm = "AM"
                final_hours -= 12
            else:
                am_or_pm = "PM"
            if final_minutes > 60:
                final_minutes -= 60
                final_minutes = "0"+str(final_minutes)
                final_hours += 1
                if final_hours >= 12:
                    am_or_pm = "AM"
    
    # future time
    future_time = "{}:{} {}".format(final_hours, final_minutes, am_or_pm)

    # (no. of days later)
    if no_of_days_later == 1:
        n_days_later = "(next day)"
    else:
        n_days_later = "({} days later)".format(no_of_days_later)
    
    # future day
    if day == None:
        return future_time + ' ' + n_days_later
    else:
        index = days_of_week.index(day.title())
        future_day = index + no_of_days_later
        if future_day > 7:
            while future_day > 7:
                future_day -= 7
            future_day = days_of_week[future_day]
        else:
            future_day = days_of_week[index + no_of_days_later]
        return future_time + ', ' + future_day + ' ' + n_days_later
    
    

add_time("11:43 PM", "24:20", "tueSday")

