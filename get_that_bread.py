import numpy as np
import matplotlib.pyplot as plt
import random
import datetime
import time


players = ['Kaylie', 'Luca', 'John', 'Zach', 'Antonio', 'Kyle', 'Ritwik', 'Carter', 'Demetri', 'Courtney']
stepProb = 0.5
y_pos = list(range(len(players)))
distance = [0 for p in players]

fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks(y_pos)
ax.set_yticklabels(players)
ax.invert_yaxis()
ax.set_xlabel('Position')
ax.set_title("Who's tryna get that bread?")
rects = ax.barh(range(len(players)), np.ones(len(players)), color=['cyan', 'green', 'red', 'lightgray', 'blue', 'gold', 'pink', 'indigo', 'gray', 'darkorange']) 


endTime = datetime.datetime(2020,8,13,11,59,59)
while(True):
    step = [int(random.random() > stepProb) for p in players]
    distance = [sum(x) for x in zip(distance, step)]
    for rect,d in zip(rects,distance):
        rect.set_width(d)
    fig.canvas.draw()
    ax.relim()
    ax.autoscale_view()
    plt.pause(1.0)
    now = datetime.datetime.now()
    if now > endTime:
    	time.sleep(86400)