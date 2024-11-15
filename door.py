# Draw the door
context.move_to(240, 279)
context.line_to(240, 170)
context.line_to(290, 168)
context.line_to(290, 276)
context.close_path()
context.set_source_rgb(0.48, 0.25, 0)
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

# Set up line style for the squiggly line
context.set_line_width(2)
context.set_source_rgb(0, 0, 0)  # Black color for the squiggly line

# Draw the squiggly line using Bezier curves
start_x, start_y = 270, 180 # Starting point
context.move_to(start_x, start_y)

# Parameters for squiggle pattern
squiggle_height = 10  # Height of each "wave"
num_waves = 7  # Number of waves in the squiggle

for i in range(num_waves):
    # Alternate between moving right and left
    if i % 2 == 0:
        control_x1 = start_x + 20
        control_x2 = start_x + 20
    else:
        control_x1 = start_x - 20
        control_x2 = start_x - 20

    control_y1 = start_y + squiggle_height / 2
    control_y2 = start_y + squiggle_height / 2
    end_x = start_x + 5
    end_y = start_y + squiggle_height

    # Create the curve
    context.curve_to(control_x1, control_y1, control_x2, control_y2, end_x, end_y)

    # Update starting point for the next wave
    start_y += squiggle_height

# Stroke the path to make the squiggly line visible
context.stroke()

# Draw the door knob
context.set_source_rgb(0.2, 0.2, 0)  # Darker color for knob
context.arc(249, 225, 4, 0, 2 * 3.1416)  # Position and size of the knob
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()
