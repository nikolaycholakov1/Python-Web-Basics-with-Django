from django import forms

from Exam_30_October_2022.car.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'imageUrl': 'Image URL'
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
