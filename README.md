# 5800 Final Project

## Project Overview

This repository contains code and data for the 5800 Final Project

---

## Project Structure
```
fake-review-detection/
├── data/
│   ├── demo/
│   │   └── datamit_hotel.csv           # Demo dataset for real-world application
│   ├── original/
│   │   ├── dosc_hotel_reviews.csv      # Raw hotel reviews from data source
│   │   └── kaggle_fake_reviews.csv     # Raw fake reviews from Kaggle
│   └── processed/                      # Cleaned and preprocessed datasets
│       ├── hotel_clean.csv       # Processed cleaned-text hotel reviews dataset
│       ├── hotel_rawn.csv       # Processed raw-text hotel reviews dataset
│       ├── product_clean.csv     # Processed cleaned-text product reviews dataset
│       └── product_raw.csv     # Processed raw-text product reviews dataset
├── embeddings/
│   ├── hotel_bert_test_embeddings.pkl  # BERT embeddings for hotel test data
│   ├── hotel_bert_train_embeddings.pkl # BERT embeddings for hotel training data
│   └── hotel_embeddings_meta.pkl       # Metadata for hotel embeddings (reauire download from Google drive)
├── models/                             # Trained models and model artifacts (reauire download from Google drive)
├── notebooks/                          # Jupyter notebooks for analysis and experimentationm 
│   ├── 01_data_loading.ipynb           # Data loading and initial processing
│   ├── 02_data_analysis.ipynb          # Exploratory data analysis
│   ├── 03_product_models_with_tfidf.ipynb # Product review models with TF-IDF
│   ├── 04_transfer_learning_with_bert.ipynb # Transfer learning using BERT
│   ├── 05_hybrid_classification_and_embeddings.ipynb # Hybrid classification approaches
│   ├── 06_graph_clustering_with_embeddings.ipynb # Graph-based clustering methods
│   ├── 07_optimization_and_complexity.ipynb # Model optimization and complexity analysis
│   └── 08_final_integration_and_evaluation.ipynb # Final model integration and evaluation
├── results/                            # Model results and performance metrics
│   ├── bert_confusion_matrix.png       # BERT model confusion matrix
│   ├── bert_only_clustering.png        # BERT clustering visualization
│   ├── complexity_and_performance_comparison.png # Performance comparison chart
│   ├── ensemble_confusion_matrix.png   # Ensemble model confusion matrix
│   ├── ensemble_performance_comparison.png # Ensemble performance metrics
│   ├── graph_clustering/               # Graph clustering results (reauire download from Google drive)
│   ├── hybrid_classification/          # Hybrid model results (reauire download from Google drive)
│   └── transfer_learning/              # Transfer learning results (reauire download from Google drive)
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