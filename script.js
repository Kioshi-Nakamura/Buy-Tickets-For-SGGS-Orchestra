let totalPrice = 0;

// Define ticket prices and emojis for each category
const prices = {
    "pelajar sggs": 12.00,
    "guru sggs": 14.00,
    "orang awam <12": 5.50,
    "orang awam 13-50": 20.00,
    "orang awam 51+": 15.00
};

const symbols = {
    "pelajar sggs": "🎓",
    "guru sggs": "👩‍🏫",
    "orang awam <12": "🦄",
    "orang awam 13-50": "🎸",
    "orang awam 51+": "🎻"
};

// Function to add a ticket
function addTicket() {
    const category = document.getElementById('category').value;
    const ticketPrice = prices[category];
    const ticketSymbol = symbols[category];

    // Add the ticket price to the total
    totalPrice += ticketPrice;

    // Create ticket item and display it
    const ticketItem = document.createElement('div');
    ticketItem.classList.add('ticket-item');
    ticketItem.innerHTML = `💸 ${category.replace(/_/g, " ")}: RM${ticketPrice.toFixed(2)} ${ticketSymbol}`;
    
    document.getElementById('tickets-list').appendChild(ticketItem);

    // Update total price displayed
    updateTotalPrice();
}

// Function to update the total price display
function updateTotalPrice() {
    document.getElementById('total-price').textContent = totalPrice.toFixed(2);
}

// Function to handle purchase completion
function finishPurchase() {
    if (totalPrice === 0) {
        alert("Please add tickets first!");
    } else {
        alert(`Purchase complete! Total amount: RM${totalPrice.toFixed(2)}`);
        resetForm();
    }
}

// Function to reset the form after purchase
function resetForm() {
    totalPrice = 0;
    document.getElementById('total-price').textContent = "0.00";
    document.getElementById('tickets-list').innerHTML = '';
}
