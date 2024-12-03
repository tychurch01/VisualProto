import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class VisualArray:
    def __init__(self, rows=5, cols=5, cell_size=0.1, border_width=0.01):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.border_width = border_width
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]  # Empty grid


        if not glfw.init():
            raise Exception("GLFW cannot be initialized")

        self.window = glfw.create_window(800, 600, "OpenGL Grid", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window cannot be created")

        glfw.make_context_current(self.window)


        glClearColor(1, 1, 1, 1)  # White background
        glOrtho(0, 1, 0, 1, -1, 1)  # 2D orthographic view

    def update_cell(self, row, col, color=(0, 0, 0)):

        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = color

    def draw_grid(self):

        for row in range(self.rows):
            for col in range(self.cols):
                color = self.grid[row][col] if self.grid[row][col] else (1, 1, 1)  # Default to white
                self.draw_cell(row, col, color)
                self.draw_cell_border(row, col)  # Draw the border around each cell

    def draw_cell(self, row, col, color):

        x = col * self.cell_size
        y = 1 - (row + 1) * self.cell_size

        glColor3fv(color)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + self.cell_size, y)
        glVertex2f(x + self.cell_size, y + self.cell_size)
        glVertex2f(x, y + self.cell_size)
        glEnd()

    def draw_cell_border(self, row, col):

        x = col * self.cell_size
        y = 1 - (row + 1) * self.cell_size

        glColor3fv((0, 0, 0))
        glLineWidth(3)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x, y)
        glVertex2f(x + self.cell_size, y)
        glVertex2f(x + self.cell_size, y + self.cell_size)
        glVertex2f(x, y + self.cell_size)
        glEnd()

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT)
        self.draw_grid()
        glfw.swap_buffers(self.window)

    def run(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            self.render()


            glfw.swap_interval(1)

        glfw.terminate()
