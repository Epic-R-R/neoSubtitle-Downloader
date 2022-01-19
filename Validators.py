from PyInquirer import ValidationError, Validator
import re

# create class for check Empty Field in input
class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank", cursor_position=len(value.text)
            )


# create class for check email valid
class EmailValidator(Validator):
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"

    def validate(self, email):
        if len(email.text):
            if re.match(self.pattern, email.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid email", cursor_position=len(email.text)
                )
        else:
            raise ValidationError(
                message="You can't leave this blank", cursor_position=len(email.text)
            )


# Create Class for check valid password
class ValidatePassword(Validator):
    def validate(self, password):
        flag = 0
        while True:
            if len(password.text) < 8:
                flag = -1
                break
            elif not re.search("[a-z]", password.text):
                flag = -1
                break
            elif not re.search("[A-Z]", password.text):
                flag = -1
                break
            elif not re.search("[0-9]", password.text):
                flag = -1
                break
            elif not re.search("[_@$]", password.text):
                flag = -1
                break
            elif re.search("\s", password.text):
                flag = -1
                break
            else:
                flag = 0
                return True
        if flag == -1:
            raise ValidationError(
                message="Your password must: Be a minimum of 8 or more characters, and include uppercase, lowercase, numbers, non-alphanumeric symbols",
                cursor_position=len(password.text),
            )
        else:
            raise ValidationError(
                message="You can't leave this blank", cursor_position=len(password.text)
            )
