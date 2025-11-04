import matplotlib.pyplot as plt
import numpy as np

base00 = "#657b83"
base0 = "#839496"
orange ="#cb4b16"

swr = np.linspace(1, 6, 100)

def rho(swr):
    return (swr - 1) / (swr + 1)
def ml(swr):
    return -10 * np.log10(1- rho(swr)**2)

plt.figure(figsize=[8, 4])
plt.plot(swr, ml(swr), '-', color="#839496")

for swr_val in [1.5, 2.0, 3.0, 4.0, 5.0, 6.0]:
    plt.scatter(swr_val, ml(swr_val), marker="o", color=base0)
    plt.text(swr_val, ml(swr_val), f"{ml(swr_val):.1f} dB  ", fontsize=12, ha='right', color=base0)

xticks = np.arange(1, swr[-1]+1, 1.0)
plt.xticks(xticks, labels=[f"{i:.0f}:1" for i in xticks])

plt.gca().spines[['top', 'right']].set_visible(False)
plt.gca().spines[['left', 'bottom']].set_color(base00)
plt.gca().tick_params(which='both', color=base00, labelcolor=base00)
plt.xlabel("SWR", color=base00)
plt.ylabel("Mismatch loss (dB)", color=base00)
plt.tight_layout()
plt.savefig("assets/images/swr/swr-ml.svg", transparent=True)