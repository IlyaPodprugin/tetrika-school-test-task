import wikipediaapi


def print_categorymembers(categorymembers) -> dict:
	letters_counter: dict = {}
	for c in categorymembers.values():
		if c.title[0] >= "\u0410" and c.title[0] <= "\u042F": # Cyrillic script in Unicode: https://en.wikipedia.org/wiki/Cyrillic_script_in_Unicode
			if c.title[0] in letters_counter:
				letters_counter[c.title[0]] += 1
			else:
				letters_counter[c.title[0]] = 1
	return letters_counter


wiki = wikipediaapi.Wikipedia('ru')
page = wiki.page("Категория:Животные_по_алфавиту")
letters_counter: dict = print_categorymembers(page.categorymembers)
for key, value in letters_counter.items():
	print(f"{key}: {value}")
