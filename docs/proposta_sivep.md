# Proposta provisória — SIVEP-Gripe

**Não aprovada / não executada.** Primeiro candidato para discussão com Daniel.

Pergunta: “Como o desempenho discriminativo, a calibração e os atributos relevantes de modelos para óbito registrado em casos hospitalizados de SRAG variam entre anos, quando restringimos os preditores ao instante definido de avaliação?”

Título candidato: *Temporal Generalization and Interpretability of Machine Learning Models for Recorded Mortality in Severe Acute Respiratory Syndrome*.

## População, alvo e limitações

- Candidato: hospitalizações registradas em 2022–2024; abrangência nacional ou recorte a definir após piloto. Não afirmar representatividade de todos os pacientes com infecção respiratória.
- Alvo binário: definição baseada nos códigos oficiais de evolução, com óbito por SRAG versus recuperação como primeiro cenário candidato. Decidir explicitamente o tratamento de óbito por outras causas. Não agrupar sem justificativa.
- Ausência de evolução, encerramento desconhecido e registros não elegíveis: contabilizar separadamente e analisar diferenças de perfil; não imputar alvo nem converter em recuperação. Discutir viés da coorte com desfecho conhecido.
- Instante: candidato na notificação/admissão, somente se documentável. Muitos campos podem ser atualizados retrospectivamente. Não chamar de previsão precoce se isso não puder ser confirmado.
- Idade, sexo, sintomas, comorbidades: candidatos, sujeitos à auditoria campo a campo. UTI, suporte ventilatório, evolução, datas de óbito/encerramento e tratamentos posteriores são exemplos de campos a bloquear ou auditar, não lista completa.
- Não avaliar eficácia de tratamento, vacinação ou relações causais a partir de importância de atributos.

## Protocolo candidato

1. Obter ficha, dicionário, arquivos anuais e termos de uso. Salvar hash/data/URL e levantar esquema.
2. Definir elegibilidade e auditar duplicatas, atualização, dependência entre episódios e completude do alvo.
3. Reservar 2024 como teste; explorar e ajustar com 2022–2023. Decisões são registradas antes de acessar resultados do teste.
4. Spot-checking com no mínimo 5 algoritmos da disciplina e baseline; usar divisões comuns. Avaliação primária temporal: treino 2022/validação 2023; repetições aleatórias dentro de treino podem ser análises secundárias e não substituem avaliação entre anos. Se houver datas suficientes, usar múltiplas janelas com avanço temporal, nunca misturar futuro no passado.
5. Imputação, codificação, escala, seleção e eventual balanceamento ajustados somente dentro de cada treino. Comparar inicialmente pesos de classe; SMOTE não é obrigatório e exige cuidado com atributos categóricos.
6. Métrica principal candidata: average precision (AP); secundárias ROC-AUC, sensibilidade, especificidade, F1, Brier e curva de calibração. AP é uma sumarização da curva precisão-revocação e não é sinônimo de qualquer integração trapezoidal de PR-AUC. Comparações entre anos devem considerar prevalência e case-mix.
7. Ajustar hiperparâmetros, calibração e limiar apenas em treino/validação. Sensibilidade mínima, se usada, precisa ser justificada antes da seleção. Aplicar o modelo final congelado uma vez ao teste.
8. Intervalos por bootstrap com unidade compatível com dependência dos registros; não tratar folds sobrepostos como observações independentes em teste t. Pré-especificar análises do teste e relatar sem voltar a ajustar o modelo.
9. Interpretação por importância por permutação em validação e comparação com modelo simples. Variáveis correlacionadas podem repartir importância; associação preditiva não implica causalidade. SHAP opcional conforme necessidade.
10. Sensibilidades candidatas: apenas atributos com timing documentado; indicadores de ausência versus imputação simples; peso de classe versus padrão; subgrupos com eventos suficientes.

## Critério de viabilidade do piloto

Confirmar acesso reprodutível, termos de uso, variável alvo, completude por ano, quantidade de óbitos/recuperações e disponibilidade dos preditores. O piloto ainda não foi feito. Sem timing confiável, reformular o objetivo ou escolher outra base. Sem eventos suficientes no recorte RS, ampliar a coorte antes de alterar métricas ou critérios.

Fonte primária: https://dadosabertos.saude.gov.br/dataset/srag-2019-a-2026
