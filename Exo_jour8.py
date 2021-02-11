import matplotlib.pyplot as plt
import math

"""
figure, axes = plt.subplots()
draw_circle = plt.Circle((0.5, 0.5), 0.3,fill=False)
axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title('Circle')
plt.show()
"""
prev_x = 0
prev_y = 50
new_x = 0
new_y = 50
for i in range (1, 30) :
    prev_x = new_x
    prev_y = new_y
    new_x = 50 + math.cos(math.radians(360/i) - math.pi / 2) * 50
    new_y = 50 + math.sin(math.radians(360/i) - math.pi / 2) * 50
    plt.plot([prev_x, prev_x], [new_y, prev_y], 'k-')

plt.show()
plt.close()