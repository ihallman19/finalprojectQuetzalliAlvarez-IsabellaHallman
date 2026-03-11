from menuDef import MenuItem

#gives you meals that are below or equal to a certain amount of calories you want to eat
def healthy(menu:list[MenuItem], cal:int)->list[MenuItem]:
    health = []
    for i in menu:
        if i.calories != 0:
            if i.calories <= cal:
                health.append(i.name)
    return health

#gives you meals at a certain location that are below or equal to a certain amount of calories you want to eat
def restaurant(menu:list[MenuItem], location:str, cal:int)->list[MenuItem]:
    health = []
    for i in menu:
        if i.location == location:
            if i.calories <= cal and i.calories != 0:
                health.append(i.name)
    return health

#gives you meals at a certain location that are vegan
def vegan(menu:list[MenuItem], locate:str)->list[MenuItem]:
    loc = []
    for i in menu:
        if i.location == locate:
            if i.vegan:
                loc.append(i.name)
    return loc

#detects if there's missing calorie information
def missing_cals(menu:list[MenuItem])->list[MenuItem]:
    missing = []
    for i in menu:
        if i.calories == 0:
            missing.append(i.name)
    return missing

#gives you meals that are vegetarian
def vegetarian(menu:list[MenuItem])->list[MenuItem]:
    vegetarian_ = []
    for i in menu:
        if i.vegetarian:
            vegetarian_.append(i.name)
    return vegetarian_

#gives you meals that are gluten-free
def gluten_free(menu:list[MenuItem])->list[MenuItem]:
    gluten_free_ = []
    for i in menu:
        if i.vegetarian:
            gluten_free_.append(i.name)
    return gluten_free_

#gives you the location with the healthiest meals
def healthy_location(menu:list[MenuItem])->dict:
    d = {}
    for i in menu:
        if i.location not in d:
            d[i.location] = 0

    for j in d:
        for i in menu:
            if i.location == j:
                d[j] += i.calories

    return d