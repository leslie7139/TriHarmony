from django import forms
from .models import Behavior, Child, BehaviorCheckIn, Feeling


class FeelingForm(forms.ModelForm):
    feeling = forms.ChoiceField(
        choices=Feeling.FEELINGS_CHOICES, widget=forms.RadioSelect(), required=True)
    note = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Feeling
        fields = ['feeling', 'note']

    def clean(self):
        cleaned_data = super().clean()
        feeling = cleaned_data.get('feeling')

        if not feeling:
            raise forms.ValidationError('Please select a feeling!')

        return cleaned_data


class BehaviorForm(forms.ModelForm):
    FREQUENCY_CHOICES = [
        ('0', '(0) nonexistant'),
        ('1', '(1) virtually nonexistent (less than once a month, not worrisome)'),
        ('2', '(2) upper limit of normal/tolerable for a child of same approximate age'),
        ('3', '(3) a few times in the past week and almost every week in the past month'),
        ('4', '(4) a few times in the past week and EVERY single week in the past month'),
        ('5', '(5) many times in the past week and almost every week in the past month'),
        ('6', '(6) many times in the past week and EVERY single week in the past month'),
        ('7', '(7) several times per day (with breaks in-between incidents), almost every day'),
        ('8', '(8) several times per day (with breaks in-between incidents, EVERY single day'),
        ('9', '(9) constantly (it never stops, or stops briefly before restarting) almost every day'),
        ('10', '(10) constantly (it never stops, or stops briefly before restarting) EVERY single day')

    ]
    INTENSITY_CHOICES = [
        ('0', '(0) Behavior isn’t worrisome. There are no negative consequences imaginable'),
        ('1', '(1) Behavior is not worrisome. There are almost no negative consequences imaginable'),
        ('2', '(2) Upper limit of tolerable for a child of the same approximate age. Behavior is manageable, but frustrating'),
        ('3', '(3) Behavior is severe enough to worry you almost every time'),
        ('4', '(4) Behavior is severe enough to worry you EVERY single time'),
        ('5', '(5) Behavior is very serious almost every time'),
        ('6', '(6) Behavior is very serious EVERY single time and is hurting the child or others when it happens'),
        ('7', '(7) Behavior is alarmingly serious almost every time'),
        ('8', '(8) Behavior is alarmingly serious EVERY time and there are more "bad days" than "good days" overall.'),
        ('9', '(9) This behavior is or was potentially life-threatening'),
        ('10', '(10) A successful or thwarted suicidal or homicidal act has occurred, OR child was in some other life-threatening situation')

    ]

    class Meta:
        model = BehaviorCheckIn
        fields = ['behavior', 'behavior_intensity', 'behavior_frequency', 'note']
    behavior = forms.ModelChoiceField(queryset=Behavior.objects.all())
    behavior_intensity = forms.ChoiceField(choices=INTENSITY_CHOICES)
    behavior_frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)
    note = forms.CharField(widget=forms.Textarea, required=False)


# ModelForm class - should auto generate fields for each field in model, will handle input validation and error handling.

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age', 'dob', 'gender', 'specialist']


class SpecialistBehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = ['behavior', 'behavior_details', 'notes']


