"""Exporta apenas paper/; preserva caminho principal main.tex no ZIP."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
out = root / 'dist' / 'cmp263-overleaf.zip'
out.parent.mkdir(exist_ok=True)
allowed = {'.tex', '.bib', '.sty', '.bst', '.png', '.jpg', '.jpeg', '.pdf', '.md'}
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in sorted((root / 'paper').rglob('*')):
        if path.is_file() and path.suffix in allowed and path.name != 'main.pdf':
            archive.write(path, path.relative_to(root / 'paper'))
print(out)
