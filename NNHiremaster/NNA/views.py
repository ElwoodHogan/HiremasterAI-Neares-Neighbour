from django.shortcuts import render
from .RandomPointGenerator import get_min_max_values, generate_random_data_point

def demo_view(request):
    if request.method == 'POST':
        min_max_values = get_min_max_values()
        html_content = generate_random_data_point(min_max_values)
        return render(request, 'demopage.html', {'html_content': html_content})
    else:
        return render(request, 'demopage.html')