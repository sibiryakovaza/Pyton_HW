# Задание 1 задача №5 
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве 
# (AB = √(xb - xa)2 + (yb - ya)2)
xa = int(input('Введите координаты точки A по оси х:'))
ya = int(input('Введите координаты точки A по оси y:'))
xb = int(input('Введите координаты точки B по оси х:'))
yb = int(input('Введите координаты точки B по оси y:'))
ab= ((xb - xa) **2 + (yb - ya) **2)**(1/2)
ab = round (ab, 2)
print (f"Расстояние межу точками с координатами (",xa,",",ya, ") и (", xb,",", yb,") равно", ab)
