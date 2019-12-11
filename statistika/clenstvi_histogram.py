import numpy as np
from matplotlib import pyplot as plt

year = 2019


anpetu = np.loadtxt("anpetu.txt", dtype=np.str)
hanyetu = np.loadtxt("hanyetu.txt", dtype=np.str)


mem_a = 2019 - anpetu[:, 3].astype(np.int)
mem_h = 2019 - hanyetu[:, 3].astype(np.int)

beg = 0
end = 20

bins = np.linspace(beg-0.5, end-0.5, num=end-beg+1)


plt.rcParams['font.size'] = 12
fig, (ax_a, ax_h) = plt.subplots(2, 1, figsize=(8, 5))


yticks = np.linspace(0, 12, num= 7)

ax_a.hist(mem_a, bins=bins, rwidth = 0.9)
ax_a.set_xticks(bins+0.5)
ax_a.set_ylabel("Anpetu")
ax_a.grid(axis = "y")
ax_a.set_axisbelow(True)
ax_a.set_yticks(yticks)

ax_h.hist(mem_h, bins=bins, rwidth = 0.9)
ax_h.set_xticks(bins+0.5)
ax_h.set_ylabel("Hanyetu")
ax_h.grid(axis = "y")
ax_h.set_axisbelow(True)
ax_h.set_yticks(yticks)


ax_h.set_xlabel("Roky v oddíle")

plt.savefig("hist_clen.pdf")
plt.show()

#Letos poprvé ~ 0
#Na osu se nevejdou např. Perňa nebo Máří