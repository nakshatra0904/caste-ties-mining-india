"""Regenerate source text using pypdf's layout extraction; one-based PDF pages."""
from pathlib import Path
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]/'data/raw'
for name in ['ec6_report.pdf','maharashtra_ec6.pdf']:
    reader=PdfReader(R/name)
    parts=[]
    for i,page in enumerate(reader.pages,1):
        parts.append(r'\n--- PDF PAGE '+str(i)+r' ---\n'+page.extract_text(extraction_mode='layout'))
    (R/(name+'.txt')).write_text(''.join(parts),encoding='utf-8')
    print(name, len(reader.pages), 'pages')
