_________________________________
1. Views with one template function
_______________________________
    def persist_pet(request,OBJECT,template_name):
        form = OBJECTForm(instance=OBJECT)
        if request.method == "POST":
            form = OBJECTForm(request.POST,instance=OBJECT)
    
            if form.is_valid():
                form.save()
                return redirect('pet details or comment', OBJECT.pk)
            
        context = {
            'form': form,
            'OBJECT': OBJECT,
        }
        return render(request, f'{template_name}.html', context)


    def edit_pet(request, pk):
        OBJECT = OBJECT.objects.get(pk=pk)
        return persist_pet(request, OBJECT, 'OBJECT_edit')


    def create_pet(request):
        OBJECT = OBJECT()
        return persist_pet(request, OBJECT, 'OBJECT_create')
_______________
2. DELETE example
______________
    def delete_pet(request, pk):
        OBJECT = OBJECT.objects.get(pk=pk)
        if request.method == 'GET':
            context = {
                'OBJECT': OBJECT,
            }
            return render(request, 'OBJECT_delete.html', context)
        else:
            OBJECT.delete()
            return redirect('list OBJECT')

_____________________________________________
3. MIXIN add class to all fields:
_______ _____________ ____________ _________

    class BootstrapFormMixin:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._init_bootstarp_fields()
    
        def _init_bootstarp_fields(self):
            for (_,field) in self.fields.items():
                if 'class' not in field.widget.attrs:
                    field.widget.attrs['class'] = ''
                field.widget.attrs['class'] += ' form-control'


_________________________________________________

4. VALIDATION- number bigger than 0 + class to all fields example Using clean_
________________________________________________________
    class BookModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.add_form_control_class_to_all()
    
        def add_form_control_class_to_all(self):
            for (_, field) in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
    
        def clean_pages(self):
            pages = self.cleaned_data['pages']
            if pages <= 0:
                raise ValidationError(f'Pages must be grater then 1')
            return pages
    
        class Meta:
            model = BookModel
            fields = '__all__'
_________________________________________________________________

5. FORMS with choice:
__________________________________________________

    class Pet(models.Model):

        DOG = 'dog'
        CAT = 'cat'
        PARROT = 'parrot'
        UNKNOWN = 'unknown'
    
    
        PET_TYPES = (
            (DOG, 'Dog'),
            (CAT, 'Cat'),
            (PARROT, 'Parrot'),
            (UNKNOWN, 'Unknown'),
        )
    
    
    
        type = models.CharField(max_length=7, choices=PET_TYPES)

_____________________________________________________________________________
6. Calculating something using set:
______________________________________
    pet.likes_count = pet.like_set.count()

_____________________________________________
7. Disable field with widgets
________________________________
    class EditPetForm(PetForm):
        class Meta:
            model = Pet
            fields = '__all__'
            widgets = {
                'type': forms.TextInput(
                    attrs={
                        'readonly': 'disabled',
                    }
                )
            }
________________________________
8. Validators example:
________________________
    def validate_name(value):

    if value[0] != value[0].upper():
        raise ValidationError('The name must start with an uppercase letter')


    def validate_age(value):
    if value <= 0:
        raise ValidationError('The age cannot be less than zero')


    def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Enter a valid password')
    if any([not x.isalnum() for x in value]):
        raise ValidationError('Enter a valid password')


    class UserForm(forms.Form):
    name = forms.CharField(
        validators=[
            MinLengthValidator(6),
            validate_name
        ]
    )
___________________________________________
9. another example for disabled
__________________________________________________   
    class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for(_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'