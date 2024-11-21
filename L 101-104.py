#the author's name is: Serenity
#my partner (Olivia) left the lab without saying anything to me; we only kind of worked on the first problem together 

#L101
s = {"winter":24, "sapphire":2, "rose":2, "raven":1, "love":"infinite"}

def my_get_function(x):
    if x in s:
        print(s[x])
    else:
        print("DNE")

#test
my_get_function("love")
my_get_function("men")


#L102
#the T.A. and class was uncertain what exactly was being asked here: this is my best attempt
cpsc_dict = {"Schuler":"Serenity", "Taylor":"Rylee", "Raycroft":"Anna", "Gangwer":"Gwyneth", "Hand":"Colleen", "DeYoung":"Lily", "Weber-Hess":"Mairi", "Laneman":"Margaret", "Beck":"Olivia", "Wyatt":"Elizabeth", "Garcia Jimenez":"Victoria", "Litvak":"Aliza"}

def my_histogram(my_dict):
    d = dict()
    for key in my_dict:
        if my_dict[key] not in d:
            d[my_dict[key]] = 1
        else:
            d[my_dict[key]] += 1
    return d

def new_d(d):
    histogram = my_histogram(d)
    empty_d = {}
    for name in histogram:
        val = histogram[name]
        if val not in empty_d:
            empty_d[val] = [name]
        else:
            empty_d[val].append(name)
    return empty_d
        
#test
print(new_d(cpsc_dict))


#L103
cpsc_names = ["Serenity", "Schuler", "Rylee", "Taylor", "Anna", "Raycroft", "Gwyneth", "Gangwer", "Colleen", "Hand", "Lily", "DeYoung", "Mairi", "Weber-Hess", "Margaret", "Laneman", "Olivia", "Beck", "Elizabeth", "Wyatt", "Victoria", "Garcia Jimenez", "Aliza", "Litvak"]
last_names = cpsc_names[1::2]
first_lett = dict()
for x in last_names:
    if x[0] not in first_lett:
        first_lett[x[0]] = 1
    else:
        first_lett[x[0]] += 1
once = []
twice = []
for key in first_lett:
    if first_lett[key] == 1:
        once.append(key)
    else:
        twice.append(key)
first_lett_2 = {1:once, 2:twice}

#test
print(first_lett_2)


#L104
red_cake = {"flour":3, "baking soda":1, "cocoa powder":2, "salt":0.5, "butter":0.5, "sugar":2, "oil":1, "eggs":4}
lem_cake = {"flour":1.5, "baking soda":2, "salt":0.5, "butter":0.5, "sugar":1,"eggs":2, "milk":0.5, "lemons":2}

same_ingredients = []
for x in red_cake:
    if x in lem_cake:
        same_ingredients.append(x)

#test
print(same_ingredients)
