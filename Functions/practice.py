def total_study_minutes(monday, tuesday, wednesday, thursday, friday):
    total = monday+tuesday+wednesday+thursday+friday
    return total
def total_study_hours(monday, tuesday, wednesday, thursday, friday):
    total = total_study_minutes(monday, tuesday, wednesday, thursday, friday)
    total_hours = (total/60)
    return total_hours

def avg_minutes_per_day(monday, tuesday, wednesday, thursday, friday):
    total = total_study_minutes(monday, tuesday, wednesday, thursday, friday)
    avg_minutes_per_day = (total/5)
    return avg_minutes_per_day

def avg_minutes_per_completed_lesson(completed_lessons, monday, tuesday, wednesday, thursday, friday):
    total = total_study_minutes(monday, tuesday, wednesday, thursday, friday)
    avg_minutes_per_completed_lesson = (total/completed_lessons)
    return avg_minutes_per_completed_lesson

def course_percentage_completed(total_lessons, completed_lessons):
    percentage = (completed_lessons/total_lessons)*100
    return percentage

def study_report(name, monday, tuesday, wednesday, thursday, friday, completed_lessons, total_lessons):
    total = total_study_minutes(monday, tuesday, wednesday, thursday, friday)
    total_hours = total_study_hours(monday, tuesday, wednesday, thursday, friday)
    avgminutesperday = avg_minutes_per_day(monday, tuesday, wednesday, thursday, friday)
    avgminutespercompletedlesson = avg_minutes_per_completed_lesson(completed_lessons, monday, tuesday, wednesday, thursday, friday)
    percentage = course_percentage_completed(total_lessons, completed_lessons)
    report = "Name:" + name
    report += "\nTotal minutes studied: " + str(total)
    report += "\nTotal hours studied: " + str(total_hours)
    report += "\nAverage study time per day: " + str(round(avgminutesperday,1))
    report += "\nAverage study time per completed lesson: " + str(round(avgminutespercompletedlesson,1))
    report += "\nCourse progress: " + str(round(percentage, 1))
    return report

print(study_report("Nguyen Duc Duy", 45, 70, 30, 90, 65, 12, 40))



