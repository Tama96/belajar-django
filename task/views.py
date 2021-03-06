from django.shortcuts import render, redirect

from . import models, forms

def index(req):
  form_input = forms.TaskForm()

  if req.POST:
    form_input = forms.TaskForm(req.POST)

    if form_input.is_valid():
      form_input.save()

  tasks = models.Task.objects.all()
  return render(req, 'task/index.html', {
    'data': tasks,
    'form': form_input,
  })

def detail(req, id):
  task = models.Task.objects.filter(pk=id).first()
  return render(req, 'task/detail.html', {
    'data': task,
  })

def delete(req, id):
  models.Task.objects.filter(pk=id).delete()
  return redirect('/')

def edit(req, id):
  if req.POST:
    task = models.Task.objects.filter(pk=id).update(name=req.POST['name'])
    return redirect('/')

  task = models.Task.objects.filter(pk=id).first()
  return render(req, 'task/edit.html', {
    'data': task,
  })
