from django.shortcuts import render
from .forms import VendorUploadForm  # Make sure you have imported the VendorUploadForm from the correct location
from vendor.models import Vendor

def vendor_create_view(request):
    if request.method == 'POST':
        form = VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # If the form is not valid, re-render the form with the error messages
            return render(request, "vendor/vendor_form.html", {"form": form})
    else:
        form = VendorUploadForm()  # Create an instance of the form for GET request

    return render(request, "vendor/vendor_form.html", {"form": form})

def vendor_list(request):
    vendors = Vendor.objects.all()  # Renamed the variable to 'vendors' for clarity
    return render(request, "vendor/vendor_list.html", {"vendors": vendors})
