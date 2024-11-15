import cairo

# Set up the surface and context
WIDTH, HEIGHT = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set the background color
context.set_source_rgb(1, 1, 1)  # White
context.paint()


# Draw the left wall (angled for 3D effect)
context.move_to(220, 150)
context.line_to(220, 280)
context.line_to(140, 250)
context.line_to(140, 150)
context.close_path()
context.set_source_rgb(0.8, 0.8, 0.8)  # Light grey
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

# Draw the front wall
context.move_to(220, 150)
context.line_to(220, 280)
context.line_to(400, 270)
context.line_to(400, 150)
context.line_to(310, 80)
context.close_path()
context.set_source_rgb(0.7, 0.7, 0.7)  # Slightly darker grey
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

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

# Draw the left wall windows
context.move_to(210, 190)
context.line_to(210, 250)
context.line_to(185, 240)
context.line_to(185, 187)
context.close_path()
context.set_source_rgb(0.48, 0.25, 0)
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()
context.move_to(197, 190)
context.line_to(197, 245)
context.stroke()

context.move_to(207, 195)
context.line_to(207, 245)
context.line_to(200, 242)
context.line_to(200, 193)
context.close_path()
context.set_source_rgb(0,1,1)
context.fill()

context.move_to(194, 193)
context.line_to(194, 240)
context.line_to(188, 237)
context.line_to(188, 192)
context.close_path()
context.set_source_rgb(0,1,1)
context.fill()

#Front wall window
context.move_to(320, 183)
context.line_to(390, 182)
context.line_to(389, 244)
context.line_to(320, 245)
context.close_path()
context.set_source_rgb(0.45, 0.25, 0)
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.set_line_width(2)
context.stroke()
context.move_to(355, 183)
context.line_to(356, 244)
context.set_line_width(2)
context.stroke()
context.move_to(325, 187)
context.line_to(350, 187)
context.line_to(350, 238)
context.line_to(325,238)
context.close_path()
context.set_source_rgb(0,1,1)
context.fill()

context.move_to(360, 187)
context.line_to(385, 187)
context.line_to(385, 238)
context.line_to(360,238)
context.close_path()
context.set_source_rgb(0,1,1)
context.fill()

# Save the result
surface.write_to_png("3d_house.png")
print("3D house image with perspective saved as '3d_house_with_perspective.png'")