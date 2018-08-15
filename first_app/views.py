from django.shortcuts import render
from .models import Tree
from django.shortcuts import render, get_object_or_404



# Create your views here.
def trees_list(request):
	trees = Tree.objects.all()
	return render(request, 'trees/index.html', {'trees': trees})

def tree_detail(request, id):
	tree = Tree.objects.get(id)
	return render(request, 'trees/tree_detail.html', {'tree': tree})
	
def tree_create(request):
	if request.method == 'POST':
		form = TreeForm(request.POST)
		