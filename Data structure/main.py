# tuple

fruits_tuple = ("Apple", "Banana", "Cherry", "Durian", "Grape")
print(type(fruits_tuple))
print(fruits_tuple)

#accessing tuple item
print(fruits_tuple[3]) # output: Durian

# tuple cannot be directly manipulated
# trick: convert it to list object

fruits_list = list(fruits_tuple)
fruits_list.append("Jackfruit")
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# modify item
fruits_list = list(fruits_tuple)
fruits_list[2] = "melon"
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# remove item
fruits_list = list(fruits_tuple)
fruits_list.remove("Jackfruit")
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)