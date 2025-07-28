# Persona-Driven Document Intelligence (Round 1B - Adobe Hackathon)

## 📌 Overview
This system extracts and prioritizes the most relevant sections from a document collection based on a **persona** and their **job-to-be-done**.

## 🧠 Approach
- Uses keyword matching aligned with persona focus areas.
- For each matched section, the system stores metadata and relevant text.

## 🐳 Build and Run Instructions

### Build Docker Image
```bash
docker build --platform linux/amd64 -t pdfpersonaextractor:tag .
```

### Run Docker Container
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdfpersonaextractor:tag
```

## ✅ Output Format
- `challenge1b_output.json` containing:
  - Metadata (persona, job, timestamp)
  - Extracted relevant sections
  - Sub-section analysis

## 🧠 Sample Persona
```json
{
  "name": "Investment Analyst",
  "focus": ["Revenue", "R&D", "Market Positioning"]
}
```

## 🚫 Constraints
- Model size ≤ 1 GB
- Must run on CPU within 60 seconds
- Offline only (no internet)
