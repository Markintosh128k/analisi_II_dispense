"""Ridisegna fig_03, fig_08, fig_09 con la curva indicata da phi (stesso stile degli originali)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

BLU = "#1f4e9c"
ROSSO = "#c0392b"
plt.rcParams.update({
    "font.family": "STIXGeneral",
    "mathtext.fontset": "stix",
    "font.size": 13,
})


def freccia_su_curva(ax, x, y, i, color, size=14, lw=0):
    ax.annotate("", xy=(x[i + 1], y[i + 1]), xytext=(x[i - 1], y[i - 1]),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=size))


def assi(ax, x0, x1, y0, y1, xlab=True, ylab=True, fs=15):
    kw = dict(arrowstyle="-|>", color="black", lw=1.0, mutation_scale=14)
    ax.add_patch(FancyArrowPatch((x0, 0), (x1, 0), **kw))
    ax.add_patch(FancyArrowPatch((0, y0), (0, y1), **kw))
    if xlab:
        ax.text(x1, -0.02 * (y1 - y0), "$x$", ha="right", va="top", fontsize=fs)
    if ylab:
        ax.text(0.02 * (x1 - x0), y1, "$y$", ha="left", va="top", fontsize=fs)


# ------------------------------------------------------------------ fig_03
def fig03():
    fig = plt.figure(figsize=(5.16, 2.22))
    # intervallo [a,b]
    ax1 = fig.add_axes([0.0, 0.0, 0.30, 1.0])
    ax1.set_xlim(-0.1, 1.2); ax1.set_ylim(-1.0, 1.0); ax1.axis("off")
    ax1.plot([0.0, 1.0], [0, 0], color="black", lw=2)
    for xx in (0.0, 1.0):
        ax1.plot([xx, xx], [-0.09, 0.09], color="black", lw=2)
    ax1.plot(0.4, 0, "o", color=ROSSO, ms=6)
    ax1.text(0.4, 0.17, "$t$", ha="center", va="bottom", fontsize=15)
    ax1.text(0.0, -0.18, "$a$", ha="center", va="top", fontsize=15)
    ax1.text(1.0, -0.18, "$b$", ha="center", va="top", fontsize=15)
    # freccia phi
    fig.patches.append(FancyArrowPatch((0.28, 0.66), (0.46, 0.84), transform=fig.transFigure,
                                       connectionstyle="arc3,rad=-0.45", arrowstyle="-|>",
                                       color="black", lw=1.5, mutation_scale=16))
    fig.text(0.365, 0.92, r"$\varphi$", ha="center", va="bottom", fontsize=16)
    # piano
    ax2 = fig.add_axes([0.45, 0.0, 0.55, 1.0])
    ax2.set_xlim(-0.35, 5.2); ax2.set_ylim(-0.45, 3.75); ax2.axis("off")
    assi(ax2, -0.3, 5.0, -0.4, 3.7)
    s = np.linspace(0, 1, 200)
    X = 0.55 + 4.1 * s
    Y = 0.85 + 2.35 * (1 - (1 - s) ** 2) * 0.95
    ax2.plot(X, Y, color=BLU, lw=2.2, solid_capstyle="round")
    ax2.plot(X[0], Y[0], "o", color=BLU, ms=8)
    ax2.plot(X[-1], Y[-1], "o", color=BLU, ms=8)
    idx = [25, 70, 115, 160]
    for k, i in enumerate(idx):
        ax2.plot(X[i], Y[i], "o", color=BLU, ms=4)
        dx, dy = X[i + 1] - X[i], Y[i + 1] - Y[i]
        nrm = np.hypot(dx, dy)
        L = 0.62
        ax2.annotate("", xy=(X[i] + L * dx / nrm, Y[i] + L * dy / nrm), xytext=(X[i], Y[i]),
                     arrowprops=dict(arrowstyle="-|>", color=ROSSO, lw=1.5, mutation_scale=13))
    ax2.text(X[0] + 0.05, Y[0] - 0.22, r"$\varphi(a)$", ha="center", va="top", fontsize=15)
    ax2.text(X[-1] + 0.12, Y[-1], r"$\varphi(b)$", ha="left", va="center", fontsize=15)
    ax2.text(X[70] + 0.1, Y[70] - 0.2, r"$\varphi(t)$", ha="left", va="top", fontsize=15)
    ax2.text(X[115] - 0.1, Y[115] + 0.35, r"$T(t)$", ha="center", va="bottom", fontsize=15,
             color=ROSSO)
    fig.savefig("figure/fig_03.pdf", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


# ------------------------------------------------------------------ fig_08
def fig08():
    fig, ax = plt.subplots(figsize=(4.4, 2.65))
    t = np.linspace(-1, 1, 801)
    x, y = t ** 3, t ** 2
    ax.set_xlim(-1.35, 1.4); ax.set_ylim(-0.4, 1.35); ax.axis("off")
    ax.set_aspect("auto")
    assi(ax, -1.3, 1.4, -0.4, 1.3, fs=13)
    ax.plot(x, y, color=BLU, lw=2.2)
    for tt in (-0.62, 0.55):
        i = np.argmin(abs(t - tt))
        freccia_su_curva(ax, x, y, i, BLU, size=16)
    ax.plot([-1, 1], [1, 1], "o", color=BLU, ms=7)
    ax.plot(0, 0, "o", color=ROSSO, ms=7, zorder=5)
    ax.text(-1.0, 1.1, r"$\varphi(-1)=(-1,\,1)$", ha="center", va="bottom", fontsize=13)
    ax.text(1.0, 1.1, r"$\varphi(1)=(1,\,1)$", ha="center", va="bottom", fontsize=13)
    ax.annotate("cuspide: $\\varphi\\prime\\!(0)=(0,0)$", xy=(0, 0), xytext=(1.4, -0.3),
                ha="right", va="center", color=ROSSO, fontsize=13,
                arrowprops=dict(arrowstyle="-", color=ROSSO, lw=0.9, shrinkA=0, shrinkB=0,
                                relpos=(0.45, 1.0)))
    fig.savefig("figure/fig_08.pdf", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


# ------------------------------------------------------------------ fig_09
def fig09():
    r = 1.0
    fig, ax = plt.subplots(figsize=(5.3, 1.6))
    ax.set_xlim(-0.4, 4 * np.pi + 1.1); ax.set_ylim(-0.7, 2.75); ax.axis("off")
    ax.set_aspect("equal")
    assi(ax, -0.15, 4 * np.pi + 1.0, -0.25, 2.7, xlab=False, fs=12)
    ax.text(4 * np.pi + 1.0, 0.12, "$x$", ha="right", va="bottom", fontsize=12)
    t1 = np.linspace(0, 2 * np.pi, 400)
    t2 = np.linspace(2 * np.pi, 4 * np.pi, 400)
    ax.plot(r * (t1 - np.sin(t1)), r * (1 - np.cos(t1)), color=BLU, lw=2.2)
    ax.plot(r * (t2 - np.sin(t2)), r * (1 - np.cos(t2)), color=BLU, lw=1.6, ls=(0, (4, 2.5)))
    x1, y1 = r * (t1 - np.sin(t1)), r * (1 - np.cos(t1))
    freccia_su_curva(ax, x1, y1, 70, BLU, size=14)
    tc = 2.3
    ax.add_patch(Circle((r * tc, r), r, fill=False, color="0.45", lw=1.1))
    px, py = r * (tc - np.sin(tc)), r * (1 - np.cos(tc))
    ax.plot([r * tc, px], [r, py], color="0.45", lw=1.1)
    ax.plot(r * tc, r, "o", color="0.45", ms=3)
    ax.plot(px, py, "o", color=ROSSO, ms=6.5, zorder=5)
    ax.text(px - 0.12, py + 0.1, r"$\varphi(t)$", color=ROSSO, ha="right", va="bottom", fontsize=12)
    for xx in (0, 2 * np.pi, 4 * np.pi):
        ax.plot(xx, 0, "o", color="black", ms=4, zorder=5)
    ax.text(-0.18, -0.08, "$0$", ha="right", va="top", fontsize=12)
    ax.text(2 * np.pi - 0.1, -0.08, r"$2\pi r$", ha="right", va="top", fontsize=12)
    ax.text(4 * np.pi - 0.1, -0.08, r"$4\pi r$", ha="right", va="top", fontsize=12)
    ax.annotate("cuspide", xy=(2 * np.pi, 0), xytext=(2 * np.pi + 0.45, -0.3), color=ROSSO,
                ha="left", va="top", fontsize=12,
                arrowprops=dict(arrowstyle="-", color=ROSSO, lw=0.8, shrinkA=0, shrinkB=0,
                                relpos=(0.0, 1.0)))
    ax.text(np.pi, 2.2, r"$t\in[0,\,2\pi]$", color=BLU, ha="center", va="bottom", fontsize=12)
    ax.text(3 * np.pi, 2.2, r"$t\in[2\pi,\,4\pi]$", color=BLU, ha="center", va="bottom", fontsize=12)
    fig.savefig("figure/fig_09.pdf", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


if __name__ == "__main__":
    fig03(); fig08(); fig09()
