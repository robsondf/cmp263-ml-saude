# Colaboração

Robson e Daniel participam de dados, modelagem, análise e escrita. Papéis de condução/revisão serão acordados; não atribuímos unilateralmente tarefas ao colega.

| Mudança | Branch sugerida | Entrega revisável |
|---|---|---|
| Tema e piloto | `feat/dataset-piloto` | Pergunta, fonte, dicionário, viabilidade e decisão |
| Aquisição e EDA | `feat/dados-eda` | Notebook reproduzível e documentação de elegibilidade |
| Modelos | `feat/modelos` | Splits, pipeline, grids, métrica e resultados reais |
| Interpretação | `feat/interpretacao` | Figuras, estabilidade e limitações |
| Artigo | `docs/artigo` | LaTeX compilado, referências e revisão |

Antes do PR: executar validações adequadas, conferir diferença e registrar comandos/resultados. O outro autor revisa. Sem merge automático. Não editar simultaneamente o mesmo `.ipynb`; separar notebooks ou coordenar alterações. Escrever funções reutilizáveis em `src/` reduz conflitos.

GitHub guarda fontes e histórico; Overleaf deve usar a versão acordada de `paper/`; Colab é ambiente de execução. Escolher uma origem por alteração e sincronizar para evitar forks divergentes. Dados grandes/cache podem ficar em pastas locais ou Drive separado deste projeto, com manifesto de reprodução. Não reutilizar caminhos de dados de outro artigo.

Robson criou o repositório público `robsondf/cmp263-ml-saude`. A estrutura inicial é publicada em `feat/estrutura-inicial` com PR, e futuras alterações seguem esse fluxo. O convite ao Daniel requer identificação do login correto e instrução explícita; nenhum convite foi enviado. Por ser público, ele pode consultar os arquivos pelo link; permissão de escrita exige convite. `docs/publicacao.md` registra o estado da publicação.
