import time

from .animation import Animation


class Vergenzbewegung(Animation):
    def setup(self):
        self.radius = 18
        self.step = 4

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.center_y = height // 2

        self.left_x = width // 2 - 250
        self.right_x = width // 2 + 250

        self.outer_left_x = self.left_x
        self.outer_right_x = self.right_x
        self.inner_left_x = width // 2 - 70
        self.inner_right_x = width // 2 + 70

        self.moving_inward = True
        self.phase_started_at = time.monotonic()

        self.left_eye = self.canvas.create_oval(
            self.left_x - self.radius,
            self.center_y - self.radius,
            self.left_x + self.radius,
            self.center_y + self.radius,
            fill="blue"
        )

        self.right_eye = self.canvas.create_oval(
            self.right_x - self.radius,
            self.center_y - self.radius,
            self.right_x + self.radius,
            self.center_y + self.radius,
            fill="blue"
        )

    def animate(self):
        if not self.running:
            return

        # Nach zwei Sekunden zwischen Konvergenz und Divergenz wechseln.
        if time.monotonic() - self.phase_started_at >= 2:
            self.moving_inward = not self.moving_inward
            self.phase_started_at = time.monotonic()

        if self.moving_inward:
            self.left_x = min(self.left_x + self.step, self.inner_left_x)
            self.right_x = max(self.right_x - self.step, self.inner_right_x)
        else:
            self.left_x = max(self.left_x - self.step, self.outer_left_x)
            self.right_x = min(self.right_x + self.step, self.outer_right_x)

        self.canvas.coords(
            self.left_eye,
            self.left_x - self.radius,
            self.center_y - self.radius,
            self.left_x + self.radius,
            self.center_y + self.radius
        )

        self.canvas.coords(
            self.right_eye,
            self.right_x - self.radius,
            self.center_y - self.radius,
            self.right_x + self.radius,
            self.center_y + self.radius
        )

        self.after_id = self.canvas.after(30, self.animate)
