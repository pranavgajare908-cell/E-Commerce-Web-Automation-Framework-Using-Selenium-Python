import random


class random_email_generator:
    @staticmethod
    def generate_Email():
        chars = "asdfghjklzxcvbnmqwertyuiop0123456789!"
        email = "".join(random.choice(chars) for i in range(10))
        return email + "@gmail.com"
