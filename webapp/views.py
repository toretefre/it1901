from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Konserter, Band, Tekniske_behov, Backline, Band
from django.shortcuts import render, redirect
from .forms import PostBehov, PostBackline
from django.utils import timezone

# Create your views here.
@login_required
def arrangoer_mainpage(request):
    if request.user.groups.filter(name="arrangoer").exists():
        konserts = Konserter.objects.all()
        return render(request,'webapp/arrangoer_mainpage.html',{'konserts':konserts})
    else:
        raise PermissionDenied

@login_required
def oversiktsview_konserter(request):
    if request.user.groups.filter(name="arrangoer").exists():
        konserter = Konserter.objects.all()
        scener = []
        for konsert in konserter:
            if konsert.scene not in scener:
                scener.append(konsert.scene)
        return render(request, 'webapp/oversiktsview_konserter.html', {'konserter':konserter, 'scener':scener})
    else:
        raise PermissionDenied

def login():
    return HttpResponse("login")


@login_required
def logout(request):
    return HttpResponse("User logged out")

@login_required
def redirect_login(request):
    if len(request.user.groups.all()) > 0:
        return HttpResponseRedirect(reverse(str(request.user.groups.all()[0])))
    else:
        raise PermissionDenied

@login_required
def arrangoer(request):
    if request.user.groups.filter(name="arrangoer").exists():
        return render(request,'webapp/arrangoer.html',{})
    else:
        raise PermissionDenied


@login_required
def tech_view(request):
    if request.user.groups.filter(name="teknikker").exists():
        konserter = Konserter.objects.filter(teknikere__icontains = request.user)
        return render(request, "webapp/tekniker_view.html", {'konserts': konserter})
    else:
        raise PermissionDenied

@login_required
def bookingansvarlig(request):
    if request.user.groups.filter(name="bookingansvarlig").exists():
        return render(request,'webapp/bookingansvarlig.html',{})
    else:
        raise PermissionDenied

@login_required
def bookingansvarlig_tidligere_konserter(request):
    if request.user.groups.filter(name="bookingansvarlig").exists():
        konserter = Konserter.objects.all()
        sjangre = ["-----"]
        tidligere_konserter = []
        kommende_festivaler = []
        tidligere_festivaler = []
        today = timezone.now()
        for konsert in konserter:
            # Går gjennom alle band i en konsert
            for band in konsert.band.all():
                # Finner alle individuelle sjangre
                if band.sjanger not in sjangre:
                    sjangre.append(band.sjanger)
            # Finner alle konserter hvor dato er senere enn dagens
            if konsert.festival not in kommende_festivaler and konsert.dato > today:
                kommende_festivaler.append(konsert.festival)
            # Finner alle konserter hvor dato er tidligere enn dagens, kunne sikkert hatt "else"
            if konsert.festival not in tidligere_festivaler and konsert.dato <= today:
                tidligere_festivaler.append(konsert.festival)
        # Fjerner pågående festivaler, festivaler med konserter både vært og kommende.
        for festival in tidligere_festivaler:
            if festival in kommende_festivaler:
                tidligere_festivaler.remove(festival)
        # Finner konserter som har vært
        for konsert in konserter:
            if konsert.festival in tidligere_festivaler:
                tidligere_konserter.append(konsert)

        return render(request,'webapp/bookingansvarlig_tidligere_konserter.html',{"tidligere_konserter":tidligere_konserter,"sjangre":sjangre})
    else:
        raise PermissionDenied


@login_required
def bookingansvarlig_tekniske_behov(request):
    if request.user.groups.filter(name="bookingansvarlig").exists():
        godkjente_bands = []
        konserter = Konserter.objects.all()
        today = timezone.now()

        for konsert in konserter:
            # Hent alle konserter som skal skjer nå eller i framtiden
            if konsert.dato >= today:
                # Hent alle band derfra fordi der ligger bare godkjente band
                        # Har gått gjennom bestillingen
                for band in konsert.band.all():
                    godkjente_bands.append(band)

        return render(request, 'webapp/bookingansvarlig_tekniske_behov.html', {"bands":godkjente_bands})

    else:
        raise PermissionDenied

@login_required
    def manager_mainpage(request):
    if request.user.groups.filter(name='manager').exists():
        band = Band.objects.all()
        backline = Backline.objects.all()
        behov = Tekniske_behov.objects.all()

        if request.method == 'POST' and 'submitBehov' in request.POST:
            behov_form = PostBehov(request.POST)
            if behov_form.is_valid():
                behov = behov_form.save(commit=False)
                behov.save()
                return redirect('webapp/manager_mainpage.html', pk=behov.pk)
        else:
            behov_form = PostBehov()

        if request.method == 'POST' and 'submitBackline' in request.POST:
            backline_form = PostBackline(request.POST)
            if backline_form.is_valid():
                backline = backline_form.save(commit=False)
                backline.save()
                return redirect('webapp/manager_mainpage.html', pk=backline.pk)

            else:
                backline_form = PostBackline()

        return render(request, 'webapp/manager_mainpage.html', {'band' : band, 'backline' : backline, 'behov' : behov, 'behov_form' : behov_form, 'backline_form' : backline_form})
