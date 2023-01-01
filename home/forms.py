from django import forms


class ProductForm(forms.Form):
    """ a form for taking product size and send to view for add to cart mission """
    choose_size = forms.CharField(max_length=88, required=True)

