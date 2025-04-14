import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(number_array, direction = "ascending"):
    """
    :param list number_array: list with numeric array
    :param str direction: string indicating sorting direction: ascending, descending
    :return:
    """
    n = len(number_array)
    for i in range(n):
        min_max_i = i
        for num_idx in range(i+1, n):
            if direction == "ascending":
                if number_array[num_idx] < number_array[min_max_i]:
                    min_max_i = num_idx
            elif direction == "descending":
                if number_array[num_idx] > number_array[min_max_i]:
                    min_max_i = num_idx
        number_array[i], number_array[min_max_i] = number_array[min_max_i], number_array[i]
    return  number_array

def bubble_sort(number_array):
    """
    :param list number_array: list with numeric array
    :return: sorted numeric array
    """
    n = len(number_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if number_array[j] > number_array[j + 1]:
                number_array[j],number_array[j + 1] = number_array[j + 1], number_array[j]
            else:
                continue
    return number_array

def insertion_sort(number_array):
    """
    :param list number_array: list with numeric array
    :return: sorted numeric array
    """
    n = len(number_array)
    for i in range(1,n):
        key = number_array[i]
        j = i - 1
        while j >= 0 and number_array[j] > key:
            number_array[j+1] = number_array[j]
            j = j - 1
        number_array[j + 1] = key
    return number_array

def main():
    data = read_data("numbers.csv")
    print(data)

    number_array = ([3, 6, 4, 1, 5, 8, 2])
    number_array = selection_sort(number_array)
    print(number_array)
    print(bubble_sort(number_array))
    print(insertion_sort(number_array))
    pass


if __name__ == '__main__':
    main()
