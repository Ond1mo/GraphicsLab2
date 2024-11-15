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