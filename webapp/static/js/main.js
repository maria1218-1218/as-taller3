// Funcionalidad JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar componentes cuando cargue la página
    console.log('Página cargada y lista');
});

// Función para agregar productos al carrito con AJAX
function addToCart(productId) {
    // Implementar agregado al carrito
    fetch(`/add-to-cart/${productId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        alert('Producto agregado al carrito');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error al agregar producto al carrito');
    });
}

// Función para actualizar cantidad en el carrito
function updateCartQuantity(itemId, quantity) {
    // Implementar actualización de cantidad
    if (quantity <= 0) {
        removeFromCart(itemId);
        return;
    }
    fetch(`/update-cart/${itemId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ quantity: quantity })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Carrito actualizado');
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Función para remover items del carrito
function removeFromCart(itemId) {
    // Implementar remoción de items
    if (confirm('¿Estás seguro de que deseas eliminar este producto?')) {
        fetch(`/remove-from-cart/${itemId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Producto removido del carrito');
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}
