# 🖥️ System Performance Analyzer

A cross-platform desktop application built using **Python**, **Tkinter**, and **Matplotlib** to monitor real-time system performance, including CPU usage, memory consumption, disk I/O, and more — optimized for **macOS**.

---

## 🚀 Features

- ✅ Real-time CPU, Memory, and Disk usage monitoring  
- ✅ Dynamic Graph Plotting with Matplotlib  
- ✅ Responsive Tkinter GUI with splash screen  
- ✅ Data logging and export in JSON format  
- 🔄 Alert system for performance thresholds (in progress)  
- ⏳ Settings panel for user preferences (pending)

---

## 📸 Screenshots

> <img width="328" alt="image" src="https://github.com/user-attachments/assets/461a08d4-780c-4e2b-86c5-d02a072238c0" />


---

## 🧱 Tech Stack

- **Frontend**: Tkinter (Python GUI)
- **Backend**: Python + psutil + JSON + Matplotlib
- **OS Compatibility**: macOS (tested), Linux (basic support), Windows (coming soon)

---

## 🧪 How to Run

```bash
# Clone the repo
git clone https://github.com/your-username/System-Performance-Analyzer.git
cd System-Performance-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
'''

# Project Structure
- System-Performance-Analyzer/
- │
- ├── UI.py                  # Main GUI window
- ├── monitor.py             # Performance monitoring logic
- ├── graph_plot.py          # Real-time graph plotting
- ├── splash.py              # Splash screen code
- ├── utils/                 # Helper functions and data storage
- └── assets/                # Logos, icons, images
