import os
import json
from utils.extractor import extract_outline_from_pdf

INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename.replace('.pdf', '.json'))
            outline = extract_outline_from_pdf(pdf_path)
            with open(output_path, 'w') as f:
                json.dump(outline, f, indent=2)

if __name__ == '__main__':
    main()
