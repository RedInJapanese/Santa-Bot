import random

def handle_response(message):
    asdf = message.lower();

    if(message == 'reminder'):
        return "@here Just a reminder that the deadline for secret santa is December 30th! Don't late, or I'll have sex with your mother!"
    else:
        return "@here Everyone has been sent their respective secret santa assignments. If there is a mistake or you didn't get your assignment for whatever reason, please DM Akash."
