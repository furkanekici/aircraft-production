from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from parts.models import Part
from .models import Aircraft

@login_required
def assemble_aircraft(request):
    # Fetch the aircraft type from the request or default to TB2
    aircraft_type_code = request.GET.get('aircraft_type', 'tb2')
    
    # Get the actual Aircraft instance corresponding to the aircraft type
    aircraft_type = get_object_or_404(Aircraft, aircraft_type=aircraft_type_code)
    
    if not aircraft_type:
        return HttpResponse(f"No aircraft of type {aircraft_type_code} found. Please create one.")

    # Fetch available parts for the aircraft
    wings = Part.objects.filter(part_type='wing', aircraft_type=aircraft_type)
    fuselages = Part.objects.filter(part_type='fuselage', aircraft_type=aircraft_type)
    tails = Part.objects.filter(part_type='tail', aircraft_type=aircraft_type)
    avionics = Part.objects.filter(part_type='avionics', aircraft_type=aircraft_type)

    # Ensure all parts are available
    if not wings.exists():
        return HttpResponse(f"Error: Missing wing for {aircraft_type}.")
    if not fuselages.exists():
        return HttpResponse(f"Error: Missing fuselage for {aircraft_type}.")
    if not tails.exists():
        return HttpResponse(f"Error: Missing tail for {aircraft_type}.")
    if not avionics.exists():
        return HttpResponse(f"Error: Missing avionics for {aircraft_type}.")

    if request.method == 'POST':
        selected_wing = request.POST.get('wing')
        selected_fuselage = request.POST.get('fuselage')
        selected_tail = request.POST.get('tail')
        selected_avionics = request.POST.get('avionics')

        if selected_wing and selected_fuselage and selected_tail and selected_avionics:
            # Create the assembled aircraft
            aircraft = Aircraft.objects.create(
                aircraft_type=aircraft_type_code,
                wing_id=selected_wing,
                fuselage_id=selected_fuselage,
                tail_id=selected_tail,
                avionics_id=selected_avionics,
                assembled=True
            )

            # Mark parts as used (you can also delete them if that's the intended functionality)
            Part.objects.filter(id__in=[selected_wing, selected_fuselage, selected_tail, selected_avionics]).delete()

            return redirect('aircraft_list')

    return render(request, 'aircrafts/assemble_aircraft.html', {
        'wings': wings,
        'fuselages': fuselages,
        'tails': tails,
        'avionics': avionics,
        'aircraft_type': aircraft_type_code,
    })

# Aircraft List View
@login_required
def aircraft_list(request):
    # Fetch and display all assembled aircraft
    aircrafts = Aircraft.objects.filter(assembled=True)
    return render(request, 'aircrafts/aircraft_list.html', {'aircrafts': aircrafts})
