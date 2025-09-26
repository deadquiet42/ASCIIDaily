#!/usr/bin/env python3
import sys, math, random, datetime

w, h = 80, 28
seed = str(datetime.date.today())
random.seed(seed)

ramp = " .:-=+*#%@"
rlen = len(ramp) - 1

a, b = random.random()*2, random.random()*2
c, d = random.random()*2, random.random()*2

def noise(x, y):
    v = math.sin(a*x) + math.cos(b*y) + math.sin(c*x + d*y)
    return (v + 3) / 6

sx = 2*math.pi / w
sy = 2*math.pi / h

print("Generated on:", datetime.date.today())
print()

for j in range(h):
    line = ""
    for i in range(w):
        v = noise(i * sx, j * sy)
        idx = int(v * rlen)
        line += ramp[idx]
    print(line)

