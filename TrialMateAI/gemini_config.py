"""
gemini_config.py
Configuration file for TrialMate AI
"""

import os

# Read Gemini API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "PASTE_YOUR_API_KEY_HERE")
