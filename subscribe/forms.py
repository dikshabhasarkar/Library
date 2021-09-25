from django import forms

class Subscribe(forms.Form):
    email = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # name = forms.CharField(max_length=100)
    # age = forms.IntegerField()
#output
# <tr><th><label for="id_email">Email:</label></th><td><input type="email" name="email" required id="id_email"></td></tr> 
# <tr><th><label for="id_email">Email:</label></th><td><input type="email" name="email" required id="id_email"></td></tr>
# <tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" maxlength="100" required id="id_name"></td></tr>    
# # <tr><th><label for="id_age">Age:</label></th><td><input type="number" name="age" required id="id_age"></td></tr>