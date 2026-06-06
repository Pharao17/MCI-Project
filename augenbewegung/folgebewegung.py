import math
import random

from .animation import Animation


class Folgebewegung(Animation):
    """Simuliert eine gleichmäßige Smooth-Pursuit-Augenbewegung."""

    def __init__(self, canvas):
        super().__init__(canvas)
        self.radius = 18
        self.speed = 3
        self.x = 0
        self.y = 0
        self.end_x = 0
        self.end_y = 0
        self.opposite_x = 0
        self.opposite_y = 0
        self.target = None
        self.route_name = ""

    def setup(self):
        """Wählt zufällig eine Strecke und erstellt den roten Zielpunkt."""
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        left = self.radius
        right = max(self.radius, width - self.radius)
        top = self.radius
        bottom = max(self.radius, height - self.radius)
        center_x = width / 2
        center_y = height / 2

        # Jede Strecke ist zweimal enthalten, jeweils mit anderer Startrichtung.
        routes = [
            ("links nach rechts", (left, center_y), (right, center_y)),
            ("rechts nach links", (right, center_y), (left, center_y)),
            ("oben nach unten", (center_x, top), (center_x, bottom)),
            ("unten nach oben", (center_x, bottom), (center_x, top)),
            ("oben links nach unten rechts", (left, top), (right, bottom)),
            ("unten rechts nach oben links", (right, bottom), (left, top)),
            ("oben rechts nach unten links", (right, top), (left, bottom)),
            ("unten links nach oben rechts", (left, bottom), (right, top)),
        ]

        self.route_name, start, end = random.choice(routes)
        self.x, self.y = start
        self.end_x, self.end_y = end
        self.opposite_x, self.opposite_y = start

        self.target = self.canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill="red",
            outline=""
        )

    def animate(self):
        """Bewegt den Zielpunkt gleichmäßig entlang der gewählten Strecke."""
        if not self.running or self.target is None:
            return

        distance_x = self.end_x - self.x
        distance_y = self.end_y - self.y
        distance = math.hypot(distance_x, distance_y)

        if distance <= self.speed:
            # Ziel exakt erreichen und anschließend zurückbewegen.
            self.x, self.y = self.end_x, self.end_y
            self.end_x, self.end_y, self.opposite_x, self.opposite_y = (
                self.opposite_x,
                self.opposite_y,
                self.end_x,
                self.end_y,
            )
        elif distance > 0:
            # Normierter Vektor sorgt in jeder Richtung für dieselbe Geschwindigkeit.
            self.x += self.speed * distance_x / distance
            self.y += self.speed * distance_y / distance

        self.canvas.coords(
            self.target,
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius
        )

        # Etwa 60 Bilder pro Sekunde sorgen für eine flüssige Bewegung.
        self.after_id = self.canvas.after(16, self.animate)
