from django import forms
import itertools

CHOICES=[('select1','select 1'),
    ('select2','select 2')]

DAYSOFWEEK = (
        ('monday', 'Monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday')
        )



class NameForm(forms.Form):
    iterator = itertools.count()
    num_staff = 5
    num_duties = forms.IntegerField(required=False, widget=forms.HiddenInput(), initial=10)
    #day_select = [None, None]
    #your_name = forms.CharField(label='Your name', max_length=100)
    #their_name = forms.CharField(label='Their name', max_length=100)
    #like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    #day_select[1] = forms.MultipleChoiceField(label='select 1', required=True,
            #widget=forms.CheckboxSelectMultiple,
            #choices=DAYSOFWEEK)

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        for i in range(self.num_staff):
            self.fields['day_select_{index}'.format(index=i)] =\
                    forms.MultipleChoiceField(required=True,
                    widget=forms.CheckboxSelectMultiple,
                    choices=DAYSOFWEEK)

        dutychoices = [(x, x) for x in range(1,6)]
        dutychoices.append((1000, 1000))
        for i in range(self.num_staff):
            for j in range(self.fields['num_duties'].initial):
                self.fields['duty_select_{staff}_{duty}'.format(staff=i, duty=j)] =\
                        forms.ChoiceField(choices=dutychoices, required=True)
