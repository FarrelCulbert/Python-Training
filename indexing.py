#indexing = accessing elements of a sequence using [] (indexing operator)
# [start:end:step]

number = "1234-5678-9876-5432"

# print(number[0])
# print(number[:4]) #[:end]
# print(number[3:8]) # [start:end]
# print(number[5:]) #[start:]
# print(number[-3]) #from back
# print(number[::3])#[::step]

print(f"xxxx-xxxx-xxxx-{number[-4:]}")
print(number[::-1]) #reverse using [::-1]