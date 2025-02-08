from django.shortcuts import render
from django.http import JsonResponse
from .forms import RollNumberForm
from student_app.api_calls.api_handler import APIHandler  # Updated import statement

def api_view(request):
    if request.method == 'POST':
        form = RollNumberForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            api_handler = APIHandler("http://localhost:3002/api")
            
            # Call the APIs using the roll number
            outputs = {
                "graduation_check": api_handler.call_graduation_check_api(),
                "bucket": api_handler.call_bucket_api(),
                "mandatory": api_handler.call_mandatory_api(),
                "ssh_major": api_handler.call_ssh_major_api(),
                "cw": api_handler.call_cw_api(),
                "sg": api_handler.call_sg_api(),
                "thirty_two_credits": api_handler.call_thirty_two_credits_api(),
                "ip": api_handler.call_ip_api(),
                "online_courses": api_handler.call_online_courses_api(),
                "two_x_courses": api_handler.call_two_x_courses_api(),
                "btp": api_handler.call_btp_api(),
                "honors": api_handler.call_honors_api(),
                "minors": api_handler.call_minors_api(),
                "eco_major_core": api_handler.call_eco_major_core_api(),
                "incomplete_grade": api_handler.call_incomplete_grade_api(),
                "required_credits": api_handler.call_required_credits_api(),
                "eco_major_elective": api_handler.call_eco_major_elective_api(),
            }
            return render(request, 'student_api/api_result.html', {'json_data': outputs})  # Render the result template
    else:
        form = RollNumberForm()
    
    return render(request, 'student_api/api_form.html', {'form': form})
