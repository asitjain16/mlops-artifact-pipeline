#!/usr/bin/env python3
"""
Inference script for digit classification using trained model.
"""

import os
import sys
from sklearn.metrics import accuracy_score, classification_report

# Add src directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_digits_data, load_model


def main():
    """Main inference function."""
    print("Loading trained model...")
    model_path = "model_train.pkl"
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    model = load_model(model_path)
    print("Model loaded successfully!")
    
    print("Loading digits dataset for inference...")
    # Load the same dataset used for training
    X_train, X_test, y_train, y_test = load_digits_data()
    
    print(f"Test data shape: {X_test.shape}")
    
    print("Making predictions...")
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Inference accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Show some sample predictions
    print("\nSample predictions:")
    for i in range(min(10, len(X_test))):
        true_label = y_test[i]
        pred_label = y_pred[i]
        print(f"Sample {i+1}: True={true_label}, Predicted={pred_label}")
    
    print("Inference completed successfully!")
    
    return y_pred, accuracy


if __name__ == "__main__":
    main() 