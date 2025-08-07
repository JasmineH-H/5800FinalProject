# 5800 Final Project

## Project Overview

This repository contains code and data for the 5800 Final Project

---

## Key File Structure
```
fake-review-detection/
├── data/
│   ├── demo/
│   │   └── datamit_hotel.csv           
│   ├── original/
│   │   ├── dosc_hotel_reviews.csv      
│   │   └── kaggle_fake_reviews.csv     
│   └── processed/                      
│       ├── hotel_clean.csv       
│       ├── hotel_rawn.csv       
│       ├── product_clean.csv     
│       └── product_raw.csv     
├── models/                             # reauire download from Google drive
├── notebooks/                          
│   ├── 01_data_loading.ipynb           
│   ├── 02_data_analysis.ipynb          
│   ├── 03_product_models_with_bert.ipynb 
│   ├── 04_transfer_learning_with_bert.ipynb 
│   ├── 05_hybrid_classification_and_embeddings.ipynb 
│   ├── 06_graph_clustering_with_hybird_approach.ipynb 
│   ├── 07_optimization_and_complexity.ipynb 
│   └── 08_final_integration_and_evaluation.ipynb 
├── results/                            # Model results and performance metrics
├── .gitignore                          # Git ignore rules
└── README.md                           # Project documentation
```

## Directory Descriptions

### `/data`
Contains all datasets used in the project:
- **`original/`**: Raw, unprocessed data files as downloaded from sources
- **`processed/`**: Cleaned and preprocessed data ready for model training
- **`demo/`**:  Sample datasets for testing and demonstration

### `/embeddings`
Stores pre-computed embeddings for efficient model training:
- BERT embeddings for hotel reviews (training and test sets)
- Metadata and configuration files for embeddings

### `/models`
Houses trained machine learning models and related artifacts

### `/notebooks`
Jupyter notebooks organized by project phases:
1. Data Loading & Preprocessing (01-02)
2. Model Development (03-05)
3. Advanced Techniques (06-07)
4. Final Integration (08)

### `/results`
Organized storage for all experimental results:
- Confusion matrices and performance visualizations
- Clustering analysis results
- Model comparison charts
- Phase-wise result summaries

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JasmineH-H/5800FinalProject.git
```

### 2. Create and activate a Python virtual environment (recommended)
#### Using Python 3.11:

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