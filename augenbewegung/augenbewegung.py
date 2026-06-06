import tkinter as tk
from .sakkaden import Sakkaden
from .vergenzbewegung import Vergenzbewegung


class AugenBewegung(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(anchor="center")

        #Titel
        tk.Label(
            main_frame,
            text="Augenbewegungen",
            font=("Arial", 24)
        ).pack(pady=20)

        #Hier kommt die Animation
        self.canvas = tk.Canvas(
            main_frame,
            width=1400,
            height=700,
            bg="white"
        )
        self.canvas.pack()

        #Controls abtrennen von der Canvas
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)

        #Buttons von anmachen der Animationen trennen
        animation_buttons = tk.Frame(button_frame)
        animation_buttons.pack()

        self.sakkaden = Sakkaden(self.canvas)
        self.vergenzbewegung = Vergenzbewegung(self.canvas)
        self.active_animation = None

        tk.Button(
            animation_buttons,
            text="Sakkaden",
            command=self.start_sakkaden
        ).pack(side="left", padx=20)

        tk.Button(
            animation_buttons,
            text="Vergenzbewegung",
            command=self.start_vergenzbewegung
        ).pack(side="left", padx=20)

        tk.Button(
            animation_buttons,
            text="Smooth Pursuit"
        ).pack(side="left", padx=20)

        tk.Button(
            animation_buttons,
            text="Animation stoppen",
            command=self.stop_animation
        ).pack(side="left", padx=20)

        tk.Button(
            button_frame,
            text="Zurück zum Menü",
            command=app.show_main_menu
        ).pack(pady=15)

    def start_sakkaden(self):
        self.start_animation(self.sakkaden)

    def start_vergenzbewegung(self):
        self.start_animation(self.vergenzbewegung)

    def start_animation(self, animation):
        if self.active_animation is not None:
            self.active_animation.stop()

        self.active_animation = animation
        self.active_animation.start()

    def stop_animation(self):
        if self.active_animation is not None:
            self.active_animation.stop()
            self.active_animation = None
