a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
if a + b > c and a + c > b and b + c > a:
  print("Треугольник существует.")
else:
  print("Треугольник не существует.")
