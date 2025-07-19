# ML Ops Artifact Pipeline

This repository contains a complete ML Ops pipeline for digit classification using Logistic Regression, implemented with GitHub Actions for continuous integration and deployment.

**Testing Framework Active** - This branch contains the testing framework implementation.

## Project Structure

```
.
├── src/
│   ├── train.py
│   ├── inference.py
│   └── utils.py
├── config/
│   └── config.json
├── tests/
│   └── test_train.py
├── .github/
│   └── workflows/
│       ├── train.yml
│       ├── test.yml
│       └── inference.yml
├── requirements.txt
└── README.md
```

## Features

- **Training Pipeline**: Automated model training with configurable hyperparameters
- **Testing Framework**: Comprehensive unit tests using pytest
- **CI/CD Pipeline**: GitHub Actions workflows for testing, training, and inference
- **Artifact Management**: Model artifacts passed between workflow jobs

## Dataset

- **Dataset**: sklearn.datasets.load_digits (built-in)
- **Task**: Multiclass classification (digits 0–9)
- **Features**: 64 grayscale pixel values (flattened 8x8 images)
- **Model**: LogisticRegression from sklearn.linear_model

## Branching Strategy

- `main` → `classification` → `test` → `inference`

Each branch builds upon the previous one in a linear order without merging back to main. 