def cube(x):
  return x*x*x
def my_map(cube_method,argument_list):
  result = list()

  for item in argument_list:
    result.append(cube_method(item))
  return result
my_list = my_map(cube,[1,2,3,4,5,6,7,8])
print(my_list)


print("====")

triangle = lambda m,n : 1/2 * m * n
res=triangle(34,25)
print("Area of the triangle:", res)