from sys import argv
import csv
import random

# global list to hold student data as dictionaries
students = []


# AI was used to help me with parts of this task


# list of weeks (week1 to week13 but skip week6)
weeks = [f"week{i}" for i in range(1,14) if i != 6]

def read_csv(filename):
    # read the csv file and save rows
    global students
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            students = list(reader)  # load all rows as dicts
    except FileNotFoundError: # exceptions
        print(f"error: file '{filename}' not found")
        exit(1)

def populate_scores():
    # fill empty week scores with random numbers 0-3
    for student in students:
        for w in weeks:
            val = student.get(w, "").strip()
            if val == "":
                # if empty, put a random score 0 to 3 as string
                student[w] = str(random.randint(0,3))
            else:
                # keep the existing value (as string)
                student[w] = val

def calculate_all():
    # for each student calculate total and average and save in dict
    for student in students:
        scores = []
        for w in weeks:
            try:
                # convert score to int
                s = int(student[w])
            except ValueError:
                s = 0  # if conversion fails, treat as 0
            scores.append(s)
        total = calculate_total(scores)
        average = calculate_average(scores)
        student["Total Points"] = total
        student["Average Points"] = average

def calculate_total(scores):
    # scores is a list of integers for the weeks
    # sort descending and add up best 10 scores only
    scores_sorted = sorted(scores, reverse=True)
    return sum(scores_sorted[:10])

def calculate_average(scores):
    # calculate average of all scores given
    if len(scores) == 0:
        return 0
    return round(sum(scores) / len(scores), 2)

def write_csv(filename):
    # write all student data to new csv file
    fieldnames = list(students[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def print_analysis():
    # print average points by stream and by week
    streams = {"A": [], "B": []}
    week_totals = {w: [] for w in weeks}

    for student in students:
        stream = student.get("Stream", "").strip().upper()
        try:
            avg = float(student["Average Points"])
        except:
            avg = 0
        if stream in streams:
            streams[stream].append(avg)

        for w in weeks:
            try:
                val = int(student[w])
            except:
                val = 0
            week_totals[w].append(val)

    print("\naverage points by stream:")
    for stream, vals in streams.items():
        if len(vals) > 0:
            avg = round(sum(vals)/len(vals), 2)
        else:
            avg = 0
        print(f"  stream {stream}: {avg} points")

    print("\naverage points per week:")
    for w in weeks:
        vals = week_totals[w]
        if len(vals) > 0:
            avg = round(sum(vals)/len(vals), 2)
        else:
            avg = 0
        print(f"  {w}: {avg} points")

if __name__ == "__main__":

    script, filename = argv

    print("open file:", filename)

    read_csv(filename)
    populate_scores()
    calculate_all()
    user_name = "nina"      #change my name

    # create new filename with user name
    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)       # save results to new csv
    print("new file written:", newname)

    print_analysis()         # print some averages for info
