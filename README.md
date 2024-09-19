
## Análise de fatores relacionados ao diagnóstico de TEA

Este notebook visa explorar e analisar dados relacionados ao diagnóstico de Transtorno do Espectro Autista (TEA) utilizando técnicas de Data Science. Através de uma análise exploratória dos dados e da identificação de variáveis influentes, tentaremos entender melhor os fatores que contribuem para a classificação de pacientes com ou sem TEA.

O objetivo principal é descobrir padrões e insights que podem auxiliar na identificação precoce e tratamento do TEA.

## Bibliotecas Utilizadas

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import markdown
```
## Carregando Base 
```python
url = "https://raw.githubusercontent.com/CarolineSelis/ETL-de-Base-de-Dados-P-blica/main/Autism_Screening.csv"
base = pd.read_csv(url)
print(base.head().to_markdown())
```
