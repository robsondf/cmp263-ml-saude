# CMP263 — Aprendizagem de Máquina — Turma A (2026/2)

Autores: **Robson Dias Ferreira** e **Daniel Godoy Bitelo**. Professora: Mariana Recamonde Mendoza. PPGC/UFRGS.

**Estado: estrutura inicial validada; tema, dataset e protocolo final ainda não aprovados pelos autores.**
Repositório: [robsondf/cmp263-ml-saude](https://github.com/robsondf/cmp263-ml-saude), criado por Robson como público. A estrutura inicial é publicada na branch `feat/estrutura-inicial` com PR para revisão; sem merge automático. O remoto é independente de qualquer outro artigo.
Projeto exclusivo de CMP263. Apenas a organização de pastas segue o projeto anterior; não há conteúdo, dados, resultados ou referências financeiras reutilizados.

## Comece aqui

1. Leia [os requisitos](docs/requisitos.md), [a comparação de datasets](docs/datasets.md) e [a proposta SIVEP](docs/proposta_sivep.md).
2. Os dois autores escolhem a pergunta e a base; registrem a decisão em `docs/decisoes.md`.
3. Façam o piloto de acesso/dicionário, definam população, alvo, instante de predição e separação dos dados.
4. Só então configurem `configs/experiment.json` e implementem os experimentos.

## Organização

| Pasta | Conteúdo |
|---|---|
| `paper/` | Artigo LaTeX SBC, referências, seções e figuras para Overleaf |
| `notebooks/` | Planejamento, aquisição/EDA, modelos e interpretação em Colab |
| `src/cmp263/` | Funções reutilizáveis, pipelines e registro de proveniência |
| `data/` | Dicionário, manifesto de fontes e instruções; bases locais ignoradas pelo Git |
| `results/figures/`, `results/tables/` | Saídas reais, com origem e comando de geração |
| `docs/` | Requisitos, propostas, decisões, cronograma, colaboração e uso de IA |
| `configs/` | Configurações explícitas e sementes |
| `scripts/` | Verificação da estrutura e exportação para Overleaf |

## Ambiente e execução

Python 3.12. Versões abaixo correspondem ao ambiente usado na validação inicial, não a uma execução científica.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate_structure.py
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

No Windows, ative `.venv\Scripts\Activate.ps1` no PowerShell. Para Overleaf, execute `python scripts/export_overleaf.py` e importe o ZIP gerado em `dist/`. Se importar o repositório inteiro, escolha `paper/main.tex` como documento principal. Para Colab, abra a aba GitHub na interface do Colab, procure `robsondf/cmp263-ml-saude` e escolha a branch `feat/estrutura-inicial` enquanto o PR estiver aberto, ou `main` após o merge. Forneça também a pasta do projeto ao notebook, conforme suas instruções. Alternativa: carregar o `.ipynb` manualmente e fornecer a pasta no Drive. Nenhuma execução no Colab foi validada ainda.

O notebook `00_planejamento.ipynb` já inspeciona a configuração e as pastas, sem baixar dados. Os demais notebooks documentam as etapas pendentes e bloqueiam execução sem uma base aprovada.

## Colaboração e entregas

Mudanças de código, notebook e artigo: branch + Pull Request + revisão do outro autor; sem merge automático. Ambos participam de todas as etapas. Ver `docs/colaboracao.md`.

Entrega de artigo e código: **22/11/2026, 23:59**; revisão: **24–30/11/2026, até 23:59**; apresentação: **01/12/2026**. Horários conforme enunciado, adotando America/Sao_Paulo; confirmar no Moodle. Artigo SBC em coluna única, até 20 páginas incluindo referências, preferencialmente em inglês. Uso de IA deve ser citado e os prompts constar em suplemento.

O PDF inicial é um protocolo marcado como rascunho, não um artigo com resultados. Nenhuma base foi adquirida, analisada ou selecionada nesta etapa.
