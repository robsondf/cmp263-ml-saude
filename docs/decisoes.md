# Registro de decisões

| Data (Brasil) | Registro | Estado |
|---|---|---|
| 12/10/2026 | Projeto próprio de CMP263, autores Robson e Daniel, template SBC anexado | Determinado por Robson |
| 12/10/2026 | Saúde e bases menos repetidas como preferências | Determinado por Robson |
| 12/10/2026 | Diretórios seguindo apenas a organização do projeto anterior | Determinado por Robson |
| 12/10/2026 | SIVEP-Gripe como primeira recomendação; PNS como segunda | Proposta do assistente, sem aprovação conjunta |
| 12/10/2026 | Nome `cmp263-ml-saude`, privado em `robsondf` | Proposta operacional; remoto ainda não criado |
| 12/10/2026 | Robson autorizou criação da estrutura no Git/GitHub; autenticação no navegador não concluída | Git local inicializado; publicação remota pendente |
| 12/10/2026 | Robson criou `robsondf/cmp263-ml-saude`; conexão existente confirmou repositório vazio e público | Publicação da estrutura em branch + PR, sem merge automático |
| 13/10/2026 | Interpretabilidade é um ponto importante do artigo e deve orientar as escolhas científicas e a discussão | Diretriz explícita de Robson |
| 13/10/2026 | Robson relatou que a professora destacou SHAP como estado da arte e também comentou LIME | Anotação de aula; conferir adequação dos métodos ao problema |

Pendente: pergunta, base, versão/licença, recorte, alvo, timing, métricas, estratégia de avaliação, login de Daniel, diretrizes de citação IA do Moodle e divisão de condução/revisão. Não marcar decisões como aprovadas sem evidência.

## Prioridade: interpretabilidade

A interpretabilidade deve ser considerada desde a escolha da pergunta, do dataset e dos modelos até a análise dos resultados. Planejar comparação com modelos naturalmente interpretáveis e selecionar métodos explicativos adequados ao modelo e ao problema. Examinar quais atributos influenciam as predições, a estabilidade das explicações e suas limitações. A explicação de associações preditivas não demonstra causalidade. Os métodos específicos serão definidos pelos autores após a escolha da base.

## SHAP e LIME — anotação de aula

Robson relatou que a professora destacou SHAP como “estado da arte” para explicar modelos e também apresentou LIME. Essa avaliação foi registrada como comentário de aula, não como afirmação de superioridade universal. SHAP será uma referência prioritária a estudar e LIME uma alternativa a considerar; a escolha final depende dos dados, dos modelos e do objetivo das explicações.

Cronologia conferida nas fontes primárias: LIME foi apresentado por Marco Tulio Ribeiro, Sameer Singh e Carlos Guestrin em 2016; SHAP foi apresentado por Scott Lundberg e Su-In Lee em 2017. Portanto, o LIME original antecede o SHAP original. O relato de que LIME seria “mais recente” não foi incorporado como fato; uma possível referência a versões posteriores precisaria ser esclarecida.

- LIME: aprende um modelo interpretável na vizinhança de uma predição para explicá-la localmente. Trabalho original: *“Why Should I Trust You?”: Explaining the Predictions of Any Classifier*. https://arxiv.org/abs/1602.04938
- SHAP: atribui contribuições aos atributos para uma predição, em uma estrutura de explicações aditivas. Trabalho original: *A Unified Approach to Interpreting Model Predictions*. https://arxiv.org/abs/1705.07874

Nenhum método foi implementado ou escolhido definitivamente nesta anotação. O desenho experimental deverá considerar fidelidade, estabilidade e limitações das explicações, mantendo a distinção entre associação preditiva e causalidade.
