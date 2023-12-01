function verContactos() {
    const numero = document.getElementById('numero_contactos').value;
    fetch(`/billetera/contactos?minumero=${numero}`)
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById('lista_contactos');
            lista.innerHTML = ''; 
            for (const contacto in data) {
                const li = document.createElement('li');
                li.textContent = `${contacto}: ${data[contacto]}`;
                lista.appendChild(li);
            }
        });
}

function realizarPago() {
    const numeroOrigen = document.getElementById('numero_origen').value;
    const numeroDestino = document.getElementById('numero_destino').value;
    const valor = document.getElementById('valor').value;
    fetch(`/billetera/pagar?minumero=${numeroOrigen}&numerodestino=${numeroDestino}&valor=${valor}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('respuesta_pago').textContent = data.mensaje || 'Error al realizar el pago';
    });
}

function verHistorial() {
    const numero = document.getElementById('numero_historial').value;
    fetch(`/billetera/historial?minumero=${numero}`)
        .then(response => response.json())
        .then(data => {
            const detalles = document.getElementById('detalles_historial');
            detalles.innerHTML = `Saldo: ${data.saldo}<br>`;
            detalles.innerHTML += 'Operaciones:<br>';
            data.operaciones.forEach(op => {
                detalles.innerHTML += `${op}<br>`;
            });
        });
}
