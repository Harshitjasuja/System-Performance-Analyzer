import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.font import Font
import platform
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
import datetime
import os

class SystemAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Performance Analyzer - Architechs")
        self.root.geometry("1280x800")
        self.root.configure(bg='#f5f5f5')
        self.dark_mode = False

        self.create_styles()
        self.create_menu()
        self.create_tabs()
        self.update_metrics()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TNotebook.Tab', font=('Helvetica', 12))
        self.style.configure('TFrame', background='#f5f5f5')
        self.style.configure('Treeview.Heading', font=('Helvetica', 10, 'bold'))
        self.style.configure('Treeview', font=('Helvetica', 9))

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
        menu_bar.add_cascade(label="View", menu=view_menu)

        export_menu = tk.Menu(menu_bar, tearoff=0)
        export_menu.add_command(label="Export Report", command=self.export_report)
        menu_bar.add_cascade(label="Export", menu=export_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About Us", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)

        self.cpu_tab = ttk.Frame(self.notebook)
        self.memory_tab = ttk.Frame(self.notebook)
        self.disk_tab = ttk.Frame(self.notebook)
        self.process_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.cpu_tab, text="CPU")
        self.notebook.add(self.memory_tab, text="Memory")
        self.notebook.add(self.disk_tab, text="Disk")
        self.notebook.add(self.process_tab, text="Processes")
        self.notebook.pack(expand=True, fill="both")

        self.create_cpu_tab()
        self.create_memory_tab()
        self.create_disk_tab()
        self.create_process_tab()

        footer = tk.Label(self.root, text="System Performance Analyzer by Architechs | SE(OS)-VI-T250", font=("Arial", 10), bg="#f5f5f5")
        footer.pack(side="bottom", fill="x")

    def create_cpu_tab(self):
        self.cpu_label = tk.Label(self.cpu_tab, text="CPU Usage", font=("Helvetica", 16), bg="#f5f5f5")
        self.cpu_label.pack(pady=10)
        self.cpu_usage = ttk.Progressbar(self.cpu_tab, orient="horizontal", length=600, mode="determinate")
        self.cpu_usage.pack(pady=10)

        self.cpu_figure, self.cpu_ax = plt.subplots()
        self.cpu_ax.set_title("CPU Usage Over Time")
        self.cpu_ax.set_xlabel("Time")
        self.cpu_ax.set_ylabel("Usage (%)")
        self.cpu_line, = self.cpu_ax.plot([], [])
        self.cpu_ax.set_ylim(0, 100)
        self.cpu_canvas = FigureCanvasTkAgg(self.cpu_figure, master=self.cpu_tab)
        self.cpu_canvas_widget = self.cpu_canvas.get_tk_widget()
        self.cpu_canvas_widget.pack(fill="both", expand=True)
        self.cpu_time_data = []
        self.cpu_usage_data = []

    def create_memory_tab(self):
        self.memory_label = tk.Label(self.memory_tab, text="Memory Usage", font=("Helvetica", 16), bg="#f5f5f5")
        self.memory_label.pack(pady=10)
        self.memory_usage = ttk.Progressbar(self.memory_tab, orient="horizontal", length=600, mode="determinate")
        self.memory_usage.pack(pady=10)

        self.memory_figure, self.memory_ax = plt.subplots()
        self.memory_ax.set_title("Memory Usage Over Time")
        self.memory_ax.set_xlabel("Time")
        self.memory_ax.set_ylabel("Usage (%)")
        self.memory_line, = self.memory_ax.plot([], [])
        self.memory_ax.set_ylim(0, 100)
        self.memory_canvas = FigureCanvasTkAgg(self.memory_figure, master=self.memory_tab)
        self.memory_canvas_widget = self.memory_canvas.get_tk_widget()
        self.memory_canvas_widget.pack(fill="both", expand=True)
        self.memory_time_data = []
        self.memory_usage_data = []

    def create_disk_tab(self):
        self.disk_label = tk.Label(self.disk_tab, text="Disk Usage", font=("Helvetica", 16), bg="#f5f5f5")
        self.disk_label.pack(pady=10)
        self.disk_usage = ttk.Progressbar(self.disk_tab, orient="horizontal", length=600, mode="determinate")
        self.disk_usage.pack(pady=10)

        self.disk_figure, self.disk_ax = plt.subplots()
        self.disk_ax.set_title("Disk Usage Over Time")
        self.disk_ax.set_xlabel("Time")
        self.disk_ax.set_ylabel("Usage (%)")
        self.disk_line, = self.disk_ax.plot([], [])
        self.disk_ax.set_ylim(0, 100)
        self.disk_canvas = FigureCanvasTkAgg(self.disk_figure, master=self.disk_tab)
        self.disk_canvas_widget = self.disk_canvas.get_tk_widget()
        self.disk_canvas_widget.pack(fill="both", expand=True)
        self.disk_time_data = []
        self.disk_usage_data = []

    def create_process_tab(self):
        self.proc_label = tk.Label(self.process_tab, text="Running Processes", font=("Helvetica", 16), bg="#f5f5f5")
        self.proc_label.pack(pady=10)

        self.proc_tree = ttk.Treeview(self.process_tab, columns=("PID", "Name", "CPU", "Memory"), show="headings")
        self.proc_tree.heading("PID", text="PID")
        self.proc_tree.heading("Name", text="Name")
        self.proc_tree.heading("CPU", text="CPU %")
        self.proc_tree.heading("Memory", text="Memory %")
        self.proc_tree.pack(fill="both", expand=True)

        kill_btn = ttk.Button(self.process_tab, text="Terminate Process", command=self.terminate_