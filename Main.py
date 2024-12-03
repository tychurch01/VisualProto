from VisualArrayAPI import VisualArray

def main():

    visualizer = VisualArray(rows=5, cols=5, cell_size=0.15, border_width=0.01)


    visualizer.update_cell(0, 0, (1, 0, 0))
    visualizer.update_cell(1, 1, (0, 1, 0))
    visualizer.update_cell(2, 2, (0, 0, 1))

    visualizer.update_cell(2, 3, (1, 1, 0))
    visualizer.update_cell(4, 4, (0, 1, 1))  

    visualizer.run()  # The run method contains the event loop and the rendering process

if __name__ == "__main__":
    main()
