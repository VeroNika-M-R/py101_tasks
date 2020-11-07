"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

coefficient_message = "You get {} points from 3 for your password"
validated_password = "Hey, you have really cool password. I will send it to my sniffer, okay? :D (Сложный пароль)"
bad_password = "Your password isn't hard. It can be easily bruteforced (Простой пароль)"

errors = {
    'no-password': 'You didn\'t enter the password. Repeat again',
    'little-length': 'The password is short. Try to make it longer',
    'much/less-numbers': 'Not enough or too much numbers',
    'need-special': 'Your password doesn\'t have any special characters. It\'s not cool!'
}

passed = False
def password_validate(password):
    global passed
    coefficient = 0
    # Does it exist?
    if password: 
        # How long is it?
        if len(password) >= 8:
            coefficient += 1
            count = 0 
            for char in password:
                if char.isnumeric():
                    count += 1
            percentage = count * 100 // len(password)
            # Does it have any numbers?
            if percentage >= 10 and percentage <= 90:
                coefficient += 1
                special, count = '!@#$%^&*()_+=-~', 0
                for char in password:
                    if char in special:
                        count += 1
                percentage = count * 100 // len(password)
                # Does it have any special characters?
                if percentage >= 2 and percentage <= 100:
                    coefficient += 1
                    passed = True
                    print(validated_password)
                else: print(errors['need-special'])
            else: print(errors['much/less-numbers'])
        else: print(errors['little-length']) 
    else: print(errors['no-password'])
    print(coefficient_message.format(coefficient))
    if not passed:
        print(bad_password)

while not passed:
    password = input("Enter your password here: ")
    password_validate(password)
    del password