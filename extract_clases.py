from pypdf import PdfReader
import pathlib, re

src = pathlib.Path("Clases")
dst = pathlib.Path("Clases_txt")
dst.mkdir(exist_ok=True)

for pdf in sorted(src.glob("*.pdf")):
    try:
        reader = PdfReader(pdf)
        paginas = []
        for i, page in enumerate(reader.pages, 1):
            try:
                txt = page.extract_text() or ""
            except Exception:
                txt = ""
            # limpia warnings de pypdf incrustados en el texto
            txt = re.sub(r"^could not convert string to float:.*$", "", txt, flags=re.M)
            paginas.append(f"## Pagina {i}\n\n{txt.strip()}")
        out = f"# {pdf.stem}\n\n" + "\n\n---\n\n".join(paginas) + "\n"
        (dst / f"{pdf.stem}.md").write_text(out, encoding="utf-8")
        print(f"{pdf.name}: {len(reader.pages)} paginas -> {dst / (pdf.stem + '.md')}")
    except Exception as e:
        print(f"{pdf.name}: ERROR {e}")
