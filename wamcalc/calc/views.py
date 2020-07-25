#pylint: disable=no-member
from django.shortcuts import render, get_object_or_404
from .models import Marks
from .forms import EditMarkForm

# Create your views here.

def calc_view(request):
    queryset = Marks.objects.all()
    
    
    def WAM(subjects):
        sub_amt = 0
        summed_marks = 0
        for subject in subjects:
            if subject.code[3] == '1':
                sub_amt += 1
                summed_marks += subject.mark
            else:
                sub_amt += 2
                summed_marks += 2*subject.mark
        return round(summed_marks/sub_amt,3)


    def GPA(subjects):
        GPA_dict = {
        'HD': 4, 
        'D': 3,
        'C': 2,
        'P': 1,
        'F': 0.3
        }
        weighted_sum = 0
        cp_sum = 0
        for subject in subjects:
            weighted_sum += subject.cp * GPA_dict[subject.letter()]
            cp_sum += subject.cp
        return weighted_sum/cp_sum


    def GPA7(subjects):
        GPA_dict = {
        'HD': 4, 
        'D': 3,
        'C': 2,
        'P': 1,
        'F': 0.3
        }
        weighted_sum = 0
        cp_sum = 0
        for subject in subjects:
            weighted_sum += subject.cp * (GPA_dict[subject.letter()]+3)
            cp_sum += subject.cp
        return weighted_sum/cp_sum


    context = {
        'WAM': WAM(queryset),
        'GPA': GPA(queryset),
        'GPA7': GPA7(queryset),
        'subj_list': queryset
    }
    return render(request, 'calc.html', context)


def edit_view(request, my_id):
    obj = get_object_or_404(Marks, id=my_id)
    form = EditMarkForm

    context = {
        'obj': obj,
        'form': form
    }
    return render(request, 'edit.html', context)


def add_view(request):
    return render(request, 'add.html', {})