from django.shortcuts import render
from forms import ScoreForm

    100m = 0
    200m = 0
    400m = 0
    800m = 0
    1500m = 0
    110mH = 0
    high_jump = 0
    pole_vault = 0
    long_jump = 0
    shot = 0
    discus = 0
    javeline = 0
    60m = 0
    1000m = 0
    60mH = 0

def scores(request):
    # form = ScoreForm()
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            player_name = cd.get('player_name')
            gender = cd.get('gender')
            100m = cd.get('100m')
            200m = cd.get('200m')
            400m = cd.get('400m')
            1500m = cd.get('1500m')
            110mH = cd.get('110mH')
            high_jump = cd.get('high_jump')
            pole_vault = cd.get('pole_vault')
            long_jump = cd.get('long_jump')
            shot = cd.get('shot')
            discus = cd.get('discus')
            javeline = cd.get('javeline')
            60m = cd.get('60m')
            1000m = cd.get('1000m')
            60mH = cd.get('60mH')

            if gender == 'Male':
                points_100m = 25.4347*((18.00-100m)**1.81)
                points_200m = 5.8425*((38.00-200m)**1.81)
                points_400m = 1.53775*((82.00-400m)**1.81)
                points_1500m = 0.03768*((480.00-1500m)**1.81)
                points_110mH = 5.74352*((25.50-110mH)**1.81)
                points_high_jump = 0.8465*((high_jump-75.00)**1.42)
                points_pole_vault = 0.2797*((pole_vault-100.00)**1.35)
                points_long_jump = 0.14354*((long_jump-220.00)**1.40)
                points_shot = 51.39*((shot-1.50)**1.05)
                points_discus = 12.91*((discus-4.00)**1.10)
                points_javeline = 10.14*((javelin-7.00)**1.08)
                points_60m = 58.0150*((11.50-60m)**1.81)
                points_1000m = 0.08713*((305.50-1000m)**1.85)
                points_60mH = 20.5173*((15.50-60mH)**1.92)
            else:
                points_200m = 4.99087*((42.50-200m)**1.81)
                points_800m = 0.11193*((254.00-800m)**1.88)
                points_100mH = 9.23076*((26.70-100mH)**1.835)
                points_high_jump = 1.84523*((high_jump-75.00)**1.348)
                points_long_jump = 0.188807*((long_jump-210.00)**1.41)
                points_shot = 56.0211*((shot-1.50)**1.05)
                points_javeline = 15.9803*((javelin-3.80)**1.04)
                points_100m = 17.8570*((21.00-100m)**1.81)
                points_400m = 1.34285*((91.7-400m)**1.81)
                points_1500m = 0.02883*((535.00-1500m)**1.88)
                points_pole_vault = 0.44125*((pole_vault-100.00)**1.35)
                points_discus = 12.3311*((discus-3.00)**1.10)
                points_60mH = 20.0479*((17.00-60mH)**1.835)