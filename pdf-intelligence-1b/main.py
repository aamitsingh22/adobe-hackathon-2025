import os
import json
from datetime import datetime
from utils.extractor import analyze_documents

INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'

def main():
    input_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.pdf')]
    persona = {
        "name": "Investment Analyst",
        "focus": ["Revenue", "R&D", "Market Positioning"]
    }
    job = "Analyze revenue trends, R&D investments, and market positioning strategies"

    output = analyze_documents(INPUT_DIR, input_files, persona, job)

    output['metadata'] = {
        "input_documents": input_files,
        "persona": persona,
        "job_to_be_done": job,
        "processing_timestamp": datetime.utcnow().isoformat()
    }

    with open(os.path.join(OUTPUT_DIR, "challenge1b_output.json"), "w") as f:
        json.dump(output, f, indent=2)

if __name__ == '__main__':
    main()
