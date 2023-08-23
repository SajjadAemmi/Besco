import csv
import svgpathtools

# Load SVG file
svg_file = "azg.svg"
output_csv = "output.csv"

# Convert SVG paths to CSV format
with open(output_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["command", "x", "y"])

    paths, attributes = svgpathtools.svg2paths(svg_file)
    for path in paths:
        for segment in path:
            if isinstance(segment, svgpathtools.Line):
                csv_writer.writerow(["line", segment.start.real, -segment.start.imag])
                csv_writer.writerow(["line", segment.end.real, -segment.end.imag])
            elif isinstance(segment, svgpathtools.CubicBezier):
                csv_writer.writerow(["cubic", segment.start.real, -segment.start.imag])
                csv_writer.writerow(["cubic", segment.control1.real, -segment.control1.imag])
                csv_writer.writerow(["cubic", segment.control2.real, -segment.control2.imag])
                csv_writer.writerow(["cubic", segment.end.real, -segment.end.imag])
            # Add more cases for other segment types as needed
