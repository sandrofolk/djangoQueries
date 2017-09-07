from django.db import models, connection


class CustonManager(models.Manager):
    def rendimento(self):
        with connection.cursor() as cursor:
            cursor.execute("""
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
                        B.SAFRA = %s AND
                        B.empresa = %s
                      GROUP BY
                        B.empresa,
                        A.id,
                        A.peso
    
                  )
                  GROUP BY EMPRESA""", [2016, 2])
            result_list = []
            for row in cursor.fetchall():
                p = {
                    'EMPRESA': row[0],
                    'PESO': row[1],
                    'QTD_FARDOS': row[2],
                    'PESO_FARDOS': row[3],
                    'RENDIMENTO': row[4],
                }
                result_list.append(p)
        return result_list


class Fardao(models.Model):

    id = models.CharField(max_length=10, primary_key=True)
    empresa = models.IntegerField()
    safra = models.IntegerField()
    peso = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.IntegerField()


    class Meta:
        verbose_name = 'fardão'
        verbose_name_plural = 'fardões'

    def __str__(self):
        return self.id

class Pluma(models.Model):

    id = models.IntegerField(primary_key=True)
    empresa = models.IntegerField()
    safra = models.IntegerField()
    fardao = models.ForeignKey('Fardao')
    peso = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.DecimalField(max_digits=2, decimal_places=1)

    objects = CustonManager()

    def __str__(self):
        return self.id