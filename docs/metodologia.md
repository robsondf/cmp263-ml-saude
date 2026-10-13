# Protocolo metodológico geral — pendente da escolha da base

Definir pergunta, unidade, população, alvo, momento de predição e estimando antes dos modelos. Distinguir classificação transversal de prognóstico. Não usar variáveis definidoras do alvo como preditores.

Baseline: DummyClassifier para classificação; no mínimo cinco algoritmos candidatos: regressão logística, k-NN, árvore, floresta aleatória e SVM. Confirmar correspondência com o conteúdo programático. `src/cmp263/pipelines.py` é um ponto de partida para classificação tabular, não pipeline científico final. Se escolher regressão, implementar baseline e regressores adequados antes de treinar.

Não existe esquema universal de avaliação: dados independentes podem usar holdout estratificado + validação cruzada repetida no treino; dados por pessoa/escola/domicílio exigem grupos; perguntas sobre anos futuros exigem separação temporal. Definir as mesmas divisões para todos os modelos. Preservar teste final, evitando EDA orientada ao alvo no teste. Para amostras pequenas, discutir validação aninhada em vez de um holdout instável.

Imputação, escala, encoding, seleção, PCA, remoção de outliers aprendida e resampling devem ser ajustados só no treino de cada fold. Não aplicar todos os métodos por obrigação: EDA deve justificar a necessidade. Regras fixas de codificação oficial e elegibilidade podem preceder a divisão; critérios aprendidos não podem usar teste.

Uma métrica principal definida antes da otimização. Em classificação desbalanceada, considerar AP e baseline de prevalência; em regressão, MAE/RMSE conforme objetivo. Relatar incerteza, custo computacional, erros por grupo, calibração se probabilidades forem interpretadas e estabilidade. Não concluir superioridade por diferença minúscula nem inferir causalidade a partir de explicações.

Registrar versões, seeds, divisões, dados/artefatos com hashes e comandos. Documentar estudo anterior, diferença da pergunta, limitações de seleção, ausências e validade externa. `configs/experiment.json` só será aprovado após decisão conjunta.
