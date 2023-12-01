from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

bd = [
    {"numero": "21345", "nombre": "Arnaldo", "saldo": 200, "contactos": ["123", "456"], "historial": []},
    {"numero": "123", "nombre": "Luisa", "saldo": 400, "contactos": ["456"], "historial": []},
    {"numero": "456", "nombre": "Andrea", "saldo": 300, "contactos": ["21345"], "historial": []},
]
@app.route('/')
def index():
     return render_template('index.html')


@app.route('/billetera/contactos')
def contactos():
    minumero = request.args.get('minumero')
    cuenta = next((c for c in bd if c['numero'] == minumero), None)
    if not cuenta:
        return jsonify({'error': 'Cuenta no encontrada'}), 404
    contactos = {contacto: next((c['nombre'] for c in bd if c['numero'] == contacto), None) for contacto in cuenta['contactos']}
    return jsonify(contactos)
@app.route('/billetera/pagar', methods=['GET', 'POST']) 
def pagar():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))
    cuenta_origen = next((c for c in bd if c['numero'] == minumero), None)
    cuenta_destino = next((c for c in bd if c['numero'] == numerodestino), None)
    if not cuenta_origen or not cuenta_destino:
        return jsonify({'error': 'Cuenta no encontrada'}), 404
    if cuenta_origen['saldo'] < valor:
        return jsonify({'error': 'Saldo insuficiente'}), 400
    if numerodestino not in cuenta_origen['contactos']:
        return jsonify({'error': 'El destino debe ser un contacto'}), 400
    # Realizar la operación
    cuenta_origen['saldo'] -= valor
    cuenta_destino['saldo'] += valor
    operacion = {
        'numero_destino': numerodestino,
        'valor': valor,
        'fecha': datetime.now().strftime("%d/%m/%Y")
    }
    cuenta_origen['historial'].append(operacion)
    return jsonify({'mensaje': f"Realizado en {operacion['fecha']}."})

@app.route('/billetera/historial')
def historial():
    minumero = request.args.get('minumero')
    cuenta = next((c for c in bd if c['numero'] == minumero), None)
    if not cuenta:
        return jsonify({'error': 'Cuenta no encontrada'}), 404
    historial_formatted = {
        'saldo': f"Saldo de {cuenta['nombre']}: {cuenta['saldo']}",
        'operaciones': [f"Pago {('recibido' if op['numero_destino'] == minumero else 'realizado')} de {op['valor']} de {c['nombre']}"
                        for op in cuenta['historial'] for c in bd if op['numero_destino'] == c['numero'] or c['numero'] == minumero]
    }
    return jsonify(historial_formatted)

if __name__ == '__main__':
    app.run(debug=True)