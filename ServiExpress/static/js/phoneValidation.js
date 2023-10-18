// Obtener referencia al campo de texto y al mensaje de error
var phoneInput = document.getElementById('phoneInput');
var phoneError = document.getElementById('phoneError');

// Agregar evento de cambio al campo de texto
phoneInput.addEventListener('input', function() {
    // Limpiar el mensaje de error previo
    phoneError.textContent = '';

    // Obtener el valor del número telefónico ingresado
    var phoneNumber = phoneInput.value;

    // Expresión regular para validar el número telefónico
    var phoneRegex = /^\d{7,20}$/;

    // Verificar si el número telefónico cumple con el patrón
    if (!phoneRegex.test(phoneNumber)) {
        phoneError.textContent = 'El número telefónico no es válido.';
    }
});
