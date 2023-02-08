from time import perf_counter
from random import randrange, shuffle


def isSorted(mylist):
  for i in range(len(mylist)-1):
    if mylist[i] > mylist[i+1]:
      return False
  return True
  
def swap(mylist, i, j):
  temp = mylist[j]
  mylist[j] = mylist[i]
  mylist[i] = temp
  
def bubble_sort(mylist):
  while not isSorted(mylist):
    for i in range(len(mylist)-1):
      if mylist[i] > mylist[i + 1]:
        swap(mylist, i, i + 1)

def insertion_sort(mylist):
  if len(mylist) <= 1:
    return mylist
  else:
    for i in range(len(mylist)-1):
      j = i+1
      while j > 0 and mylist[j] < mylist[j-1]:
        swap(mylist, j, j-1)
        j -= 1
        
def merge(A, B):
  C = []
  while len(A) > 0 and len(B) > 0:
    if A[0] >= B[0]:
      C.append(B[0])
      del B[0]

    elif B[0] > A[0]:
      C.append(A[0])
      del A[0]

  if len(A) == 0:
    C += B
    
  if len(B) == 0:
    C += A
    

  return C

def merge_sort(mylist):
  if len(mylist) == 1:
    return mylist
  
  x = len(mylist)
  A = mylist[:x//2]
  B = mylist[x//2:]
  
  sorted_list = merge(merge_sort(A), merge_sort(B))
  return sorted_list
      
def scramble(mylist, n):
  list_len = len(mylist)
  for i in range(n):
    j = randrange(list_len)
    k = randrange(list_len)
    swap(mylist, k, j)
        
def test_rand(sort_func):
  sort_times = []
  iter = 10000
  for i in range(50, iter + 1):
    mylist = list(range(i))
    shuffle(mylist)
    sort_times.append(time_exec(bubble_sort))
  return sort_times

def time_exec(num_iters, func, *args, **kwargs):
  sort_times = []
  results = None
  for _ in range(num_iters):
    start_time = perf_counter()
    results = func(*args, **kwargs)
    end_time = perf_counter()
    sort_times.append(end_time - start_time)
  return sum(sort_times)/num_iters, results

def test_algorithm(sort_func, out_file_name, n_trials=5, n_scramble=5, start=20, stop=5001, skip=20):
  with open(out_file_name, 'w') as f:
    f.write('list_length,randomized,reversed, shuffle\n')
    for list_length in range(start, stop, skip):
      print(f'Testing list of length {list_length}')

      randomized_list = list(range(list_length))
      shuffle(randomized_list)
      randomized_time, _ = time_exec(n_trials, sort_func, randomized_list)

      reversed_list = list(range(list_length))
      reversed_list.reverse()
      reversed_time, _ = time_exec(n_trials, sort_func, reversed_list)

      scrambled_list = list(range(list_length))
      scramble(scrambled_list, n_scramble)
      scrambeled_time, _ = time_exec(n_trials, sort_func, scrambled_list)

      out_string = f"{list_length}, {randomized_time}, {reversed_time}, {scrambeled_time}\n"
      f.write(out_string)
      
      
def main():
 test_algorithm(merge_sort, ".merge_sort_test.csv")

if __name__ == '__main__':
  main()