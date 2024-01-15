document.addEventListener('DOMContentLoaded', function () {
    // Initial load of all customers
    loadAllCustomers();

    // Search customer on button click
    document.getElementById('searchButton').addEventListener('click', searchCustomer);
});

function loadAllCustomers() {
    // Make an API request to get all customers
    fetch('/view_all/')
        .then(response => response.json())
        .then(displayCustomerCards)
        .catch(error => console.error('Error fetching all customers:', error));
}

function searchCustomer() {
    // Get customer ID from input
    const customerId = document.getElementById('customerIdInput').value;

    // Make an API request to search for a customer
    fetch(`/find/${customerId}/`)
        .then(response => response.json())
        .then(data => displayCustomerCards([data])) // Display the searched customer
        .catch(error => console.error('Error searching customer:', error));
}

function displayCustomerCards(customers) {
    const customerCardsContainer = document.getElementById('customerCards');
    customerCardsContainer.innerHTML = ''; // Clear previous cards

    customers.forEach(customer => {
        const card = createCustomerCard(customer);
        customerCardsContainer.appendChild(card);
    });
}

function createCustomerCard(customer) {
    const card = document.createElement('div');
    card.className = 'card m-2';
    card.style = 'width: 18rem;';

    const cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    const cardTitle = document.createElement('h5');
    cardTitle.className = 'card-title';
    cardTitle.textContent = `Customer ID: ${customer.customer_id}`;

    const cardText = document.createElement('p');
    cardText.className = 'card-text';
    cardText.textContent = `VoIP Usage: ${customer.voip_usage}, SMS Usage: ${customer.sms_usage}, Storage Usage: ${customer.storage_usage}, Subscription: ${customer.subscription}, Usage Date: ${customer.usage_date}`;

    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardText);
    card.appendChild(cardBody);

    return card;
}
