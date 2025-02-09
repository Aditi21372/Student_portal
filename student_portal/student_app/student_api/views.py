import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from .forms import RollNumberForm
from student_app.api_calls.api_utils import run_api_calls

logger = logging.getLogger(__name__)

@require_http_methods(["GET", "POST"])
def api_view(request):
    """View to handle API form submission and display results"""
    if request.method == 'POST':
        form = RollNumberForm(request.POST)
        if form.is_valid():
            try:
                roll_number = form.cleaned_data['roll_number']
                
                # Try to get cached results first
                cache_key = f'student_data_{roll_number}'
                outputs = cache.get(cache_key)
                
                if outputs is None:
                    outputs = run_api_calls(roll_number)
                    # Cache the results for 5 minutes
                    cache.set(cache_key, outputs, 300)
                
                return render(
                    request, 
                    'student_api/api_result.html', 
                    {'json_data': outputs, 'roll_number': roll_number}
                )
            except Exception as e:
                logger.error(f"Error processing request for roll number {roll_number}: {str(e)}")
                return render(
                    request,
                    'student_api/api_form.html',
                    {
                        'form': form,
                        'error': 'An error occurred while processing your request. Please try again.'
                    }
                )
    else:
        form = RollNumberForm()
    
    return render(request, 'student_api/api_form.html', {'form': form})
