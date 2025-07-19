#!/usr/bin/env python3
"""
Training script for digit classification using Logistic Regression.
"""

import os
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Add src directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_config, load_digits_data, save_model


def train_model(X_train, y_train, config):
    """
    Train a Logistic Regression model with given configuration.
    
    Args:
        X_train: Training features
        y_train: Training labels
        config (dict): Model configuration
        
    Returns:
        LogisticRegression: Trained model
    """
    model = LogisticRegression(
        C=config['C'],
        solver=config['solver'],
        max_iter=config['max_iter'],
        random_state=config['random_state']
    )
    
    model.fit(X_train, y_train)
    return model


def main():
    """Main training function."""
    print("Loading configuration...")
    config = load_config()
    
    print("Loading digits dataset...")
    X_train, X_test, y_train, y_test = load_digits_data(
        test_size=config['test_size'],
        random_state=config['random_state']
    )
    
    print(f"Training data shape: {X_train.shape}")
    print(f"Test data shape: {X_test.shape}")
    
    print("Training Logistic Regression model...")
    model = train_model(X_train, y_train, config)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model
    model_path = "model_train.pkl"
    print(f"Saving model to {model_path}...")
    save_model(model, model_path)
    
    print("Training completed successfully!")
    
    return model, accuracy


if __name__ == "__main__":
    main() 