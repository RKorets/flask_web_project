from wtforms import Form, StringField, FieldList, FormField


class EmailForm(Form):
    email = StringField('email')


class PhoneForm(Form):
    phone = StringField('phone')


class UserForm(Form):
    username = StringField('username')
    address = StringField('address')
    email = FieldList(FormField(EmailForm))
    phone = FieldList(FormField(PhoneForm))





