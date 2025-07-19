# ML Ops Artifact Pipeline - Setup Guide

## Overview

This repository implements a complete ML Ops pipeline for digit classification using Logistic Regression with GitHub Actions for continuous integration and deployment.

## Project Structure

```
mlops-artifact-pipeline/
├── src/
│   ├── train.py          # Training script
│   ├── inference.py      # Inference script
│   └── utils.py          # Utility functions
├── config/
│   └── config.json       # Model hyperparameters
├── tests/
│   └── test_train.py     # Unit tests
├── .github/
│   └── workflows/
│       ├── train.yml     # Training workflow
│       ├── test.yml      # Testing workflow
│       └── inference.yml # Multi-job inference workflow
├── requirements.txt       # Python dependencies
├── README.md            # Project documentation
└── SETUP.md             # This setup guide
```

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mlops-artifact-pipeline.git
cd mlops-artifact-pipeline
```

### 2. Create Conda Environment

```bash
conda create -n mlops-pipeline python=3.9
conda activate mlops-pipeline
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Branching Strategy

Follow this linear branching approach as specified in the assignment:

1. **main** (initial branch with README only)
2. **classification** (Phase 1: Training Pipeline)
3. **test** (Phase 2: Testing with Pytest)
4. **inference** (Phase 3: Multi-job Inference Pipeline)

### Creating Branches

```bash
# Start from main
git checkout main

# Create classification branch
git checkout -b classification
# Complete Phase 1 tasks
git add .
git commit -m "Phase 1: Training pipeline implementation"
git push origin classification

# Create test branch from classification
git checkout classification
git checkout -b test
# Complete Phase 2 tasks
git add .
git commit -m "Phase 2: Testing framework implementation"
git push origin test

# Create inference branch from test
git checkout test
git checkout -b inference
# Complete Phase 3 tasks
git add .
git commit -m "Phase 3: Multi-job inference pipeline"
git push origin inference
```

## Local Testing

### 1. Test Training Pipeline

```bash
python src/train.py
```

Expected output:
- Model training with accuracy > 95%
- Model saved as `model_train.pkl`

### 2. Test Inference Pipeline

```bash
python src/inference.py
```

Expected output:
- Model loaded successfully
- Inference accuracy > 95%
- Sample predictions displayed

### 3. Run Unit Tests

```bash
python -m pytest tests/ -v
```

Expected output:
- All 11 tests passing
- Configuration validation
- Model creation tests
- Accuracy threshold tests

## GitHub Actions Workflows

### 1. Training Workflow (train.yml)

**Trigger**: Push/PR to `classification` branch
**Jobs**: 
- Setup Python environment
- Install dependencies
- Run training script
- Upload model artifact

### 2. Testing Workflow (test.yml)

**Trigger**: Push/PR to `test` branch
**Jobs**:
- Setup Python environment
- Install dependencies
- Run pytest suite

### 3. Inference Workflow (inference.yml)

**Trigger**: Push/PR to `inference` branch
**Jobs** (with dependencies):
1. **test**: Run all unit tests
2. **train**: Train model (depends on test)
3. **inference**: Run inference (depends on train)

## Configuration

The model hyperparameters are defined in `config/config.json`:

```json
{
    "C": 1.0,              // Inverse regularization strength
    "solver": "lbfgs",      // Optimization algorithm
    "max_iter": 1000,       // Maximum iterations
    "random_state": 42,     // Random seed
    "test_size": 0.2        // Test set proportion
}
```

## Model Performance

- **Dataset**: sklearn.datasets.load_digits
- **Features**: 64 grayscale pixel values (8x8 images)
- **Classes**: 10 digits (0-9)
- **Model**: LogisticRegression
- **Expected Accuracy**: > 95%

## Artifact Management

- Models are saved as `model_train.pkl`
- GitHub Actions uploads models as artifacts
- Artifacts are passed between jobs using `needs` parameter
- Artifact retention: 30 days

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're in the correct directory and dependencies are installed
2. **Model Not Found**: Run training script first to generate `model_train.pkl`
3. **Test Failures**: Check that all required files exist and paths are correct

### Windows-Specific Notes

- Use `python -m pytest` instead of `pytest` directly
- Some packages may require Visual Studio Build Tools for compilation

## Performance Metrics

The pipeline achieves:
- **Training Accuracy**: ~96%
- **Test Accuracy**: ~96%
- **F1-Score**: ~96%
- **All Tests Passing**: 11/11

## Submission Checklist

- [x] Repository is public and named `mlops-artifact-pipeline`
- [x] All tasks completed
- [x] `model_train.pkl` is uploaded as GitHub artifact
- [x] Final inference workflow chains test → train → inference correctly
- [x] All workflows pass in GitHub Actions
- [x] No hardcoded values (all from config.json)
- [x] Comprehensive documentation included 