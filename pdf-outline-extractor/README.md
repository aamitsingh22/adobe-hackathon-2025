# PDF Outline Extractor (Round 1A - Adobe Hackathon)

## 📌 Overview
This project extracts structured outlines (Title, H1, H2, H3 headings) from a given PDF file and outputs a standardized JSON format.

## 🧠 Approach
We use PyMuPDF to:
- Parse page text blocks
- Identify heading levels based on font size heuristics
- Capture text, level, and page number

## 📦 Model/Library
- `PyMuPDF (fitz)` for PDF parsing

## 🐳 Build and Run Instructions

### Build Docker Image
```bash
docker build --platform linux/amd64 -t pdfoutlineextractor:tag .
```

### Run Docker Image
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdfoutlineextractor:tag
```

## ✅ Output Format
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## 🚫 Constraints
- No internet access
- ≤ 10 sec for 50-page PDF
- CPU only
