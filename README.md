# 5800 Final Project

## Project Overview

This repository contains code and data for the 5800 Final Project

---

## Project Structure
```
fake-review-detection/
├── data/
│   ├── processed/                  # Cleaned and preprocessed datasets
│   │   ├── hotel_final_clean.csv   # Final cleaned hotel reviews dataset
│   │   └── product_final_clean.csv # Final cleaned product reviews dataset
│   └── raw/                        # Original, unprocessed data files
│       ├── dosc_hotel_reviews.csv  # Raw hotel reviews from data source
│       └── kaggle_fake_reviews.csv # Raw fake reviews from Kaggle
├── notebooks/                      # Jupyter notebooks for analysis and experimentation
│   └── 01_data_exploration.ipynb   # Initial data exploration and analysis
├── src/                           # Source code modules
│   ├── __init__.py                # Makes src a Python package
│   └── data_processing.py         # Data cleaning and preprocessing functions
├── .gitignore                     # Git ignore rules
└── README.md                      # Project documentation
```

## Directory Descriptions

### `/data`
Contains all datasets used in the project:
- **`raw/`**: Original, unmodified data files as downloaded from sources
- **`processed/`**: Cleaned and preprocessed data ready for model training

### `/notebooks`
Jupyter notebooks for exploratory data analysis, experimentation, and prototyping:
- `01_data_exploration.ipynb`: Initial analysis of the review datasets

### `/src`
Python source code modules:
- `data_processing.py`: Functions for data cleaning, preprocessing, and feature engineering
- `__init__.py`: Package initialization file

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JasmineH-H/5800FinalProject.git
```

### 2. Create and activate a Python virtual environment (recommended)
#### Using Python 3.12:

```bash
python3 -m venv .venv
source .venv/bin/activate       # On macOS/Linux
.venv\Scripts\activate          # On Windows
```

### 3. macOS Users: SSL Certificate Setup
If you encounter SSL errors when downloading NLTK data (e.g., certificate verify failed), run this command in your macOS Terminal once:
```bash
/Applications/Python\ 3.12/Install\ Certificates.command
```