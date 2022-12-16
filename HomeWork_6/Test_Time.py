from timeit import timeit
# после изменений
print(timeit("append_ratting()", setup="from Task_2_5 import append_ratting", number=1000))
print(timeit("sort_array(arr)", setup="from Task_2_2 import sort_array, arr", number=1000))
