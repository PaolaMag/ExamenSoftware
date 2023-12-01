import unittest
from app import app
import json

class FlaskTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # Caso de éxito:
    def test_contactos_success(self):
        response = self.app.get('/billetera/contactos?minumero=21345')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('123', data)  
        self.assertIn('456', data) 

    # Caso de error de cuenta no encontrada 
    def test_contactos_cuenta_no_encontrada(self):
        response = self.app.get('/billetera/contactos?minumero=00000')
        self.assertEqual(response.status_code, 404)

    # Caso de error de saldo insuficiente 
    def test_pagar_saldo_insuficiente(self):
        response = self.app.post('/billetera/pagar?minumero=21345&numerodestino=123&valor=1000')
        self.assertEqual(response.status_code, 400)

    # Caso de error de verificar el manejo de cuenta no encontrada en pagos
    def test_pagar_cuenta_no_encontrada(self):
        response = self.app.post('/billetera/pagar?minumero=00000&numerodestino=123&valor=50')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
