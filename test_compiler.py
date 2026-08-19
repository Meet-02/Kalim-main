import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

# Import the compiler pipeline directly
from compiler.pipeline import run_compiler  # or import individual functions

# Alternatively, if using the submodule functions:
from compiler.nlp_parser import nlp_parser
from compiler.gemini_corrector import gemini_corrector

sample_raw_text = "[RED] 4 [BLUE] 2 [GREEN] 6"

# 1. Parse raw notation
parsed = nlp_parser(sample_raw_text)
print("--- Parsed Output ---")
print(parsed)

# 2. Correct with Gemini
result_json = gemini_corrector(parsed)
print("\n--- Final Structured JSON ---")
print(result_json)