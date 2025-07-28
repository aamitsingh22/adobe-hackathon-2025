import fitz  # PyMuPDF

def analyze_documents(input_dir, filenames, persona, job):
    results = {
        "extracted_sections": [],
        "sub_section_analysis": []
    }

    keywords = [kw.lower() for kw in persona["focus"]]

    for fname in filenames:
        doc = fitz.open(f"{input_dir}/{fname}")
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            lines = text.split("\n")
            for line in lines:
                lowered = line.lower()
                for kw in keywords:
                    if kw in lowered:
                        results["extracted_sections"].append({
                            "document": fname,
                            "page": page_num,
                            "section_title": line.strip(),
                            "importance_rank": 1
                        })
                        results["sub_section_analysis"].append({
                            "document": fname,
                            "page": page_num,
                            "refined_text": line.strip()
                        })
                        break
    return results
