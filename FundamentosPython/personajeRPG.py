full_dot = '●'
empty_dot = '○'

def create_character(name,fuerza, inteligencia, carisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if len(name)==0:
        return "The character should have a name"
    if len(name)>10:
        return "The caracter name is too long"
    if name.isspace():
        return "The character name should not contain spaces"