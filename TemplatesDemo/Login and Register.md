# Login and Register

    


    * we have to add validation for field email to make it requierd field
        def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email