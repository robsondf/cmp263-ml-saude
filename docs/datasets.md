# Comparação de temas e datasets

Consulta a fontes primárias em 12/10/2026 (Brasil; 13/10 UTC). Recomendação metodológica inicial, não seleção definitiva. Não foi feita revisão sistemática para medir popularidade. Nenhuma destas bases deve ser apresentada como inédita. “Menos batido” deve significar pergunta/recorte menos repetido, a confirmar em trabalhos relacionados. As bases não foram baixadas nem tiveram qualidade empírica validada nesta etapa.

## Sugestões de Daniel

| Opção | Viabilidade | Pergunta e cuidados | Avaliação inicial |
|---|---|---|---|
| Online Shoppers Purchasing Intention (UCI) | 12.330 sessões, 17 atributos; sem ausências declaradas | Conversão; definir momento da previsão e auditar `PageValues`, variável ligada a transações, antes de usá-la | Execução simples; base estabelecida, exigiria recorte próprio |
| Default of Credit Card Clients (UCI) | 30.000 clientes, 23 atributos; sem ausências declaradas | Inadimplência; separar diagnóstico retrospectivo de uso prospectivo e discutir contexto de Taiwan | Execução simples; não é saúde, base estabelecida |
| SAEB (Inep) | Microdados e documentação oficiais; tamanho depende da edição/etapa | Predizer proficiência a partir de condições socioeconômicas/escolares; dividir por escola quando identificável; respeitar amostragem e anonimização | Melhor opção fora de saúde para um recorte brasileiro; trabalho de preparação maior |
| FAO / perdas alimentares | “FAO” é uma organização, não uma base definida | A FLW Database compila estudos/relatórios heterogêneos; primeiro verificar alvo, unidade, comparabilidade e número de observações brasileiras | Não escolher antes de piloto de cobertura; pode virar estudo agregado com poucos casos |

Fontes: [UCI Online Shoppers](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset), [UCI crédito](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients), [Inep SAEB](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb), [FAO FLW](https://www.fao.org/platform-food-loss-waste/flw-data), [guia FAO](https://www.fao.org/platform-food-loss-waste/flw-data/user-guide/en).

## Opções em saúde

| Prioridade proposta | Base / acesso oficial | Pergunta candidata | Trabalho e limite principal |
|---|---|---|---|
| 1 | SIVEP-Gripe / Ministério da Saúde; dados anuais, ficha e dicionário | Quanto o desempenho e a calibração de modelos para óbito registrado em SRAG variam entre anos, usando somente informação elegível no instante definido? | Moderado/alto: limpeza, alvo incompleto, atualização retrospectiva e auditoria temporal dos campos |
| 2 | PNS 2019 / IBGE; microdados e documentação públicos | É possível classificar saúde autoavaliada ruim/muito ruim a partir de condições socioeconômicas e hábitos? O desempenho varia por grupos? | Moderado: arquivo de largura fixa, saltos do questionário, seleção do morador e amostragem complexa; tarefa transversal, não prognóstico |
| 3 | Myocardial Infarction Complications / UCI e University of Leicester; 1.700 registros, 111 atributos declarados | Qual é a relação entre disponibilidade de atributos na admissão, desempenho e estabilidade da interpretação para um único desfecho? | Moderado: faltantes e diferentes momentos dos atributos; dados antigos e sem garantia de validade para o Brasil |
| 4 | NHANES agosto/2021–agosto/2023 / CDC | Quais atributos não laboratoriais ajudam a classificar diabetes autorreferido, e como o desempenho varia por faixa etária? | Moderado/alto: junção por SEQN, amostragem, códigos especiais; excluir medicação/questões condicionadas ao diagnóstico para evitar atalhos |
| 5 | Tuberculose / SINAN e DATASUS | Características iniciais permitem classificar interrupção registrada do tratamento entre episódios com encerramento conhecido? | Alto: acesso/anos e download específico ainda precisam ser confirmados; distinguir interrupção, cura, transferência, óbitos e encerramentos desconhecidos |

### SIVEP-Gripe: recomendação principal, condicionada ao piloto

O portal oferece recursos por ano e documentação. A descrição informa congelamento de 2019–2024, mas os próprios recursos usam rótulos “banco vivo” em partes da página. Portanto, guardar snapshot, URL exata, data e SHA-256 mesmo para anos antigos. Preferir 2022–2024 ao ano corrente incompleto. O recorte exato (Brasil, RS ou população específica) depende do número de eventos e da revisão de literatura. Não escolher apenas para agradar a professora: a adequação científica vem da pergunta, da qualidade e do protocolo.

Proposta detalhada em `proposta_sivep.md`. Não assumir que sintomas/comorbidades foram todos conhecidos na admissão: confirmar ficha, dicionário e preenchimento retrospectivo. Se o instante não puder ser sustentado, reformular como classificação retrospectiva e declarar essa limitação.

Fonte: https://dadosabertos.saude.gov.br/dataset/srag-2019-a-2026

### PNS: alternativa brasileira com foco em saúde pública

Dados: https://ftp.ibge.gov.br/PNS/2019/Microdados/Dados/PNS_2019_20220525.zip (28 MB indicados no portal; tamanho descompactado não verificado).
Documentação: https://ftp.ibge.gov.br/PNS/2019/Microdados/Documentacao/
Usar o dicionário oficial para identificar a variável de autoavaliação, população elegível e códigos. Não inventamos o nome da variável. Decidir previamente se o estimando é desempenho na amostra ou na população; para inferência populacional, considerar pesos, estratos e conglomerados. Unidades dependentes devem permanecer juntas nas divisões.

### Infarto: alternativa mais compacta

https://archive.ics.uci.edu/dataset/579/myocardial+infarction+complications
https://figshare.le.ac.uk/articles/dataset/Myocardial_infarction_complications_Database/12045261
A documentação distingue atributos de admissão, 24h, 48h e 72h e relata faltantes. Escolher um desfecho, remover outros desfechos dos preditores, confirmar eventos anteriores ao horizonte e número de positivos. Não comparar cenários 0h/72h como se fossem a mesma população: sobrevivência até 72h pode alterar a coorte. Preferir estudo restrito à admissão. Os dados originais são de 1992–1995, o que limita atualidade clínica.

### NHANES: dados oficiais bem documentados

https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023
https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DIQ_L.htm
O alvo proposto é condição autorreferida existente, não diagnóstico clínico nem previsão futura. O CDC especifica pesos diferentes conforme módulos combinados. O módulo de diabetes também tem perguntas condicionadas ao diagnóstico, que podem revelar o próprio alvo.

### SINAN: interesse alto, custo de preparação maior

https://portalsinan.saude.gov.br/tuberculose (ficha, dicionário e acompanhamento).
https://datasus.saude.gov.br/transferencia-de-arquivos/ (portal de acesso; URL do arquivo ainda não resolvida).
Encerramentos desconhecidos não devem virar automaticamente classe negativa. Transferências podem envolver episódios múltiplos; ausência de identificador confiável limita controle de dependência. A pergunta é preditiva/associativa e não demonstra causas de interrupção.

## Opções descartadas como primeira escolha

- Recorrência de câncer de tireoide (UCI, 383 casos): vários estudos recentes já comparam modelos e interpretabilidade nessa base. Uma simples comparação com SHAP seria pouco diferenciada, e a amostra pequena exige cuidado. Fonte: https://archive.ics.uci.edu/dataset/915/differentiated+thyroid+cancer+recurrence ; exemplo de estudo: https://arxiv.org/abs/2410.10907
- Bases clássicas Iris, Titanic, Breast Cancer Wisconsin, Pima Indians e Heart Disease não serão escolhas automáticas. Essa é uma preferência do projeto, não uma proibição do enunciado.

## Critérios para decisão conjunta

1. Alvo preditivo bem definido e quantidade suficiente de eventos no treino e teste.
2. Acesso efetivo, fonte primária, dicionário, licença e possibilidade de reprodução.
3. Instante de predição coerente, sem atributos que revelem o desfecho.
4. Recorte e pergunta confrontados com literatura, não só comparação de acurácia.
5. Custo compatível com seis semanas e escopo de disciplina.
6. Cinco modelos do conteúdo da disciplina, uma baseline e um método explicativo.

Decisão permanece aberta para Robson e Daniel. Se o acesso SIVEP não for resolvido em 2 dias úteis, discutir PNS ou infarto em vez de consumir o prazo com infraestrutura.
