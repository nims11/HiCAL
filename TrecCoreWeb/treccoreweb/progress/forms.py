from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from treccoreweb.progress.models import CLOSE_LIKERT_SCALE_CHOICES
from treccoreweb.progress.models import DIFF_LIKERT_SCALE_CHOICES
from treccoreweb.progress.models import FAM_LIKERT_SCALE_CHOICES
from treccoreweb.progress.models import FEAT_LIKERT_SCALE_CHOICES
from treccoreweb.progress.models import HELP_LIKERT_SCALE_CHOICES
from treccoreweb.progress.models import INTERFACE_LIKERT_SCALE_CHOICES
from treccoreweb.progress.models import LEFTDOC_SCALE_CHOICES
from treccoreweb.progress.models import Demographic
from treccoreweb.progress.models import ExitTask
from treccoreweb.progress.models import PostTask
from treccoreweb.progress.models import PreTask
from treccoreweb.progress.models import NA


class DemographicForm(forms.ModelForm):
    """
    Form for demographic questionnaire

    """

    class Meta:
        model = Demographic
        exclude = ["username"]
        other_msg = 'If you answered other in the previous question, please specify:'
        labels = {
            'age': 'Your age',
            'student_degree': 'You are:',
            'student_degree_other': other_msg,
            'student_major': 'Your major',
            'student_major_other': other_msg,
            'language': 'How fluent are you in English',
            'search_engine_usage': 'How often do you search the internet for information '
                                   'using a search engine such as Google, Yahoo Search, '
                                   'or Microsoft Bing:',
            'expertise': 'I am an expert at finding information using search engines '
                         'like Google, Yahoo, and Microsoft Bing:',
            'trouble': 'I often have trouble finding what I am looking '
                       'for on the internet:',
            'help': 'Friends and family turn to me to help them search the internet for '
                    'answers to their questions:',
            'enjoyment': 'I enjoy using search engines like '
                         'Google, Yahoo, and Microsoft Bing:',
            'training': 'Have you ever had special training or education in searching '
                        'or information retrieval?',
            'training_feedback': 'If you answered yes to the previous questions, '
                                 'please describe the training or education:',
            'feedback': 'If you have any general feedback about about you that you think '
                        'is necessary or useful for us to know, please describe it below:'
        }

    submit_name = 'submit-demographic-form'

    def __init__(self, *args, **kwargs):
        super(DemographicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Submit(self.submit_name, u'Submit',
                   css_class='btn btn-primary')
        )


class PreTaskForm(forms.ModelForm):
    """
    Form for updating Pretask

    """
    submit_name = 'submit-pretask-form'

    familiarity = forms.CharField(
        widget=forms.Select(choices=FAM_LIKERT_SCALE_CHOICES),
        label=u'How familiar are you with this subject of the above topic?')
    difficulty = forms.CharField(
        widget=forms.Select(choices=DIFF_LIKERT_SCALE_CHOICES),
        label=u'How hard do you think it will be to find relevant documents '
              u'towards this topic?')
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,
                                     'cols': 80}
                              ),
        label=u'Do you have any feedback on this topic?',
        required=False
    )

    class Meta:
        model = PreTask
        fields = ['familiarity', 'difficulty', 'feedback']

    def __init__(self, *args, **kwargs):
        super(PreTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Submit(self.submit_name, u'Submit',
                   css_class='btn btn-primary')
        )


class PostTaskForm(forms.ModelForm):
    """
    Form for updating Posttask

    """
    submit_name = 'submit-posttask-form'
    difficulty = forms.CharField(
        widget=forms.Select(choices=DIFF_LIKERT_SCALE_CHOICES),
        label=u'How easy to use did you find this user interface for its intended '
              u'purpose of helping you find all relevant documents?')
    close = forms.CharField(
        widget=forms.Select(choices=CLOSE_LIKERT_SCALE_CHOICES),
        label=u'How close to finding all relevant documents do you think you came?')
    complete = forms.CharField(
        widget=forms.Select(choices=LEFTDOC_SCALE_CHOICES),
        label=u'How many relevant documents do you think remain to be found?')
    familiarity = forms.CharField(
        widget=forms.Select(choices=FAM_LIKERT_SCALE_CHOICES),
        label=u'How familiar are you with this subject of the above topic '
              u'after completing this task?')

    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,
                                     'cols': 80}
                              ),
        label=u'What, if anything, would you change about this user interface to make it '
              u'easier or more useful for its intended purpose of helping you find all '
              u'relevant documents?',
        required=False
    )

    class Meta:
        model = PostTask
        fields = ['difficulty', 'close', 'complete', 'familiarity', 'feedback']

    def __init__(self, *args, **kwargs):
        super(PostTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Submit(self.submit_name, u'Submit',
                   css_class='btn btn-primary')
        )


class ExitTaskForm(forms.ModelForm):
    """
    Form for creating exit questionnaire

    """
    submit_name = 'submit-exit-form'
    difficulty = forms.CharField(
        widget=forms.Select(choices=INTERFACE_LIKERT_SCALE_CHOICES),
        label=u'Please rate the 5 user interfaces from most to least useful for '
              u'their intended purpose of helping you find all relevant documents?')


    keyword_search_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'The judging system was composed of many different features. For each'
              u'of these features, how useful was it for its intended purpose of '
              u'helping you find all relevant documents?\n'
              u'Feature: Keyword search within a document or paragraph.')

    keyword_shortcut_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'Feature: Keyboard shortcuts for submitting relevance judgments.')


    doc_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'Feature: Ability to use a search engine to find documents in addition to the learning interface.')

    topic_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'Feature: Display of topic statement of what is considered relevant.')

    recent_doc_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'Feature: Ability to review recent judgments and change judgment.')

    full_doc_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'Feature: Ability to view a full document rather than merely a paragraph summary.')


    quote_helpful = forms.CharField(
        widget=forms.Select(choices=HELP_LIKERT_SCALE_CHOICES),
        label=u'Feature: For the search engine, the ability to specify phrases (&quot;new york&quot;) or require words (+france).')


    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,
                                     'cols': 80}
                              ),
        label=u'Is there anything else you would like to add about the user interfaces, '
              u'the topics, or this study?',
        required=False
    )

    class Meta:
        model = ExitTask
        exclude = ['username']

    def __init__(self, *args, **kwargs):
        super(ExitTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Submit(self.submit_name, u'Submit',
                   css_class='btn btn-primary')
        )
