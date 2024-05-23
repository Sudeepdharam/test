ans = 0
last_day_miss = 0


def probability_of_attendance(prev_attendance, curr_attendance, missing_attendance, number_of_days, attendance, miss_flag):
    global ans
    global last_day_miss
    if missing_attendance >= 4:
        miss_flag = True
        return

    if number_of_days == attendance:
        #attendance_str = prev_attendance + curr_attendance
        if miss_flag:
            return
        if curr_attendance == 'A':
            last_day_miss += 1
        ans += 1
        return

    probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="P",
                              missing_attendance=0, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
    probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="A",
                              missing_attendance=missing_attendance+1, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
    return


probability_of_attendance("", "", 0, 0, 6, False)
print(str(last_day_miss)+'/'+str(ans))