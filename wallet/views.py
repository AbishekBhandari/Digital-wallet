from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Transaction
from .forms import LoadMoneyForm, TransferMoneyForm, RegistrationForm
from django.contrib.auth.models import User

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    wallet, _ = Client.objects.get_or_create(user=request.user)
    transactions = Transaction.objects.filter(wallet=wallet).order_by('-timestamp')
    return render(request, 'dashboard.html', {'wallet': wallet, 'latest_transactions': transactions})

@login_required
def load_money(request):
    if request.method == 'POST':
        form = LoadMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            client, _ = Client.objects.get_or_create(user=request.user)
            print(request.user)
            client.balance += amount
            client.save()
            Transaction.objects.create(wallet=client, amount=amount, transaction_type='Credit')
            messages.success(request, 'Money loaded successfully!')
            return redirect('dashboard')
    else:
        form = LoadMoneyForm()
    return render(request, 'load_money.html', {'form': form})

@login_required
def transfer_money(request):
    if request.method == 'POST':
        form = TransferMoneyForm(request.POST)
        if form.is_valid():
            recipient_username = form.cleaned_data['recipient']
            amount = form.cleaned_data['amount']
            try:
                recipient = User.objects.get(username=recipient_username)
                sender_wallet, _ = Client.objects.get_or_create(user=request.user)
                recipient_wallet, _ = Client.objects.get_or_create(user=recipient)
                
                if sender_wallet.balance >= amount:
                    sender_wallet.balance -= amount
                    recipient_wallet.balance += amount
                    sender_wallet.save()
                    recipient_wallet.save()
                    
                    Transaction.objects.create(wallet=sender_wallet, amount=amount, transaction_type='Debit')
                    Transaction.objects.create(wallet=recipient_wallet, amount=amount, transaction_type='Credit')
                    
                    messages.success(request, 'Transfer successful!')
                    return redirect('dashboard')
                else:
                    error = 'Insufficient balance!'
                    return render(request, 'transfer_money.html', {'form': form, 'error': error})
            except User.DoesNotExist:
                    error ='Recipient not found!'
                    return render(request, 'transfer_money.html', {'form': form, 'error': error})
    else:
        form = TransferMoneyForm()
        return render(request, 'transfer_money.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration successful! Welcome, " + user.username)
            return redirect('dashboard')
        else:
            messages.error(request, "Please fix the errors below.")
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html')
