import time
import numpy as np

SIZE = 10_000_000

# --------------------------
# Python List Performance
# --------------------------
python_list = list(range(SIZE))

start = time.perf_counter()

result_list = []
for num in python_list:
    result_list.append(num * 2)

end = time.perf_counter()

list_time = end - start

print("Python List Time :", round(list_time, 4), "seconds")

# --------------------------
# NumPy Performance
# --------------------------
numpy_array = np.arange(SIZE)

start = time.perf_counter()

result_array = numpy_array * 2

end = time.perf_counter()

numpy_time = end - start

print("NumPy Time       :", round(numpy_time, 4), "seconds")

# --------------------------
# Comparison
# --------------------------
print("\nPerformance Summary")
print("-" * 35)
print(f"List Time  : {list_time:.4f} sec")
print(f"NumPy Time : {numpy_time:.4f} sec")

if numpy_time > 0:
    print(f"NumPy is approximately {list_time / numpy_time:.2f}x faster.")