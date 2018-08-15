from django.shortcuts import render
from .models import Tree
from django.shortcuts import render, get_object_or_404



# Create your views here.
def trees_list(request):
	trees = Tree.objects.all()
	return render(request, 'trees/index.html', {'trees': trees})

def tree_show(request, pk):
	tree = get_object_or_404(Tree, pk=pk)
    return render(request, 'trees/tree_show.html', {'tree': tree})
	
