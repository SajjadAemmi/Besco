import csv
import turtle

def draw_svg_from_csv(csv_file):
    turtle.speed(0)  # Adjust speed as needed

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip header row
        next(csv_reader)
        for row in csv_reader:
            command, x, y = row
            x, y = float(x), float(y)

            if command == "line":
                turtle.pendown()
                turtle.goto(x, y)
            elif command == "cubic":
                turtle.pendown()
                turtle.goto(x, y)
            # Add more cases for other command types as needed
            else:
                turtle.penup()
                turtle.goto(x, y)

    turtle.done()

# Replace 'output.csv' with the name of the CSV file generated in the first step
draw_svg_from_csv('output.csv')
