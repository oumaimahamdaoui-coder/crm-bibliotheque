from django.shortcuts import render, redirect
from .models import Livre, Emprunt
from .forms import LivreForm, EmpruntForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    livres = Livre.objects.all()
    emprunts = Emprunt.objects.all()

    # 📊 Dashboard stats
    total_livres = livres.count()
    total_emprunts = emprunts.count()

    emprunts_retard = 0
    total_amendes = 0

    for e in emprunts:
        if e.jours_retard() > 0:
            emprunts_retard += 1
        total_amendes += e.amende()

    return render(request, 'library/home.html', {
        'livres': livres,
        'emprunts': emprunts,
        'total_livres': total_livres,
        'total_emprunts': total_emprunts,
        'emprunts_retard': emprunts_retard,
        'total_amendes': total_amendes,
    })


def add_livre(request):
    form = LivreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'library/form.html', {'form': form})


def add_emprunt(request):
    form = EmpruntForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'library/form.html', {'form': form})
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="emprunts.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 800, "Liste des Emprunts")

    y = 750

    emprunts = Emprunt.objects.all()

    for e in emprunts:
        text = f"{e.nom_etudiant} | {e.livre} | Retard: {e.jours_retard} | Amende: {e.amende} DH"
        p.setFont("Helvetica", 10)
        p.drawString(50, y, text)
        y -= 20

    p.showPage()
    p.save()

    return response
