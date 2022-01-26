from django import forms


class StudentForm(forms.Form):

    full_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Full Name',
                'required': '',
                'class': 'input',
            }
        )
    )

    student_id = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Student Id',
                'required': '',
                'class': 'input',
            }
        )
    )

    sex = forms.CharField(
        max_length=6,
        widget=forms.Select(
            choices=[('', 'Select Sex...'), ('M', 'Male'), ('F', 'Female')],
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    department = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Department',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        full_name = cleaned_data.get('full_name')
        student_id = cleaned_data.get('student_id')
        sex = cleaned_data.get('sex')
        department = cleaned_data.get('department')

        if not student_id or not full_name or not sex or not department:
            raise forms.ValidationError('Field cannot be empty')


class FoodForm(forms.Form):
    food_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Food Name',
                'required': '',
                'class': 'input',
            }
        )
    )

    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(FoodForm, self).clean()
        food_name = cleaned_data.get('food_name')
        stock = cleaned_data.get('stock')

        if not food_name or not stock:
            raise forms.ValidationError('Field cannot be empty')


class OrderForm(forms.Form):
    ticket_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    student_id = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Student Id',
                'required': '',
                'class': 'input',
            }
        )
    )

    food_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Food Name',
                'required': '',
                'class': 'input',
            }
        )
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        ticket_id = cleaned_data.get('ticket_id')
        student_id = cleaned_data.get('student_id')
        food_name = cleaned_data.get('food_name')
        quantity = cleaned_data.get('quantity')

        if not ticket_id or not student_id or not food_name or not quantity:
            raise forms.ValidationError('Field cannot be empty')


class ValidateTicketForm(forms.Form):
    ticket_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    student_id = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Student Id',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(ValidateTicketForm, self).clean()
        ticket_id = cleaned_data.get('ticket_id')
        student_id = cleaned_data.get('student_id')

        if not ticket_id or not student_id:
            raise forms.ValidationError('Field cannot be empty')


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Username',
                'required': '',
                'class': 'input',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username or not password:
            raise forms.ValidationError('field cannot be empty')
