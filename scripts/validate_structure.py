"""Verifica estrutura e notebooks; não executa experimentos científicos."""
from pathlib import Path
import json, ast

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'AGENTS.md', 'paper/main.tex', 'paper/sbc-template.sty',
            'paper/sbc.bst', 'paper/references.bib', 'configs/experiment.json',
            'data/manifest.json', 'docs/requisitos.md', 'docs/uso_ia.md']
for name in required:
    assert (root / name).is_file(), f'Missing: {name}'
config = json.loads((root / 'configs/experiment.json').read_text())
assert config['project'] == 'CMP263_2026_2_Turma_A'
for path in sorted((root / 'notebooks').glob('*.ipynb')):
    notebook = json.loads(path.read_text())
    assert notebook['nbformat'] == 4
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            ast.parse(''.join(cell['source']))
for path in (root / 'src').rglob('*.py'):
    ast.parse(path.read_text())
print('Estrutura, JSON, notebooks e sintaxe Python verificados. Sem resultados científicos.')
