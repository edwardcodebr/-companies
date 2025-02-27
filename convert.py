
import pdfplumber
import csv
import os

pdf_path = os.path.expanduser("~/Downloads/dados_temperatura.pdf")
csv_path = os.path.expanduser("~/Downloads/dados_temperatura.csv")

with pdfplumber.open(pdf_path) as pdf:
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file: 
        writer = csv.writer(csv_file)

        for page in pdf.pages:
            table = page.extract_table()
            if table:
                writer.writerows(table)
print(f"Conversão concluída, salvo como {csv_path}")
