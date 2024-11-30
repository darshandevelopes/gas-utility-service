from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def dashboard(request):
    customer = request.user.customer
    service_requests = ServiceRequest.objects.filter(customer=customer).order_by('-created_at')
    return render(request, 'customer_service/dashboard.html', {'service_requests': service_requests})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def request_detail(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id, customer=request.user.customer)
    return render(request, 'customer_service/request_detail.html', {'service_request': service_request})


@login_required
def user_profile(request):
    user = request.user
    account_number = user.customer.account_number if hasattr(user, 'customer') else 'N/A'
    
    return render(request, 'customer_service/user_profile.html', {
        'user': user,
        'account_number': account_number,
    })
