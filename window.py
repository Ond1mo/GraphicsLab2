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
context.line_to(160, 250)
context.line_to(160, 160)
context.close_path()
context.set_source_rgb(0.8, 0.8, 0.8)  # Light grey
context.fill()

# Draw the front wall
context.move_to(220, 150)
context.line_to(220, 280)
context.line_to(400, 270)
context.line_to(400, 150)
context.line_to(310, 80)
context.close_path()
context.set_source_rgb(0.7, 0.7, 0.7)  # Slightly darker grey
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
context.set_source_rgb(0.65,0.78,0.9)
context.fill()

context.move_to(360, 187)
context.line_to(385, 187)
context.line_to(385, 238)
context.line_to(360,238)
context.close_path()
context.set_source_rgb(0.65,0.78,0.9)
context.fill()
