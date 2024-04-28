from django.shortcuts import render
from django.http import HttpResponse
studentData = [
            {'id':'1' , 'studentName': 'Bakhshullah wahid' , 'department': 'computer science'},
            {'id':'2' , 'studentName': 'wahid' , 'department': 'science'},
            {'id':'3' , 'studentName': 'abid' , 'department': 'education'},]
# Create your views here.
def transfer_data(request):
    
    return render(request , 'index.html' , {'context':studentData})
def index2_view(request):
    student_id = request.GET.get('id', '')
    student_name = request.GET.get('name', '')
    student_department = request.GET.get('department', '')
    
    # Process the selected student data (e.g., fetch additional details from database)
    return render(request, 'index2.html', {'id': student_id, 'name': student_name, 'department': student_department})