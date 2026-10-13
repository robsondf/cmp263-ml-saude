# Validação inicial — 13/10/2026 UTC

Esta validação é técnica. Nenhum dataset real foi adquirido, nenhum modelo científico foi treinado e nenhuma conclusão empírica foi produzida.

## Evidências

- `python scripts/validate_structure.py`: passou; arquivos obrigatórios, configurações JSON, estrutura e sintaxe das células dos quatro notebooks e dos módulos Python.
- `notebooks/00_planejamento.ipynb`: duas células de código executadas localmente, sem exceção. O notebook distribuído mantém saídas limpas.
- Notebooks 01, 02 e 03: localização/configuração funcionam; a etapa dependente de dados levanta intencionalmente RuntimeError enquanto o protocolo não está aprovado.
- Pipelines: baseline + regressão logística + k-NN + árvore + floresta + SVM passaram por fit/predict em fixture sintética de 12 observações, somente para verificação técnica. Ausência numérica e categoria inédita no teste foram toleradas. A mediana permaneceu a do treino (6), sem influência de um valor extremo no teste (10000).
- Proveniência: função SHA-256 conferida contra hashlib sobre arquivo local.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`: passou com referências resolvidas; PDF de duas páginas, sem erro, citação indefinida ou caixa excedendo margem. As duas páginas foram renderizadas e inspecionadas visualmente: título, autores, coluna única, margens e referências legíveis.
- `sbc-template.sty` e `sbc.bst`: copiados byte a byte do anexo; hashes registrados em `paper/TEMPLATE_ORIGIN.md`.
- Exportação Overleaf: ZIP produzido por `scripts/export_overleaf.py`; inclui main.tex, seções, estilo e bibliografia.

## Ambiente

Python 3.12.14; NumPy 2.3.5; pandas 2.2.3; scikit-learn 1.8.0; latexmk 4.83; pdfTeX/TeX Live 2023 (Debian).

## Pendências

Acesso/download efetivo, licença, qualidade e timing dos dados, validação de novidade, protocolo final, experimentos, revisão dos autores e diretrizes adicionais Moodle. O repositório remoto foi criado por Robson e sua publicação usa a conexão GitHub existente. Não confundir os smoke checks sintéticos com resultados do trabalho.
