# Worksheet 1.3: Task 3
from pathlib import Path
# Your code for the overall grade classification

# ask for filename of the student file
fname = input('Enter the filename of the student file: -> ')
file_path = Path(__file__).resolve().parent / f"{fname}"
# open the file
with open(file_path, 'r', newline='') as f:
# read in the data, and for each student calculate their average grade and classification

    next(f)

    gradesheet = []

    for line in f:
        score = line.replace('\n', '').split(',')
        score = [cell for cell in score if cell != '']
        gradesheet.append(score)

print(gradesheet)
        
# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}

with open(f'{fname}_out.csv', 'w+') as f:
    for line in gradesheet:
        output = []
        score = [int(x) for x in line[1:]] 
        output.append(line[0])
        grade = (sum(score) / len(score))
        output.append(f'{grade:.2f}')

        if grade < 40:
            output.append('F')
        elif grade < 50:
            output.append('3')
        elif grade < 60:
            output.append('2:2')
        elif grade < 70:
            output.append('2:1')
        else:
            output.append('1')

        f.write(', '.join(map(str, output)) + '\n')

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder