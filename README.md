# 📘 PDF Outline Extractor
Round 1A
## 🎯 Objective
To transform raw PDF documents into **structured outlines** by extracting:
- Document **Title**
- Headings with levels: **H1**, **H2**, **H3**
- Corresponding **page numbers**

This lays the foundation for intelligent PDF navigation, semantic search, and document understanding.

---

## 🧠 Approach

We use **PyMuPDF** (fitz) to:
- Parse PDF text and layout information
- Apply **font-size based heuristics** to infer heading levels
- Clean and format the headings in hierarchical structure

### 🔍 Key Heuristics:
  font size > 16 → H1  
  font size > 14 → H2  
  font size > 12 → H3  

This method is adaptive and avoids hardcoded assumptions about specific documents.

---

Round 1B

markdown
# 🔍 Persona-Driven Document Intelligence  
### Adobe India Hackathon 2025 – Round 1B Submission

## 🎯 Objective

Build a system that understands **who** the reader is (persona), **what** they want (job), and intelligently extracts only the **relevant document sections** from multiple PDFs.

---

## 🧠 Problem Breakdown

Given:
- A persona (e.g., "Investment Analyst")
- A job to do (e.g., "Analyze revenue trends")
- A set of related PDF documents

Your system must:
1. Extract sections relevant to that persona's task
2. Provide both section-level and sub-section-level insight
3. Output a structured, ranked JSON file

---

## 🧩 Approach

We use **PyMuPDF** to parse text and perform **keyword-based filtering** that aligns with persona focus areas.

### 🧠 Persona Example:
json
{
  "name": "Investment Analyst",
  "focus": ["Revenue", "R&D", "Market Positioning"]
}
