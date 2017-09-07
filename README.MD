# Exemplos de Queries

Preciso cheger nessa

```sql
    SELECT
      EMPRESA,
      SUM(PESO) AS PESO,
      SUM(QTD_FARDOS) AS QTD_FARDOS,
      SUM(PESO_FARDOS) AS PESO_FARDOS,
      ROUND((SUM(PESO_FARDOS) / SUM(PESO)) * 100, 2) AS RENDIMENTO
    FROM (
      SELECT
        EMPRESA,
        ID,
        PESO,
        QTD_FARDOS,
        PESO_FARDOS
      FROM (
        SELECT
          B.EMPRESA_ID         AS EMPRESA,
          A.COD_FARDAO         AS ID,
          A.FAR_PESO_BAL       AS PESO,
          COUNT(DISTINCT B.ID) AS QTD_FARDOS,
          SUM(B.PESO)          AS PESO_FARDOS
        FROM
          GA_ALG_FARDAO A,
          V_PLUMA B
        WHERE
          B.FARDAO_ID = A.COD_FARDAO AND
          B.SAFRA = 2016 AND
          B.EMPRESA_ID = 2
        --A.COD_FARDAO = '051632522'
        GROUP BY
          B.EMPRESA_ID,
          A.COD_FARDAO,
          A.FAR_PESO_BAL
      )
    )
    GROUP BY EMPRESA
  
  
#Fix
  
  
SELECT
    EMPRESA,
    SUM(PESO) AS PESO,
    SUM(QTD_FARDOS) AS QTD_FARDOS,
    SUM(PESO_FARDOS) AS PESO_FARDOS,
    ROUND((SUM(PESO_FARDOS) / SUM(PESO)) * 100, 2) AS RENDIMENTO
  FROM (

      SELECT
        B.empresa         AS EMPRESA,
        A.id         AS ID,
        A.peso       AS PESO,
        COUNT(DISTINCT B.ID) AS QTD_FARDOS,
        SUM(B.PESO)          AS PESO_FARDOS
      FROM
        gatec_fardao A,
        gatec_pluma B
      WHERE
        B.FARDAO_ID = A.id AND
        B.SAFRA = 2016 AND
        B.empresa = 2
      GROUP BY
        B.empresa,
        A.id,
        A.peso

  )
  GROUP BY EMPRESA
```

## Setup

1. `python -m venv .venv`
2. `source .venv/bin/activate` on mac or linux `.venv\Scripts\activate.bat` on windows
3. `pip install -r requirements.txt`
4. `python manage.py runserver`


## Solutions:

### Option 1

Using Cursor with execute:
1. `python manage.py shell_plus`
2. `Pluma.objects.rendimento()`

It's magic!
