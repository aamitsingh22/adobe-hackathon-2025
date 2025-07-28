import os
import fitz  # PyMuPDF

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.basename(pdf_path).replace(".pdf", "")

    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text = " ".join([span["text"] for span in line["spans"]])
                    font_size = max([span["size"] for span in line["spans"]])

                    if font_size > 16:
                        level = "H1"
                    elif font_size > 14:
                        level = "H2"
                    elif font_size > 12:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": text.strip(),
                        "page": page_number
                    })

    return {
        "title": title,
        "outline": outline
    }
