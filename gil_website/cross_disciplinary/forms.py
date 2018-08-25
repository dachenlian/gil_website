from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F')
    )
    student_id = forms.CharField(max_length=100, label="學號")
    eng_name = forms.CharField(max_length=100, label="英文姓名")
    zh_name = forms.CharField(max_length=100, label="中文姓名")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="生理性別")
    college = forms.CharField(max_length=100, label="學院", help_text="文學院")
    department = forms.CharField(max_length=100, label="學院", help_text="文學院")
    reason = forms.CharField(widget=forms.Textarea, label="申請原因")
    primary_email = forms.EmailField(label="常用電子信箱")
    personal_page = forms.URLField(required=False, label="個人首頁網址")
    address = forms.CharField(max_length=100, required=False, label="聯絡地址")
    profile_picture = forms.ImageField(required=False, label="上傳照片")
    more_info = forms.CharField(widget=forms.Textarea, label="更多個人資訊", required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'student_id', 'eng_name', 'zh_name', 'gender', 'college',
                  'department', 'reason', 'primary_email', 'personal_page', 'address', 'profile_picture', 'more_info']
