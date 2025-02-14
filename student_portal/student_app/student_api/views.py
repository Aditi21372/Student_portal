import logging
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from .forms import RollNumberForm
from student_app.api_calls.api_utils import run_api_calls

logger = logging.getLogger(__name__)

@require_http_methods(["GET", "POST"])
def api_view(request):
    if request.method == 'POST':
        form = RollNumberForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            try:
                api_data = run_api_calls(roll_number)
                
                # Handle API response (success or fallback)
                context = {
                'data': api_data,
                'branch': api_data['student_data'].get('branch', 'Unknown'),
                'ssh_requirements': api_data.get('ssh_courses', []),
                'discipline_requirements': api_data.get('discipline_courses', []),
                'csai_courses': api_data.get('csai_courses', {}),
                'eco_major': api_data.get('eco_major', {}),
                'btp_credits': api_data.get('btp_credits', {}),
                'ip_credits': api_data.get('ip_credits', {}),
                'online_courses': api_data.get('online_courses', {}),
                'two_xx_courses': api_data.get('two_xx_courses', {})
                }
                
                # Add error information if present
                if 'error' in api_data.get('student_data', {}):
                    context['error'] = api_data['student_data']['error']
                    context['details'] = api_data['student_data'].get('details', '')
                
                return render(request, 'student_api/api_result.html', context)
            except Exception as e:
                logger.error(f"API call failed: {str(e)}")
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        form = RollNumberForm()
        return render(request, 'student_api/api_form.html', {'form': form})
