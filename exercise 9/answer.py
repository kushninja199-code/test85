import os
import pypdf

def merge_pdfs(pdf_list, output_path):
    merger = pypdf.PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

files = [
    os.path.join("exercise 9", "AdmitCard-260310707585.pdf"),
    os.path.join("exercise 9", "pes application.pdf")
]
merge_pdfs(files, os.path.join("exercise 9", "merged_result.pdf"))
