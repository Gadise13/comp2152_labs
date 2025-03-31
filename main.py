# import mammal
from mammal import Mammal
from person import Person
from tick import Tick
from puma import Puma

m = Mammal(10)
m.speak()  # Call the speak method
print(m)

p = Person(name="John Doe", age=20, height=6)
p.speak()
print(p)
p.heart.beat()
print(p.heart)

t = Tick()
t.suck_blood()
print(t)

pm = Puma(age=5, tick=t)
pm.tick.suck_blood()
print(pm)
pm.claw()

pm2 = Puma(age=3)
pm2.claw()