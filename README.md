# ExamenSoftware
## Pregunta 1
![image](https://github.com/PaolaMag/ExamenSoftware/assets/91236162/f495e21f-900e-4f17-8099-bf3d7476319f)
![image](https://github.com/PaolaMag/ExamenSoftware/assets/91236162/cf0e0c7b-bd4a-45e9-8c61-23c3cdf147ba)
![image](https://github.com/PaolaMag/ExamenSoftware/assets/91236162/ee248e92-d25c-4ca4-8a60-da0bea441203)

## Pregunta 3
### Cambios en el Código (Clases / Métodos)
- Modificar la Clase Cuenta:
Se agregaria un nuevo atributo para rastrear las transferencias realizadas en el día actual, podría ser un diccionario o una lista que almacene las fechas y los montos transferidos.
- Modificar el Método de Pago:
Se actualizaria el método pagar en la clase Cuenta para verificar el límite diario antes de realizar la transacción, se tendria que sumar el monto de todas las transferencias realizadas en el día actual y rechazar la operación si agregar el nuevo monto excede el límite de 200 soles.
- Resetear el Contador Diario:
Se podria implementar la opcion de resetear el contador de transferencias cada día.
### Nuevos Casos de Prueba a Adicionar
- Transferencia dentro del Límite Diario:
Probar que se pueden realizar múltiples transferencias en un día siempre que no exceda los 200 soles.
- Exceder el Límite Diario:
Verificar que si excede el límite de 200 soles en un día sea rechazada.
- Resetear el Contador Diario:
Asaegurarnos que el contador de transferencias se resetee correctamente al cambiar el día.
### Riesgo de "Romper" lo que ya Funciona
Riesgo Medio a Alto:
Si hace algun cambio en la lógica puede generar un riesgo ya que como bien puede producir errores en partes del código que ya funcionaban correctamente o puede resultar exitoso la integración de esta.
