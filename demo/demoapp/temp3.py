# ans = 0
# last_day_miss = 0


# def probability_of_attendance(curr_attendance, missing_attendance, number_of_days, attendance, miss_flag):
#     global ans
#     global last_day_miss
#     if missing_attendance >= 4:
#         miss_flag = True
#         return

#     if number_of_days == attendance:
#         if miss_flag:
#             return
#         if curr_attendance == 'A':
#             last_day_miss += 1
#         ans += 1
#         return

#     probability_of_attendance(curr_attendance="P",
#                               missing_attendance=0, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
#     probability_of_attendance(curr_attendance="A",
#                               missing_attendance=missing_attendance+1, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
#     return


# probability_of_attendance("", 0, 0, 5, False)
# print(str(last_day_miss)+'/'+str(ans))









# attend_class = 0
# graduation_miss = 0


# def probability_of_attendance(curr_attendance, missing_attendance, attendance, miss_flag, graduation_miss, attend_class):
#     if missing_attendance >= 4:
#         miss_flag = True
#         return

#     if attendance == 0:
#         if miss_flag:
#             return
#         if curr_attendance == 'A':
#             graduation_miss = graduation_miss + 1
#         attend_class += 1
#         return

#     probability_of_attendance(curr_attendance = "P",
#                               missing_attendance = 0, attendance = attendance - 1, miss_flag = miss_flag, graduation_miss = graduation_miss, attend_class = attend_class)
#     probability_of_attendance(curr_attendance = "A",
#                               missing_attendance = missing_attendance + 1, attendance = attendance - 1, miss_flag = miss_flag, graduation_miss = graduation_miss, attend_class = attend_class)
#     return


# probability_of_attendance("", 0, 5, False, 0, 0)
# print(str(graduation_miss)+'/'+str(attend_class))



ans = 0
last_day_miss = 0

class College():
    def __init__(self, no_of_days):
        self.curr_attendance = ""
        self.missing_attendance = 0
        self.attendance = no_of_days
        self.number_of_days = 0
        self.miss_flag = False
        self.ans = 0
        self.last_day_miss = 0
        self.probability_of_attendance(self.curr_attendance, self.missing_attendance,\
                                       self.number_of_days, self.attendance, self.miss_flag)
    
    def probability_of_attendance(self, curr_attendance, missing_attendance, number_of_days, attendance, miss_flag):
        if missing_attendance >= 4:
            miss_flag = True
            return

        if number_of_days == attendance:
            if miss_flag:
                return
            if curr_attendance == 'A':
                self.last_day_miss += 1
            self.ans += 1
            return

        self.probability_of_attendance(curr_attendance = "P",
                                missing_attendance=0, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
        self.probability_of_attendance(curr_attendance="A",
                                missing_attendance=missing_attendance+1, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
        return
    
    def 

no_of_days = int(input("Enter the number of days: "))
college_obj = College(no_of_days)
print(str(college_obj.last_day_miss)+'/'+str(college_obj.ans))