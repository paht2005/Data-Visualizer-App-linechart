# Data Visualizer App 

![screen](/imgs/screen.png)

This repository contains the implementation of a **Data Visualizer App** built using **Streamlit** and **Matplotlib** for visualizing data from `.csv` or `.xlsx` files. The app allows users to upload data, visualize it in line chart format, filter data based on conditions, and customize the visualization process.

---
## 🗂️ Table of Contents

- [✨ Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [⚙️ Installation](#️-installation)
- [🎯 Usage](#-usage)
- [📄 License](#-license)
- [🤝 Contributing](#-contributing)
- [🧠 Acknowledgements](#-Acknowledgements)

---

## ✨ Features

- **Data Upload:** Users can upload `.csv` and `.xlsx` files for visualization.
- **Data Visualization:** Supports line chart
- **Data Filtering:** Apply conditions to filter the data before visualizing.
- **Dynamic Column Selection:** Automatically detect column names for both X and Y axes.
- **Dark Mode Support:** The app has a dark mode feature for a better user experience.
- **Chart Customization:** Customize chart appearance (labels, titles, colors).

---

## 🗂️ Repository Structure
```
├── imgs/ # Folder for storing images
├── DataVisualizer_app.py # Main Streamlit app script
├── requirements.txt # Python dependencies
└── README.md # Project overview
└── LICENSE

```
---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paht2005/Data-Visualizer-App-linechart.git
   cd Data-Visualizer-App-linechart
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
   ```bash
   streamlit run DataVisualizer_app.py
   ```
---
## 🎯 Usage
- After launching the app with streamlit run DataVisualizer_app.py, the app will load in your browser.
- You can upload .csv or .xlsx files by clicking the upload button.
- Choose the columns for the X and Y axes to generate the desired chart.
- Apply filters to the data for more specific visualizations.
- **Demo:**
  ![deploy1](/imgs/deploy1.png)
  ![deploy2](/imgs/deploy2.png)

---
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
## 🤝 Contributing
I welcome contributions to improve this project! Feel free to submit pull requests or open issues for discussion.
Contact for work: **Nguyễn Công Phát** – congphatnguyen.work@gmail.com

---
## 🧠 Acknowledgements
- **Streamlit** - For creating an amazing platform to build data apps.
- **Matplotlib** - For powerful and customizable visualizations.
