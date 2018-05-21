import time

# from enum import Enum
#
# class Color(Enum):
#     RED = 1
#     BLUE = 2
#     ORGANAGE = 3
#
# assert Color(1) == Color.RED

import graphene
class Colors(graphene.Enum):
    RED = 1
    BLUE = 2
    ORGANAGE = 3

assert Colors.get(1) ==  Colors.RED

# graphene.Enum.from_enum(Colors, description=lambda value: return "noo" if value == Colors.RED else "nnn")

def haha(root, info):
    print("/"*66)
    return f'{root.first_name} {root.last_name}'

class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String(resolver=haha)



per = Person(first_name="abc", last_name="def", full_name="abc")
print(per.first_name)
print(per.last_name)
print(per.full_name)

class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, info, word):
        return word[:-3]

print(Query(reverse="abcde").reverse)