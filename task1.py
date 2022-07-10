from typing import Union


# Можно было бы использовать .find(), но он работает только со строками.
# В условии задачи сказано, что на вход подаётся массив чисел, 
# но в примере передаётся строка, поэтому я использую .index()
# для работы как со списками, так и со строками.
# Сложность метода .index() O(n)
def task(array: Union[list, str]) -> Union[int, None]:
	try:
		return array.index("0")
	except ValueError:
		return None


# Если в этом задании планировалось проверить знание алгоритмов,
# то вот реализация с использованием бинарного поиска.
# На вход так же принимается как список, так и строка.
# При этом список может состоять как из чисел, так и из строк.
# Сложность O(log n)
def task_binary_search(array: Union[list, str]) -> Union[int, None]:
	start: int = 0
	end: int = len(array) - 1

	while start <= end:
		mid: int = (start + end) // 2
		guess: str = str(array[mid])
		if guess == "0":
			if str(array[mid - 1]) == "1" or mid == 0:
				return mid
			end = mid - 1
		elif guess == "1":
			start = mid + 1
		else:
			return None
	return None
		

print("Test built-in function")
print(task("111111111110000000000000000"))
print(task(list("111111111110000000000000000")))
print(task([0, 0, 0]))
print(task([1, 0, 0]))
print(task([1, 1, 0]))
print(task([1, 1, 1]))
print(task([1, 0, 1]))
print(task([]))

print("\nTest binary search function")
print(task_binary_search("111111111110000000000000000"))
print(task_binary_search(list("111111111110000000000000000")))
print(task_binary_search([0, 0, 0]))
print(task_binary_search([1, 0, 0]))
print(task_binary_search([1, 1, 0]))
print(task_binary_search([1, 1, 1]))
print(task_binary_search([1, 0, 1]))
print(task_binary_search([]))
