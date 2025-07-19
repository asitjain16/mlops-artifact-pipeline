#!/usr/bin/env python3
"""
Unit tests for the training pipeline.
"""

import os
import sys
import pytest
import json
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Add src directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_config, load_digits_data, save_model, load_model
from src.train import train_model


class TestConfiguration:
    """Test configuration file loading and validation."""
    
    def test_config_file_exists(self):
        """Test that configuration file exists."""
        config_path = "config/config.json"
        assert os.path.exists(config_path), f"Configuration file not found: {config_path}"
    
    def test_config_file_loads_successfully(self):
        """Test that configuration file loads successfully."""
        config = load_config()
        assert isinstance(config, dict), "Configuration should be a dictionary"
    
    def test_required_hyperparameters_exist(self):
        """Test that all required hyperparameters exist in configuration."""
        config = load_config()
        required_params = ['C', 'solver', 'max_iter']
        
        for param in required_params:
            assert param in config, f"Required parameter '{param}' not found in config"
    
    def test_hyperparameter_data_types(self):
        """Test that hyperparameters have correct data types."""
        config = load_config()
        
        # Check data types
        assert isinstance(config['C'], (int, float)), "C should be numeric"
        assert isinstance(config['solver'], str), "solver should be string"
        assert isinstance(config['max_iter'], int), "max_iter should be integer"
        assert isinstance(config['random_state'], int), "random_state should be integer"
        assert isinstance(config['test_size'], float), "test_size should be float"
    
    def test_hyperparameter_values(self):
        """Test that hyperparameter values are reasonable."""
        config = load_config()
        
        assert config['C'] > 0, "C should be positive"
        assert config['max_iter'] > 0, "max_iter should be positive"
        assert 0 < config['test_size'] < 1, "test_size should be between 0 and 1"
        assert config['solver'] in ['lbfgs', 'liblinear', 'newton-cg', 'sag', 'saga'], \
            "solver should be a valid sklearn solver"


class TestModelCreation:
    """Test model creation and training."""
    
    def test_train_model_function_returns_logistic_regression(self):
        """Test that train_model function returns a LogisticRegression object."""
        config = load_config()
        X_train, X_test, y_train, y_test = load_digits_data()
        
        model = train_model(X_train, y_train, config)
        
        assert isinstance(model, LogisticRegression), \
            "train_model should return a LogisticRegression object"
    
    def test_model_is_fitted(self):
        """Test that the model has been fitted (has coefficients)."""
        config = load_config()
        X_train, X_test, y_train, y_test = load_digits_data()
        
        model = train_model(X_train, y_train, config)
        
        # Check that model has been fitted
        assert hasattr(model, 'coef_'), "Model should have coefficients after fitting"
        assert hasattr(model, 'classes_'), "Model should have classes after fitting"
        assert model.coef_ is not None, "Model coefficients should not be None"
        assert model.classes_ is not None, "Model classes should not be None"
    
    def test_model_save_and_load(self):
        """Test that model can be saved and loaded correctly."""
        config = load_config()
        X_train, X_test, y_train, y_test = load_digits_data()
        
        # Train model
        model = train_model(X_train, y_train, config)
        
        # Save model
        model_path = "test_model.pkl"
        save_model(model, model_path)
        
        # Check file exists
        assert os.path.exists(model_path), "Model file should be created"
        
        # Load model
        loaded_model = load_model(model_path)
        
        # Check that loaded model is the same type
        assert isinstance(loaded_model, LogisticRegression), \
            "Loaded model should be LogisticRegression"
        
        # Check that predictions are the same
        original_pred = model.predict(X_test[:5])
        loaded_pred = loaded_model.predict(X_test[:5])
        
        assert (original_pred == loaded_pred).all(), \
            "Loaded model should make same predictions as original"
        
        # Clean up
        os.remove(model_path)


class TestModelAccuracy:
    """Test model accuracy and performance."""
    
    def test_model_accuracy_threshold(self):
        """Test that model accuracy is above a reasonable threshold."""
        config = load_config()
        X_train, X_test, y_train, y_test = load_digits_data()
        
        # Train model
        model = train_model(X_train, y_train, config)
        
        # Make predictions
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Check that accuracy is above threshold (digits dataset is relatively easy)
        min_accuracy = 0.85
        assert accuracy >= min_accuracy, \
            f"Model accuracy {accuracy:.4f} is below threshold {min_accuracy}"
        
        print(f"Model accuracy: {accuracy:.4f}")
    
    def test_model_performance_on_training_data(self):
        """Test that model performs well on training data (sanity check)."""
        config = load_config()
        X_train, X_test, y_train, y_test = load_digits_data()
        
        # Train model
        model = train_model(X_train, y_train, config)
        
        # Make predictions on training data
        y_train_pred = model.predict(X_train)
        train_accuracy = accuracy_score(y_train, y_train_pred)
        
        # Training accuracy should be high
        min_train_accuracy = 0.90
        assert train_accuracy >= min_train_accuracy, \
            f"Training accuracy {train_accuracy:.4f} is below threshold {min_train_accuracy}"
        
        print(f"Training accuracy: {train_accuracy:.4f}")


class TestDataLoading:
    """Test data loading functionality."""
    
    def test_digits_data_loading(self):
        """Test that digits dataset loads correctly."""
        X_train, X_test, y_train, y_test = load_digits_data()
        
        # Check shapes
        assert X_train.shape[1] == 64, "Features should have 64 dimensions"
        assert X_test.shape[1] == 64, "Features should have 64 dimensions"
        assert len(X_train) == len(y_train), "X_train and y_train should have same length"
        assert len(X_test) == len(y_test), "X_test and y_test should have same length"
        
        # Check data types
        assert X_train.dtype in ['float64', 'float32'], "Features should be numeric"
        assert y_train.dtype in ['int64', 'int32'], "Labels should be integer"
        
        print(f"Training data shape: {X_train.shape}")
        print(f"Test data shape: {X_test.shape}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 