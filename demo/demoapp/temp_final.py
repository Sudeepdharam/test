class University():
    def __init__(self, no_of_days):
        '''
        Intialization of all the required variables
        '''
        self.current_attendance = ""
        self.absence_attendance_counter = 0
        self.total_university_days = no_of_days
        self.days_counter = 0
        self.absent_flag = False
        self.count_ways_to_attend_classes = 0
        self.count_ways_to_miss_graduation = 0
        self.calculate_attendance_probability(self.current_attendance, self.days_counter,
                                              self.absence_attendance_counter, self.total_university_days,
                                              self.absent_flag)
    
    def calculate_attendance_probability(self, current_attendance, absence_attendance_counter,\
                                         days_counter, total_university_days, absent_flag):
        """
        Calculation of number of ways to attend college and
        probability of missing graduation
        """
        if absence_attendance_counter < 4:
            absent_flag = False
        else:
            absent_flag =  True
            return

        if days_counter == total_university_days:
            if absent_flag == True:
                return
            if current_attendance == 'A':
                self.count_ways_to_miss_graduation = self.count_ways_to_miss_graduation + 1
            self.count_ways_to_attend_classes = self.count_ways_to_attend_classes+ 1
            return
        else:
            pass
        
        # Checking the probablity of present days
        self.calculate_attendance_probability(current_attendance = "P", 
                                              days_counter = days_counter+1,
                                              absence_attendance_counter = 0,
                                              total_university_days = total_university_days,
                                              absent_flag = absent_flag)
        # Checking the probability of absent days
        self.calculate_attendance_probability(current_attendance = "A", 
                                              days_counter = days_counter+1,
                                              absence_attendance_counter = absence_attendance_counter+1,
                                              total_university_days = total_university_days,
                                              absent_flag = absent_flag)
        return
    
    def get_probability_result(self):
        """
        Print the output as per requirement
        """
        print("for {0} days: {1}/{2}".format(self.total_university_days,
                                              str(self.count_ways_to_miss_graduation),
                                              str(self.count_ways_to_attend_classes)))


no_of_days = int(input("Enter the number of days: "))
university_obj = University(no_of_days)
university_obj.get_probability_result()


# Two Options per Day:
# Each day presents two choices: attend (present) or skip (absent) class.
# Initially, lets explore the probability of attending class recursively while considering constraints(not missing more than 4 days in a row).
# Then, backtrack to explore the probability of missing class recursively.
# Constraint Checks:
# Track the absence-attendance counter to ensure that missing attendance doesn't exceed 4 consecutive days.
# If the counter exceeds 4, skip further probability calculations.
# Recursive Call Conditions:
# For each recursive call, check if the absence-attendance counter is within the constraint.
# If satisfied, proceed to calculate the probability of attending or missing class.
# Graduation Consideration:
# If missing attendance for a given day satisfies the conditions of missing graduation, count it as one of the ways.