from django.shortcuts import render
import requests

# Create your views here.
KOBO_TOKEN = "YOUR_KOBO_API_TOKEN"

MEMBER_FORM_ID = "ASSET_ID_MEMBER"
SAVINGS_FORM_ID = "ASSET_ID_SAVINGS"
TRANSACTION_FORM_ID = "ASSET_ID_TRANSACTION"

KOBO_URL_TEMPLATE = "https://kf.kobotoolbox.org/api/v2/assets/{asset_id}/data/"

def fetch_kobo_data(asset_id):
    url = KOBO_URL_TEMPLATE.format(asset_id = asset_id)
    headers = {"Authorization": f"Token {KOBO_TOKEN}"}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

def members_dashboard(request):
    members = fetch_kobo_data(MEMBER_FORM_ID)
    return render(request, "api/members.html", {"members": members})

def savings_dashboard(request):
    savings = fetch_kobo_data(SAVINGS_FORM_ID)
    return render(request, "api/savings.html", {"savings": savings})

def transactions_dashboard(request):
    transactions = fetch_kobo_data(TRANSACTION_FORM_ID)
    return render(request, "api/transactions.html", {"transactions": transactions})