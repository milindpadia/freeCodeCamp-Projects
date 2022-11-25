def add_time(start_time, duration_time, day=None):
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
    
    # return "{}:{} {}".format(final_hours, final_minutes, am_or_pm)
    print("{}:{} {}".format(final_hours, final_minutes, am_or_pm))

add_time("5:23 PM", "0:20")

