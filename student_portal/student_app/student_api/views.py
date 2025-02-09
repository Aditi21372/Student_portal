import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from django.core.exceptions import RequestAborted
from .forms import RollNumberForm
from student_app.api_calls.api_utils import run_api_calls

logger = logging.getLogger(__name__)

def handle_broken_pipe(func):
    """Decorator to handle broken pipe errors gracefully"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RequestAborted:
            logger.info("Client closed connection prematurely")
            return JsonResponse({"status": "connection_closed"})
        except BrokenPipeError:
            logger.info("Broken pipe error occurred")
            return JsonResponse({"status": "connection_closed"})
    return wrapper

@require_http_methods(["GET", "POST"])
@handle_broken_pipe
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
