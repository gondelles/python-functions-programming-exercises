# Your code goes here:
def render_person(name,birth_date,eye_color,age,genero):
    return str(name) + " is a " + str(age) + " years old " + str(genero) + " born in " + str(birth_date) + " with " + str(eye_color) + " eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))