from django.shortcuts import render, get_object_or_404
import requests  # Import the requests module
from .models import Customer
from django.http import JsonResponse, HttpResponse

def dashboard(request):
    return render(request, 'dashboard.html')


def call_api(request):
    node_api_url = 'http://localhost:3000/usage-data'
    api_key = 'UHNhbG0gMTUwOjYgTGV0IGV2ZXJ5dGhpbmcgdGhhdCBoYXMgYnJlYXRoIHByYWlzZSB0aGUgTG9yZA'

    headers = {'x-api-key': api_key}

    try:
        response = requests.get(node_api_url, headers=headers)

        if response.status_code == 200:
            customer_info = response.json()

            for customer_data in customer_info:
                # Calculate total cost based on pricing plan
                total_cost = calculate_usage_cost(
                    customer_data['voip_usage'],
                    customer_data['sms_usage'],
                    int(customer_data['storage_usage'].rstrip('GB')),  # Remove 'GB' and convert to int
                    customer_data['subscription']
                )

                # Update the Customer model with the total cost
                Customer.objects.update_or_create(
                    customer_id=customer_data['id'],
                    defaults={'voip_usage': customer_data['voip_usage'],
                              'sms_usage': customer_data['sms_usage'],
                              'storage_usage': int(customer_data['storage_usage'].rstrip('GB')),
                              'subscription': customer_data['subscription'],
                              'total_cost': total_cost}
                )

            return JsonResponse({'message': 'Data updated successfully'})
        else:
            print(f"Failed to fetch customer info. Status code: {response.status_code}")
            return JsonResponse({'error': 'Failed to fetch customer info'}, status=500)

    except Exception as e:
        print(f"Error during API request: {str(e)}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
    
def view_all(request):
    customers = Customer.objects.all()
    data = [{'customer_id': customer.customer_id,
             'voip_usage': customer.voip_usage,
             'sms_usage': customer.sms_usage,
             'storage_usage': customer.storage_usage,
             'subscription': customer.subscription,
             'total_cost': customer.total_cost,
             'usage_date': customer.usage_date} for customer in customers
            ]
    return JsonResponse(data, safe=False)

def calculate_usage_cost(voip_usage, sms_usage, storage_usage_gb, subscription):
    # Define pricing for Standard and Premium subscriptions
    standard_rates = {'voip': 0.1, 'sms': 0.05, 'storage': 0.2}
    premium_rates = {'voip': 0.08, 'sms': 0.03, 'storage': 0.15, 'subscription_fee': 5.0}

    # Calculate usage cost based on subscription type
    if subscription == 'Standard':
        total_cost = (
            (voip_usage * standard_rates['voip']) +
            (sms_usage * standard_rates['sms']) +
            (storage_usage_gb * standard_rates['storage'])
        )
    elif subscription == 'Premium':
        total_cost = (
            (voip_usage * premium_rates['voip']) +
            (sms_usage * premium_rates['sms']) +
            (storage_usage_gb * premium_rates['storage']) +
            premium_rates['subscription_fee']
        )
    else:
        # Handle unknown subscription type
        total_cost = 0.0

    return total_cost

def find_customer(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    data = {
        'customer_id': customer.customer_id,
        'voip_usage': customer.voip_usage,
        'sms_usage': customer.sms_usage,
        'storage_usage': customer.storage_usage,
        'subscription': customer.subscription,
        'total_cost': customer.total_cost,
        'usage_date': customer.usage_date,
    }
    return JsonResponse(data)
