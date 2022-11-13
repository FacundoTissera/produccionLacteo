meses=  ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
# valores de entrada
cantidadDeProduccion= [];
costoDeProduccion= [];

# valores de salida
promedioUnidadesProducidas= [];
promedioAnualProduccion= 0;
costoProduccionBajo= 0;
costoTotalProduccionMensual= 0;

for i in range(0,12):

    # le digo la cantidad de unidades producidas en cada mes;
    print(f'ingrese la cantidad de unidades producidas en el mes de {meses[i]}');
    cantidadDeProduccion.append(int(input()));

    # le digo el costo de produccion en cada mes;
    print(f'ingrese el costo de produccion en el mes de {meses[i]}');
    costoDeProduccion.append(float(input()));

print('\n');

print('MESES\t\t\t\tCANTIDAD\t\t\tCOSTO\t\t\t\tTOTAL MENSUAL');

for i in range(0,12):

    # calculo el costo total de produccion mensual
    costoTotalProduccionMensual = cantidadDeProduccion[i] * costoDeProduccion[i];

    # imprimo los valores de salida
    print(f'{meses[i]}\t\t\t\t{cantidadDeProduccion[i]}\t\t\t\t{costoDeProduccion[i]}\t\t\t\t{costoTotalProduccionMensual}');


print('\n');

# promedio de unidades producidas en el año
promedioUnidadesProducidas = sum(cantidadDeProduccion) / 3;
print(f'promedio de unidades producidas en el año: {promedioUnidadesProducidas}');

# promedio de costo de produccion anual
promedioAnualProduccion = sum(costoDeProduccion) / 3;
print(f'promedio de costo de produccion anual: {promedioAnualProduccion}');

# COSTO DE PRODUCCION MAS BAJO
costoProduccionBajo = min(costoDeProduccion);
print(f'El costo de produccion bajo es: {costoProduccionBajo} del mes de {meses[costoDeProduccion.index(costoProduccionBajo)]}');

