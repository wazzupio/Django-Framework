errors_dict = {
    'first_name': 'Имя должно быть больше одного символа.',
    'last_name': 'Фамилия должна быть больше одного символа.',
    'username': 'Имя пользователя должно быть больше одного символа.',
    'email': 'Email должен быть больше одного символа.',
}


def validate_min_length(self):
    errors = ''
    space = ' '

    if len(self.data.get('first_name')) < 2:
        errors += errors_dict['first_name'] + space

    if len(self.data.get('last_name')) < 2:
        errors += errors_dict['last_name'] + space

    if len(self.data.get('username')) < 2:
        errors += errors_dict['username'] + space

    email = self.data.get('email')
    if len(email.split('@')[0]) < 2:
        errors += errors_dict['email']

    return errors
