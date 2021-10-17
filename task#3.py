import os


def create_file(catalog_name):
	file_list = os.listdir(catalog_name)
	total_list = []
	for fl in file_list:
		with open(catalog_name + '/' + fl, encoding = 'utf-8') as file:
			file_lines = file.readlines()
			total_list.append([fl, len(file_lines), file_lines])
	with open(catalog_name + '/result.txt', 'w', encoding = 'utf-8') as result_file:
		for elem in total_list:
			result_file.write(f'{elem[0]}\n')
			result_file.write(f'{elem[1]}\n')
			for line in elem[2]:
				result_file.write(f"{line.strip()}\n")

create_file('files')