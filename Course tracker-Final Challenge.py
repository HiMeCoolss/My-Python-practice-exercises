def percentage_completed(completed_lessons, total_lessons):
    percentage=(completed_lessons/total_lessons)*100
    return percentage

def total_time_studied_in_hours(monday, tuesday, wednesday, thursday, friday):
    total_time_in_hours=(monday + tuesday + wednesday + thursday + friday)/60
    return total_time_in_hours

def average_minutes_per_lesson(monday, tuesday, wednesday, thursday, friday, completed_lessons):
    total_time_in_hours=total_time_studied_in_hours(monday, tuesday, wednesday, thursday, friday)
    average_minutes=(total_time_in_hours*60)/completed_lessons
    return average_minutes

def estimated_hours_remaining(monday, tuesday, wednesday, thursday, friday, total_lessons, completed_lessons):
    average_minutes=average_minutes_per_lesson(monday, tuesday, wednesday, thursday, friday, completed_lessons)
    hours_remaining=((total_lessons-completed_lessons)*average_minutes)/60
    return hours_remaining

def calculate_lessons_needed_per_day(remaining_days, total_lessons, completed_lessons):
    lessons_needed_per_day=((total_lessons-completed_lessons)/remaining_days)
    if lessons_needed_per_day == int(lessons_needed_per_day):
        return int(lessons_needed_per_day)
    else:
        return int(lessons_needed_per_day)+1

def progress_report(name, monday, tuesday, wednesday, thursday, friday, completed_lessons, total_lessons, remaining_days):
    percentage=percentage_completed(completed_lessons, total_lessons)
    total_time_in_hours=total_time_studied_in_hours(monday, tuesday, wednesday, thursday, friday)
    average_minutes=average_minutes_per_lesson(monday, tuesday, wednesday, thursday, friday, completed_lessons)
    remaining_hours=estimated_hours_remaining(monday, tuesday, wednesday, thursday, friday, total_lessons, completed_lessons)
    lessons_needed_per_day=calculate_lessons_needed_per_day(remaining_days, total_lessons, completed_lessons)
    report="Student: " + name
    report+="\nPercentage completed: " + str(percentage)
    report+="\nTotal time spent studying: " + str(total_time_in_hours)
    report+="\nAverage minutes per lesson: " + str(average_minutes)
    report+="\nRemamining hours: " + str(remaining_hours)
    report+="\nLessons needed per day: " + str(lessons_needed_per_day)
    return report

a=progress_report("mommy", 90, 75, 120, 45, 60, 20, 80, 15)
print(a)
