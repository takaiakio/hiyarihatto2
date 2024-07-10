from django.shortcuts import render, redirect, get_object_or_404
from .forms import HiyariHattoForm
from .models import HiyariHatto
import csv
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = HiyariHattoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HiyariHattoForm()
    return render(request, 'posts/index.html', {'form': form})

def export_to_csv(request):
    hiyarihatto_list = HiyariHatto.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hiyarihatto.csv"'

    response.write('\ufeff')

    writer = csv.writer(response)
    writer.writerow(['題名', '工程', 'やるべきこと', 'ヒヤリとした場面', '気づけなければ、どうなるのか', '回避事由', '危険度', '様態評価', '作成日時'])

    for hiyarihatto in hiyarihatto_list:
        writer.writerow([hiyarihatto.title, hiyarihatto.process, hiyarihatto.action, hiyarihatto.situation,
                         hiyarihatto.consequence, hiyarihatto.avoidance, hiyarihatto.danger_level, hiyarihatto.get_phase_display(),
                         hiyarihatto.created_at])

    return response

def list_posts(request):
    posts = HiyariHatto.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(HiyariHatto, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def success(request):
    return render(request, 'posts/success.html')

def delete_post(request, post_id):
    post = get_object_or_404(HiyariHatto, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('list_posts')
    return render(request, 'posts/delete_confirm.html', {'post': post})




