import templates

nouns=input("enter two nouns (use spaces for seperation): ").split(" ")
adjective=input("input an adjective: ")
verbs=input("enter three verbs (use spaces for seperation): ").split(" ")

print(templates.template1.format(nouns,adjective,verbs))