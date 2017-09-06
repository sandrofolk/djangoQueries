
from .models import *

def popular(safra=2016):

    Fardao.objects.all().delete()
    Pluma.objects.all().delete()

    fardoes_data = []
    plumas_data = []

    fardoes = FardaoGatec.objects.filter(safra=2016).using('oracle')

    for fardao in fardoes:

        print(fardao)

        data = dict(
            id=fardao.id,
            empresa=fardao.empresa_id,
            safra=fardao.safra,
            peso=fardao.peso,
            status=fardao.status,
        )

        fardoes_data.append(Fardao(**data))

    plumas = PlumaGatec.objects.filter(safra=2016).using('oracle')
    Fardao.objects.bulk_create(fardoes_data)

    for pluma in plumas:

        print(pluma)

        data = dict(
            id=pluma.id,
            empresa=pluma.empresa_id,
            fardao_id=pluma.fardao_id,
            safra=pluma.safra,
            peso=pluma.peso,
            status=pluma.status,
        )
        plumas_data.append(Pluma(**data))


    Pluma.objects.bulk_create(plumas_data)