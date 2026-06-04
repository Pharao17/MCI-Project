import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MCI Projekt")
        self.geometry("900x700") #größe der Window

        self.show_main_menu()

    # löscht alle widgets im Window
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        tk.Label(self, text="MCI Projekt", font=("Arial", 24)).pack(pady=30)
        #pack fügt das Widget ins Fenster ein

        tk.Button(self, text="Augenbewegungen", width=30, command=self.start_eye_menu).pack(pady=10)
        tk.Button(self, text="Fitts' Law", width=30, command=self.start_fitts_law).pack(pady=10)
        tk.Button(self, text="Auswertung", width=30, command=self.start_analysis).pack(pady=10)

    def start_eye_menu(self):
        self.clear_window()

        title = tk.Label(self, text="Augenbewegungen", font=("Arial", 24))
        title.pack(pady=20)

        tk.Label(self, text="Hier kommt später die Augenbewgungsaufgabe hin.").pack(pady=20)

        tk.Button(self, text="Zurück zum Menü", command=self.show_main_menu).pack(pady=20)


    def start_fitts_law(self):
        self.clear_window()

        title = tk.Label(self, text="Fitts' Law Aufgabe", font=("Arial", 24))
        title.pack(pady=20)

        tk.Label(self, text="Hier kommt später die Fitts' Law Aufgabe hin.").pack(pady=20)

        tk.Button(self, text="Zurück zum Menü", command=self.show_main_menu).pack(pady=20)

    def start_analysis(self):
        self.clear_window()

        title = tk.Label(self, text="Auswertung", font=("Arial", 24))
        title.pack(pady=20)

        tk.Label(self, text="Hier kommt später der Scatterplot hin.").pack(pady=20)

        tk.Button(self, text="Zurück zum Menü", command=self.show_main_menu).pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()