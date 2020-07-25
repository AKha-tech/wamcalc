a_res = [('ENG1005',97), ('FIT1045',45), ('ETC2430',75)]
# WAM = 73

def WamCalc(res):
    s = 0
    n = 0
    for subj in res:
        n += int(subj[0][3])
        if subj[0][3] == '1':
            s += subj[1]
        else:
            s += 2* subj[1]
    return s/n

#print(WamCalc(a_res))

class Marks:
    def __init__(self, code, name, mark, cp):
        self.code = code
        self.name = name
        self.mark = mark
        self.cp = cp

    def passed(self):
        if self.mark >= 50:
            return True
        return False

    def letter(self):
        if 80 <= self.mark <= 100:
            return 'HD'
        
        elif 70 <= self.mark < 80:
            return 'D'

        elif 60 <= self.mark < 70:
            return 'C'

        elif 50 <= self.mark < 60:
            return 'P'
        
        else:
            return 'F'

GPA_dict = {
    'HD': 4, 
    'D': 3,
    'C': 2,
    'P': 1,
    'F': 0.3
}


ayden_scores = [
    Marks('BFC2140', 'CorpFi', 83, 6), 
    Marks('ECC1100', 'MacroEco', 72, 6),
    Marks('ETC1000', 'Bus. Stats', 73, 6),
    Marks('MGC1010', 'Management', 67, 6),
    Marks('ACC1100', 'Fin. Accounting', 78, 6),
    Marks('BTC1100', 'Comm. Law', 81, 6),
    Marks('ECC100', 'MicroEco', 77, 6),
    Marks('MKC1200', 'Marketing', 81, 6)
    ]


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
    global GPA_dict
    weighted_sum = 0
    cp_sum = 0
    for subject in subjects:
        weighted_sum += subject.cp * GPA_dict[subject.letter()]
        cp_sum += subject.cp
    return weighted_sum/cp_sum


def GPA7(subjects):
    global GPA_dict
    weighted_sum = 0
    cp_sum = 0
    for subject in subjects:
        weighted_sum += subject.cp * (GPA_dict[subject.letter()]+3)
        cp_sum += subject.cp
    return weighted_sum/cp_sum

def results(subjects):
    return f'WAM = {WAM(subjects)} || GPA = {GPA(subjects)} || 7-Pt-GPA = {GPA7(subjects)}'


print(results(ayden_scores))