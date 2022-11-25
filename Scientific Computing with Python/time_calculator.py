def add_time(start_time, duration_time, day=None):
    # function to get hours from time
    def get_hours(time):
        time = time.split()[0]
        return time.split(':')[0]

    # function to get minutes from time
    def get_minutes(time):
        time = time.split()[0]
        return time.split(':')[1]

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

    
