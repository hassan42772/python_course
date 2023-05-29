# dictionary

opposite_meanings={
    "cat":"dog",
    "car":"bike",
    "bike":"cycle",
    "pen":"pencil",
    "men":"women",
}
print(opposite_meanings["car"])
print(opposite_meanings["bike"])
print(opposite_meanings["men"])

# add  a dictionary in it i forgotten to enter it

opposite_meanings["big"]="small"
print(opposite_meanings) 

# getting and element in dictionary

print(opposite_meanings.get("big"))

# update a element in dictionary

opposite_meanings.update({"sir":"madam",})
print(opposite_meanings)

# items function

print(opposite_meanings.items())

# keys function

print(opposite_meanings.keys())

# delete  function

del opposite_meanings["pen"]
print(opposite_meanings)

# copy function

means=opposite_meanings.copy()
del means["pen"]
print(opposite_meanings)
