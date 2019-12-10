import numpy as np
from matplotlib import pyplot as plt

anpetu = np.loadtxt("anpetu.txt", dtype=np.str)
hanyetu = np.loadtxt("hanyetu.txt", dtype=np.str)


age_a = anpetu[:, 1].astype(np.int)
age_h = hanyetu[:, 1].astype(np.int)


beg = 7
end = 25

bins = np.linspace(beg-0.5, end-0.5, num=end-beg+1)


fig, (ax_a, ax_h) = plt.subplots(2, 1, figsize=(10, 6))

fig.suptitle("Histogram rozdělení věku")

ax_a.hist(age_a, bins=bins, rwidth = 0.9)
ax_a.set_xticks(bins+0.5)
ax_a.set_ylabel("Anpetu")
ax_a.grid(axis = "y")
ax_a.set_axisbelow(True)

ax_h.hist(age_h, bins=bins, rwidth = 0.9)
ax_h.set_xticks(bins+0.5)
ax_h.set_ylabel("Hanyetu")
ax_h.grid(axis = "y")
ax_h.set_axisbelow(True)


ax_h.set_xlabel("Věk")

plt.show()