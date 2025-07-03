import string

all_letters = string.ascii_letters
input_str = input("Введите две буквы через дефис (например, a-c или s-H): ")
start, end = input_str.split('-')
start_index = all_letters.index(start)
end_index = all_letters.index(end)
print(all_letters[start_index:end_index + 1])
