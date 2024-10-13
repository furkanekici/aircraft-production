from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Part
from .forms import PartForm
from rest_framework import viewsets
from .serializers import PartSerializer

# Create Part View
@login_required
def create_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            # Assign the part to the team of the logged-in personnel
            team = request.user.personnel.teams.first()
            
            # Ensure that the team's responsibility matches the part type
            if (
                (part.part_type == 'wing' and team.team_type != 'wing') or
                (part.part_type == 'fuselage' and team.team_type != 'fuselage') or
                (part.part_type == 'tail' and team.team_type != 'tail') or
                (part.part_type == 'avionics' and team.team_type != 'avionics')
            ):
                return HttpResponseForbidden("Your team cannot create this type of part.")
            
            part.team = team
            part.save()
            return redirect('parts_list')  # Redirect to a parts list view
    else:
        form = PartForm()

    return render(request, 'parts/create_part.html', {'form': form})

# Update Part View
@login_required
def update_part(request, part_id):
    part = get_object_or_404(Part, id=part_id)

    # Ensure only the part's team can update it
    if part.team != request.user.personnel.teams.first():
        return HttpResponseForbidden("You don't have permission to update this part.")

    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('parts_list')  # Redirect to a parts list view (to be implemented)
    else:
        form = PartForm(instance=part)

    return render(request, 'parts/update_part.html', {'form': form})

# Delete Part View
@login_required
def delete_part(request, part_id):
    part = get_object_or_404(Part, id=part_id)

    # Ensure only the part's team can delete it
    if part.team != request.user.personnel.teams.first():
        return HttpResponseForbidden("You don't have permission to delete this part.")

    if request.method == 'POST':
        part.delete()
        return redirect('parts_list')  # Redirect to a parts list view (to be implemented)

    return render(request, 'parts/confirm_delete.html', {'part': part})

# Placeholder view for listing parts (to be implemented)
@login_required
def parts_list(request):
    # Example: Fetch parts based on the team of the logged-in personnel
    parts = Part.objects.filter(team=request.user.teams.first())
    return render(request, 'parts/parts_list.html', {'parts': parts})

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
