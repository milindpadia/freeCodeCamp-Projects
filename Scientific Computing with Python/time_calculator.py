def add_time(start, duration, day=None):
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
        return time.split()[1]

    # start time
    am_or_pm = get_am_pm(start)
    start_time_hours = get_hours(start)
    start_time_minutes = get_minutes(start)

    # duration time
    duration_time_hours = get_hours(duration)
    duration_time_minutes = get_minutes(duration)

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
            if am_or_pm == 'PM':
                am_or_pm = "AM"
            else:
                am_or_pm = 'PM'
        if final_minutes > 60:
            final_minutes -= 60
            final_minutes = "0"+str(final_minutes)
            final_hours += 1
            no_of_days_later += 1
            if am_or_pm == 'PM':
                am_or_pm = "AM"
            else:
                am_or_pm = 'PM'
            
    else:
        if am_or_pm == "AM":
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
            elif final_minutes < 10:
                final_minutes = "0"+str(final_minutes)
        else:
            if final_hours > 12:
                am_or_pm = "AM"
                final_hours -= 12
                no_of_days_later += 1
            else:
                am_or_pm = "PM"
            if final_minutes > 60:
                final_minutes -= 60
                final_minutes = "0"+str(final_minutes)
                final_hours += 1
                if final_hours >= 12:
                    am_or_pm = "AM"
            elif final_minutes < 10:
                final_minutes = "0"+str(final_minutes)
    
    # future time
    future_time = "{}:{} {}".format(final_hours, final_minutes, am_or_pm)

    # (no. of days later)
    if no_of_days_later == 1:
        n_days_later = "(next day)"
    else:
        n_days_later = "({} days later)".format(no_of_days_later)
    
    # future day and return statements
    if day == None:
        if no_of_days_later == 0:
            new_time = "{}:{} {}".format(final_hours, final_minutes, am_or_pm)
            return new_time
        else:
            new_time = future_time + ' ' + n_days_later
            return new_time
    else:
        index = days_of_week.index(day.title())
        future_day = index + no_of_days_later
        if future_day > 7:
            while future_day >= 7:
                future_day -= 7
            future_day = days_of_week[future_day]
        else:
            future_day = days_of_week[index + no_of_days_later]
        if no_of_days_later == 0:
            new_time = future_time + ', ' + future_day
            return new_time
        else:
            new_time = future_time + ', ' + future_day + ' ' + n_days_later
            return new_time
    
add_time("2:59 AM", "24:00", "saturDay")
