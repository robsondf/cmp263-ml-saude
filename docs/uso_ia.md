# Suplemento — assistência por IA

Ferramenta: ChatGPT / Codex, OpenAI. Data de assistência: 12/10/2026 (America/Sao_Paulo), execução técnica 13/10 UTC. Identificador exato do modelo/versão não exposto nesta sessão; não inventar.

## Registro 001

- Prompt do usuário preservado em `prompts/001_inicio.txt`.
- Tarefas: conferir enunciado/template, comparar candidatos, recomendar fontes primárias, preparar estrutura LaTeX/notebooks/documentação e validar artefatos.
- Potenciais: organização inicial e rastreabilidade, prevenção explícita de vazamento e checklist de requisitos.
- Limitações: não houve aquisição de bases ou validação empírica da qualidade; não houve revisão sistemática de novidade; preenchimento temporal dos registros requer verificação; integração não criou remoto; nenhum resultado científico foi produzido.
- Validação técnica: descrita em `validacao.md` após execução. Validação científica e revisão dos dois autores: pendentes.

Os autores devem conferir as orientações específicas de IA e citação no Moodle, citar a ferramenta no artigo e manter os prompts futuros com data, finalidade, uso efetivo, limitações e verificação humana. O enunciado exige esse suplemento; não omitir assistência.

## Registro 002 — publicação da estrutura

- Prompts subsequentes de Robson: “pode criar a estrutura no Git, e me dá um texto para eu enviar para ele com as sugestões, mas coloque os links em abertos”; “use a conexão do git já existente aqui”; “já temos o plugin do git configurado, use essa conexão”; “criei o repositório”.
- Tarefas: preparar mensagem com URLs completas, inicializar Git local, verificar conta e acesso pela conexão existente e publicar a estrutura em branch com PR.
- Limitação operacional: a conexão não expõe criação de repositório; Robson criou o remoto. Uma tentativa de autenticação pelo navegador não foi concluída e não foi repetida após a orientação de usar somente a conexão existente.
- O repositório foi observado como público. Não foram enviados convites ou mensagens ao colega. Tema, dados e protocolo científico seguem pendentes de decisão dos autores.

## Registro 003 — prioridade de interpretabilidade (13/10/2026)

- Prompt: “só para anotação, interpretabilidade é um ponto importante do artigo”.
- Uso: registrar a diretriz no histórico de decisões e nas instruções do projeto, por branch e PR.
- Limite: nenhum método explicativo foi escolhido e nenhum experimento foi executado nesta atualização.

## Registro 004 — SHAP e LIME (13/10/2026)

- Prompt: “outra anotação, a professora comentou que o SHAP é o estado da arte para explicar modelos, mas também falou de um mais recente chamado LIME”.
- Uso: registrar o comentário de aula e conferir a cronologia nas fontes primárias dos dois métodos.
- Verificação: os trabalhos originais são de 2016 (LIME, https://arxiv.org/abs/1602.04938) e 2017 (SHAP, https://arxiv.org/abs/1705.07874).
- Limite: não houve revisão sistemática do estado da arte, escolha final de método ou implementação. A avaliação relatada da professora foi preservada como relato, sem assumir superioridade universal ou cronologia invertida.
