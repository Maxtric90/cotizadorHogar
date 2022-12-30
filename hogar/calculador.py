def calculador(cotizacion):
    COBERTURAS = {
        1: {'nombre': 'Incendio a primer riesgo absoluto', 
            'tasa': '0.001'},
        2: {'nombre': 'Incendio contenido a primer riesgo absoluto',
            'tasa': '0.002'},
        3: {'nombre': 'Robo y/o hurto del contenido general',
            'tasa': '0.0015'},
        4: {'nombre': 'Gastos de limpieza, retiro de escombros, demolición del edificio',
            'tasa': '0.0015'},
        5: {'nombre': 'Gastos de limpieza, retiro del mobiliario',
            'tasa': '0.0015'},
        6: {'nombre': 'HCVT (Huracán - Vendaval - Ciclon - Tornado',
            'tasa': '0.0015'},
        7: {'nombre': 'Granizo',
            'tasa': '0.0015'},
        8: {'nombre': 'Gastos de alojamiento',
            'tasa': '0.0015'},
        9: {'nombre': 'Responsabilidad civil por incendio o explosión',
            'tasa': '0.0015'},
        10: {'nombre': 'Bauleras y dependencias anexas',
            'tasa': '0.0015'},
        11: {'nombre': 'Objetos específicos: todo riesgo en domicilio',
            'tasa': '0.0015'},
        12: {'nombre': 'Electrónicos',
            'tasa': '0.0015'},
        13: {'nombre': 'Electrodomésticos - Aparatos o equipos electrónicos de uso doméstico',
            'tasa': '0.0015'},
        14: {'nombre': 'Accidentes personales',
            'tasa': '0.0015'},
        15: {'nombre': 'Cristales',
            'tasa': '0.0015'},
        16: {'nombre': 'Responsabilidad civil hechos privados',
            'tasa': '0.0015'},
        17: {'nombre': 'Daños por agua',
            'tasa': '0.0015'},
        18: {'nombre': 'Pérdidas de alimentos en freezer',
            'tasa': '0.0015'},
        19: {'nombre': 'Palos de golf',
            'tasa': '0.0015'},
        20: {'nombre': 'Daños estéticos',
            'tasa': '0.0015'},
    }

    prima = 0

    prima += cotizacion['cob1_capital'] * float(COBERTURAS[1]['tasa'])
    prima += cotizacion['cob2_capital'] * float(COBERTURAS[2]['tasa'])
    prima += cotizacion['cob3_capital'] * float(COBERTURAS[3]['tasa'])
    prima += cotizacion['cob4_capital'] * float(COBERTURAS[4]['tasa'])
    prima += cotizacion['cob5_capital'] * float(COBERTURAS[5]['tasa'])
    prima += cotizacion['cob6_capital'] * float(COBERTURAS[6]['tasa'])
    prima += cotizacion['cob7_capital'] * float(COBERTURAS[7]['tasa'])
    prima += cotizacion['cob8_capital'] * float(COBERTURAS[8]['tasa'])
    prima += cotizacion['cob9_capital'] * float(COBERTURAS[9]['tasa'])
    prima += cotizacion['cob10_capital'] * float(COBERTURAS[10]['tasa'])
    prima += cotizacion['cob11_capital'] * float(COBERTURAS[11]['tasa'])
    prima += cotizacion['cob12_capital'] * float(COBERTURAS[12]['tasa'])
    prima += cotizacion['cob13_capital'] * float(COBERTURAS[13]['tasa'])
    prima += cotizacion['cob14_capital'] * float(COBERTURAS[14]['tasa'])
    prima += cotizacion['cob15_capital'] * float(COBERTURAS[15]['tasa'])
    prima += cotizacion['cob16_capital'] * float(COBERTURAS[16]['tasa'])
    prima += cotizacion['cob17_capital'] * float(COBERTURAS[17]['tasa'])
    prima += cotizacion['cob18_capital'] * float(COBERTURAS[18]['tasa'])
    prima += cotizacion['cob19_capital'] * float(COBERTURAS[19]['tasa'])
    prima += cotizacion['cob20_capital'] * float(COBERTURAS[20]['tasa'])

    desglosePremio ={
        'prima': prima,
        'premio': prima * 0.21,
        'comision': prima * 0.2
    }

    return desglosePremio