def time_convert(time, offset):
    months = {1: "January", 2: "February", 3: "March",
              4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September",
              10: "October", 11: "November", 12: "December"}
    last_dy = {1: 31, 2: 28, 3: 31, 4: 30,
               5: 31, 6: 30, 7: 31, 8: 31,
               9: 30, 10: 31, 11: 30, 12: 31}
    yr = int(time[0:4])
    mo = int(time[5:7])
    dy = int(time[8:10])
    hr = int(time[12:14])
    mi = time[15:17]
    hr = hr + offset
    if yr % 4 == 0:
        last_dy[2] = 29
    if hr < 0:
        hr = 24 + hr
        if dy == 1:
            mo = mo - 1
            if mo < 1:
                mo = 12
                yr = yr - 1
                dy = last_dy[mo]
            else:
                dy = last_dy[mo]
    elif hr > 23:
        hr = 24 - hr
        dy = dy + 1
        if dy > last_dy[mo]:
            mo = mo + 1
            if mo > 12:
                mo = 1
                yr = yr + 1
                dy = 1
            else:
                dy = 1
    month = months[mo]
    if hr > 12:
        hr = hr - 12
        t = "PM"
    elif hr == 0:
        hr = 12
        t = "AM"
    else:
        t = "AM"
    return month + " " + str(dy) + ", " + str(yr) + ", " + str(hr) + ":" + mi + " " + t
