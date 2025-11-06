import tkinter as tk
import random

WIDTH = 600
HEIGHT = 450
WASTE_COUNT = 12

class RoadCleanerRobot:
    def __init__(self, canvas, status_label):
        self.canvas = canvas
        self.status_label = status_label
        self.waste_items = []
        self.cars = []
        self.active = False
        self.after_id_move = None
        self.after_id_cars = None
        self.draw_map()
        self.place_waste()
        self.create_robot()
        self.create_vehicles()

    def draw_map(self):
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#d0e8ff", width=0)
        self.canvas.create_rectangle(100, 0, 200, HEIGHT, fill="gray", outline="black")
        self.canvas.create_rectangle(0, 200, WIDTH, 300, fill="gray", outline="black")
        self.canvas.create_text(150, 20, text="Main Road", fill="white", font=("Arial", 12, "bold"))
        self.canvas.create_text(80, 230, text="Cross Road", fill="white", font=("Arial", 12, "bold"))

    def place_waste(self):
        self.waste_items.clear()
        for _ in range(WASTE_COUNT):
            if random.choice([True, False]):
                x = random.randint(120, 180)
                y = random.randint(10, HEIGHT - 24)
            else:
                x = random.randint(10, WIDTH - 24)
                y = random.randint(220, 276)
            trash = self.canvas.create_oval(x, y, x+14, y+14, fill="brown", outline="")
            self.waste_items.append(trash)

    def create_robot(self):
        self.rx, self.ry = 150, 20
        self.robot = self.canvas.create_oval(self.rx, self.ry, self.rx+20, self.ry+20, fill="blue", outline="black")

    def create_vehicles(self):
        for _ in range(3):
            x = random.randint(0, WIDTH)
            y = random.choice([225, 260])
            car = self.canvas.create_rectangle(x, y, x+30, y+15, fill="red", outline="black")
            self.cars.append(car)
        self.animate_cars()

    def animate_cars(self):
        for car in self.cars:
            x1, y1, x2, y2 = self.canvas.coords(car)
            x1 += 3
            x2 += 3
            if x1 > WIDTH:
                x1, x2 = -40, -10
            self.canvas.coords(car, x1, y1, x2, y2)
        self.after_id_cars = self.canvas.after(80, self.animate_cars)

    def start_cleaning(self):
        if not self.active:
            self.active = True
            self.move_robot()

    def move_robot(self):
        if not self.active:
            return
        if not self.waste_items:
            self.status_label.config(text="Roads are Clean Now! Our team visited and collected the trash.")
            self.active = False
            return
        rx_center = self.rx
        ry_center = self.ry
        nearest_item = None
        nearest_dist2 = 10**12
        for item in self.waste_items:
            tx1, ty1, tx2, ty2 = self.canvas.coords(item)
            tx, ty = tx1, ty1
            dx = tx - rx_center
            dy = ty - ry_center
            dist2 = dx*dx + dy*dy
            if dist2 < nearest_dist2:
                nearest_dist2 = dist2
                nearest_item = item
        tx1, ty1, tx2, ty2 = self.canvas.coords(nearest_item)
        tx, ty = tx1, ty1
        step = 2
        if abs(self.rx - tx) > 1:
            self.rx += step if self.rx < tx else -step
        if abs(self.ry - ty) > 1:
            self.ry += step if self.ry < ty else -step
        self.canvas.coords(self.robot, self.rx, self.ry, self.rx+20, self.ry+20)
        if abs(self.rx - tx) < 10 and abs(self.ry - ty) < 10:
            self.canvas.delete(nearest_item)
            self.waste_items.remove(nearest_item)
        self.after_id_move = self.canvas.after(80, self.move_robot)

def run_app():
    root = tk.Tk()
    root.title("Road Cleaner Robot")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(pady=10)
    status = tk.Label(root, text="Waiting for consumer feedback...", font=("Arial", 12))
    status.pack()
    robot = RoadCleanerRobot(canvas, status)
    return root, robot, status
