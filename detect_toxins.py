# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

ingredients = ['sodium benzoate']

def is_toxin(ingredients):
    if 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients\
    or 'sodium oxide' in ingredients:
        return True
    else:
        return False


if is_toxin(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
