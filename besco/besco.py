from typing import Any
import turtle
import svgpathtools


class Besco:
    def __init__(self):
        pass

    @staticmethod
    def draw(svg_file_path):
        # Load SVG file
        paths, attributes = svgpathtools.svg2paths(svg_file_path)

        # Initialize Turtle graphics
        turtle.speed(0)
        turtle.title("Drawing Besco")
        turtle.setup(420, 420)

        # Convert SVG paths to Turtle commands
        for path, attrib in zip(paths, attributes):
            if 'stroke' in attrib:
                turtle.pencolor(attrib['stroke'])  # Set pen color based on SVG stroke attribute
            else:
                turtle.pencolor('black')  # Default pen color if stroke attribute is missing
                
            if 'fill' in attrib:
                turtle.fillcolor(attrib['fill'])  # Set fill color based on SVG fill attribute
                turtle.begin_fill()  # Start filling
                
            for segment in path:
                if isinstance(segment, svgpathtools.Line):
                    turtle.penup()
                    turtle.goto(segment.start.real - 210, -segment.start.imag + 210)
                    turtle.pendown()
                    turtle.goto(segment.end.real - 210, -segment.end.imag + 210)
                elif isinstance(segment, svgpathtools.CubicBezier):
                    turtle.penup()
                    turtle.goto(segment.start.real - 210, -segment.start.imag + 210)
                    turtle.pendown()
                    turtle.goto(segment.control1.real - 210, -segment.control1.imag + 210)
                    turtle.goto(segment.control2.real - 210, -segment.control2.imag + 210)
                    turtle.goto(segment.end.real - 210, -segment.end.imag + 210)
                # Add more cases for other segment types as needed

            if 'fill' in attrib:
                turtle.end_fill()  # End filling

        # Keep the window open until the user closes it
        print("done")
        turtle.done()



def main():
    Besco.draw("besco/azg.svg")


if __name__ == '__main__':
    main()
