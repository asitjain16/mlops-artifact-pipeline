#!/usr/bin/env python3
"""
Test script to verify all imports work correctly.
"""

import sys
import os

# Add src directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    print("Testing imports...")
    
    # Test basic imports
    import numpy as np
    print("✅ numpy imported successfully")
    
    import pandas as pd
    print("✅ pandas imported successfully")
    
    from sklearn.datasets import load_digits
    print("✅ sklearn.datasets imported successfully")
    
    from sklearn.linear_model import LogisticRegression
    print("✅ sklearn.linear_model imported successfully")
    
    from sklearn.metrics import accuracy_score, classification_report
    print("✅ sklearn.metrics imported successfully")
    
    from sklearn.model_selection import train_test_split
    print("✅ sklearn.model_selection imported successfully")
    
    import pytest
    print("✅ pytest imported successfully")
    
    import joblib
    print("✅ joblib imported successfully")
    
    # Test our custom imports
    from src.utils import load_config, load_digits_data, save_model, load_model
    print("✅ src.utils imported successfully")
    
    from src.train import train_model
    print("✅ src.train imported successfully")
    
    print("\n✅ All imports successful!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1) 