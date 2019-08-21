# iso_time must be a timestamp string in ISO 8601 format and offset is to change the timezone
def time_convert(iso_time, offset=0):
    # months dict for converting from numerical month representation to name
    months = {1: "January", 2: "February", 3: "March",
              4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September",
              10: "October", 11: "November", 12: "December"}
    # last_dy dict for getting the last day of a month
    last_dy = {1: 31, 2: 28, 3: 31, 4: 30,
               5: 31, 6: 30, 7: 31, 8: 31,
               9: 30, 10: 31, 11: 30, 12: 31}
    # Parse out the iso_time string and convert year, month, day and hour into integers. (keep minutes as a string)
    yr = int(iso_time[0:4])
    mo = int(iso_time[5:7])
    dy = int(iso_time[8:10])
    hr = int(iso_time[12:14])
    mi = iso_time[15:17]
    # Add the offset to hour to calculate new time zone time.
    hr = hr + offset
    # Check if the timestamp is in a leap year and update February's last day in the last_dy dict.
    if yr % 4 == 0:
        last_dy[2] = 29
    # Check if adding the offset pushes the hour into the negative thus requiring the day be changed to the day before.
    if hr < 0:
        # If true we add 24 to our negative hour value to get our new hour value.
        hr = 24 + hr
        # Check if our timestamp for the 1st of a month
        if dy == 1:
            # If true we set the month to the month prior
            mo = mo - 1
            # Check if the month is Jan so that we can update the year if needed.
            if mo < 1:
                # If true, we set the moth to december, subtract 1 from the year and finally update the day.
                mo = 12
                yr = yr - 1
                dy = last_dy[mo]
            # If the year doesnt change we just update the day using the last day dict.
            else:
                dy = last_dy[mo]
    # Check if adding the offset pushes the hour greater than 11pm thus requiring the day tobe changed to the day after.
    elif hr > 23:
        # If true we calculate our new hour by subtracting 24 from our hour value and add 1 to the day
        hr = hr - 24
        dy = dy + 1
        # if our new day value is greater than the last day of the month we update our month value
        if dy > last_dy[mo]:
            mo = mo + 1
            # If our month is greater than 12, we update our year, set the month to jan and finally set the day to 1.
            if mo > 12:
                mo = 1
                yr = yr + 1
                dy = 1
            # Otherwise we just set the day to 1 if the year doesnt change.
            else:
                dy = 1
    # reference our month dict to get our month name.
    month = months[mo]
    # Convert from 24hour time to AM/PM format.
    if hr > 12:
        hr = hr - 12
        t = "PM"
    elif hr == 0:
        hr = 12
        t = "AM"
    else:
        t = "AM"
    # Finally return our new datetime as a string. 
    return month + " " + str(dy) + ", " + str(yr) + ", " + str(hr) + ":" + mi + " " + t
