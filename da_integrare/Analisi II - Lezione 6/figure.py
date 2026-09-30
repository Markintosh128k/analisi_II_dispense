"""Figure della dispensa: Analisi II - Lezione 6 (topologia in R^2).

Ogni funzione fig_NN() ricostruisce una figura degli appunti (o descritta
dalla docente alla lavagna) e la salva in figure/fig_NN.pdf.
Uso:  python figure.py
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, Polygon, Rectangle

OUT = "figure"
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.size": 11,
    "mathtext.fontset": "cm",
    "font.family": "serif",
})

C_SET = "#9ecae1"      # riempimento degli insiemi
C_EDGE = "#1f4e79"     # bordo degli insiemi
C_FRONT = "#e6550d"    # frontiera (arancione, come alla lavagna)
C_VEC = "#08306b"


def salva(fig, nome):
    fig.savefig(os.path.join(OUT, nome + ".pdf"), bbox_inches="tight")
    plt.close(fig)


def assi(ax, xlim, ylim, xl="$x$", yl="$y$", tacche=False):
    """Assi cartesiani passanti per l'origine, con frecce."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    if not tacche:
        ax.set_xticks([])
        ax.set_yticks([])
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="->", lw=0.9, color="k"))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="->", lw=0.9, color="k"))
    ax.text(xlim[1], -0.04 * (ylim[1] - ylim[0]), xl, ha="right", va="top")
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], yl, ha="left", va="top")


def freccia(ax, p, q, col=C_VEC, lw=1.6, **kw):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", lw=lw, color=col,
                                shrinkA=0, shrinkB=0, **kw))


def blob(cx=0.0, cy=0.0, r=1.0, n=400):
    """Curva chiusa 'a patata' per disegnare un insieme generico."""
    t = np.linspace(0, 2 * np.pi, n)
    rr = r * (1 + 0.18 * np.cos(2 * t) + 0.10 * np.sin(3 * t))
    return cx + 1.25 * rr * np.cos(t), cy + rr * np.sin(t)


# ---------------------------------------------------------------------------
def fig_01():
    """Da una a due variabili: grafico in R^2 contro grafico in R^3."""
    fig = plt.figure(figsize=(9, 3.6))
    ax1 = fig.add_subplot(1, 2, 1)
    x = np.linspace(0.5, 3.5, 200)
    ax1.plot(x, 1 + 0.5 * np.sin(2 * x) + 0.15 * x, color=C_VEC, lw=1.8)
    ax1.plot([0.5, 3.5], [0, 0], color=C_FRONT, lw=4, solid_capstyle="butt")
    ax1.text(0.5, -0.12, "$a$", ha="center", va="top")
    ax1.text(3.5, -0.12, "$b$", ha="center", va="top")
    assi(ax1, (-0.3, 4.2), (-0.4, 2.3))
    ax1.set_title(r"$f:[a,b]\to\mathbb{R}$: grafico in $\mathbb{R}^2$")

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    X, Y = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))
    Z = np.exp(-(X**2 + Y**2) / 2) * (1 + 0.3 * X)
    ax2.plot_surface(X, Y, Z, cmap="Blues", alpha=0.85, lw=0)
    ax2.contourf(X, Y, Z, zdir="z", offset=-0.4, cmap="Blues", alpha=0.4)
    ax2.set_zlim(-0.4, 1.4)
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$y$")
    ax2.set_zlabel("$z$")
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_zticks([])
    ax2.set_title(r"$z=f(x,y)$: grafico in $\mathbb{R}^3$")
    salva(fig, "fig_01")


def fig_02():
    """Norma di v=(x,y): teorema di Pitagora."""
    fig, ax = plt.subplots(figsize=(4.2, 3.2))
    x, y = 3.0, 2.0
    ax.plot([x, x], [0, y], "--", color="gray", lw=1)
    ax.plot([0, x], [y, y], ":", color="gray", lw=1)
    ax.add_patch(Rectangle((x - 0.2, 0), 0.2, 0.2, fill=False, lw=0.8))
    ax.plot([0, x], [0, y], color=C_FRONT, lw=2)
    ax.plot(x, y, "o", color=C_VEC)
    ax.text(x + 0.1, y + 0.1, r"$v=(x,y)$")
    ax.text(1.2, 1.15, r"$\|v\|=\sqrt{x^2+y^2}$", rotation=33.7,
            ha="center", va="bottom", color=C_FRONT)
    ax.text(x / 2, -0.12, "$x$", ha="center", va="top")
    ax.text(x + 0.1, y / 2, "$y$", va="center")
    assi(ax, (-0.3, 4.2), (-0.4, 2.8), xl="", yl="")
    salva(fig, "fig_02")


def fig_03():
    """Disuguaglianza triangolare: regola del parallelogramma."""
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    v1, v2 = np.array([3.0, 0.8]), np.array([1.0, 2.0])
    s = v1 + v2
    ax.add_patch(Polygon([(0, 0), v1, s], closed=True, color=C_SET, alpha=0.5))
    ax.plot([v2[0], s[0]], [v2[1], s[1]], "--", color="gray")
    ax.plot([v1[0], s[0]], [v1[1], s[1]], "--", color="gray")
    freccia(ax, (0, 0), v1)
    freccia(ax, (0, 0), v2)
    freccia(ax, (0, 0), s, col=C_FRONT)
    ax.text(*(v1 / 2 + [0.1, -0.35]), "$v_1$")
    ax.text(*(v2 / 2 + [-0.45, 0.05]), "$v_2$")
    ax.text(*(s / 2 + [-0.6, 0.3]), "$v_1+v_2$", color=C_FRONT)
    ax.text(*((v1 + s) / 2 + [0.1, -0.1]), r"$\|v_2\|$")
    ax.text(2.3, 1.0, "$T$", fontsize=13)
    assi(ax, (-0.3, 4.6), (-0.4, 3.3), xl="", yl="")
    salva(fig, "fig_03")


def fig_04():
    """Angolo theta in [0, pi] tra due vettori di R^2."""
    fig, ax = plt.subplots(figsize=(4.0, 3.0))
    v1, v2 = np.array([3.0, 0.7]), np.array([0.9, 2.3])
    freccia(ax, (0, 0), v1)
    freccia(ax, (0, 0), v2)
    a1, a2 = np.degrees(np.arctan2(v1[1], v1[0])), np.degrees(np.arctan2(v2[1], v2[0]))
    ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=a1, theta2=a2, color=C_FRONT, lw=1.5))
    ax.text(0.75, 0.62, r"$\theta$", color=C_FRONT, fontsize=13)
    ax.text(*(v1 + [0.05, 0.1]), "$v_1$")
    ax.text(*(v2 + [0.05, 0.05]), "$v_2$")
    ax.text(1.6, 2.4, r"$\theta\in[0,\pi]$")
    assi(ax, (-0.3, 3.6), (-0.3, 2.7), xl="", yl="")
    salva(fig, "fig_04")


def fig_05():
    """Intorno sferico: norma euclidea (disco) e norma del massimo (quadrato)."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(8, 3.6))
    x0, y0, d = 1.6, 1.2, 0.9
    a.add_patch(Circle((x0, y0), d, facecolor=C_SET, edgecolor=C_EDGE,
                       ls="--", lw=1.4, alpha=0.8))
    a.plot(x0, y0, "o", color=C_VEC, ms=4)
    a.text(x0 - 0.1, y0 - 0.1, "$P_0$", ha="right", va="top")
    a.annotate("", xy=(x0 + d * np.cos(0.6), y0 + d * np.sin(0.6)), xytext=(x0, y0),
               arrowprops=dict(arrowstyle="->", lw=1))
    a.text(x0 + 0.42, y0 + 0.45, r"$\delta$")
    assi(a, (-0.4, 3.0), (-0.4, 2.5))
    a.set_title(r"$(x-x_0)^2+(y-y_0)^2<\delta^2$", fontsize=11)

    b.add_patch(Rectangle((-1, -1), 2, 2, facecolor=C_SET, edgecolor=C_EDGE,
                          ls="--", lw=1.4, alpha=0.8))
    b.text(1.05, -0.12, "$1$", va="top")
    b.text(-1.05, -0.12, "$-1$", va="top", ha="right")
    b.text(0.06, 1.05, "$1$", va="bottom")
    b.text(0.06, -1.05, "$-1$", va="top")
    assi(b, (-1.7, 1.7), (-1.6, 1.6))
    b.set_title(r"$\max\{|x|,|y|\}<1$", fontsize=11)
    salva(fig, "fig_05")


def fig_06():
    """Punti interni, esterni, di frontiera, isolati."""
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    bx, by = blob(2.2, 1.6, 1.0)
    ax.fill(bx, by, color=C_SET, alpha=0.7)
    ax.plot(bx, by, color=C_FRONT, lw=2.2)
    ax.text(2.2 + 0.6, 1.6 + 0.8, "$A$", fontsize=13)
    # interno
    p = (1.9, 1.4)
    ax.add_patch(Circle(p, 0.35, fill=False, ls="--", color=C_VEC))
    ax.plot(*p, "o", color=C_VEC, ms=4)
    ax.annotate("interno", xy=p, xytext=(0.2, 0.4),
                arrowprops=dict(arrowstyle="->", lw=0.8))
    # frontiera
    i = 30
    q = (bx[i], by[i])
    ax.add_patch(Circle(q, 0.3, fill=False, ls="--", color=C_VEC))
    ax.plot(*q, "o", color=C_VEC, ms=4)
    ax.annotate("di frontiera", xy=q, xytext=(4.1, 2.9),
                arrowprops=dict(arrowstyle="->", lw=0.8))
    # esterno
    e = (4.4, 0.6)
    ax.add_patch(Circle(e, 0.3, fill=False, ls="--", color=C_VEC))
    ax.plot(*e, "o", color=C_VEC, ms=4)
    ax.text(e[0] + 0.35, e[1] - 0.1, "esterno", va="center")
    # isolato
    s = (4.6, 2.0)
    ax.plot(*s, "o", color=C_SET, mec=C_FRONT, ms=7, mew=1.5)
    ax.add_patch(Circle(s, 0.25, fill=False, ls=":", color=C_VEC))
    ax.text(s[0] + 0.3, s[1], r"isolato ($\in A$)", va="center")
    ax.text(0.5, 3.3, r"in arancione: $\partial A$", color=C_FRONT)
    assi(ax, (-0.3, 6.3), (-0.3, 3.6))
    salva(fig, "fig_06")


def fig_07():
    """Frontiera: in R sono gli estremi, in R^2 e' una curva."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(8, 2.8),
                               gridspec_kw=dict(width_ratios=[1.2, 1]))
    a.plot([-0.5, 3.5], [0, 0], color="k", lw=0.8)
    a.plot([0.5, 2.5], [0, 0], color=C_SET, lw=6, solid_capstyle="butt")
    a.plot([0.5, 2.5], [0, 0], "o", color=C_FRONT, ms=7)
    a.text(0.5, -0.15, "$a$", ha="center", va="top")
    a.text(2.5, -0.15, "$b$", ha="center", va="top")
    a.text(1.5, 0.25, r"$\partial[a,b]=\{a,b\}$", ha="center")
    a.set_xlim(-0.6, 3.6)
    a.set_ylim(-0.6, 0.7)
    a.set_aspect("equal")
    a.axis("off")
    a.set_title(r"in $\mathbb{R}$")

    bx, by = blob(0, 0, 1)
    b.fill(bx, by, color=C_SET, alpha=0.7)
    b.plot(bx, by, color=C_FRONT, lw=2.2)
    b.text(0, 0, "$A$", ha="center", va="center", fontsize=13)
    b.text(1.5, 0.9, r"$\partial A$: una curva", color=C_FRONT)
    b.set_aspect("equal")
    b.set_xlim(-1.7, 3.2)
    b.axis("off")
    b.set_title(r"in $\mathbb{R}^2$")
    salva(fig, "fig_07")


def fig_08():
    """Aperti e chiusi: bordo continuo = appartiene, tratteggiato = no."""
    fig, axs = plt.subplots(1, 4, figsize=(11, 3.0))
    # (a) ne' aperto ne' chiuso: parte del bordo inclusa, parte no
    ax = axs[0]
    t = np.linspace(-np.pi / 2, np.pi / 2, 100)
    arc_x, arc_y = 1.2 + np.cos(t), 1.2 + np.sin(t)
    ax.fill(np.r_[arc_x, 0.4, 0.4], np.r_[arc_y, 2.2, 0.2], color=C_SET, alpha=0.7)
    ax.plot(arc_x, arc_y, color=C_EDGE, lw=1.8)
    ax.plot([0.4, 1.2], [2.2, 2.2], color=C_EDGE, lw=1.8)
    ax.plot([0.4, 0.4, 1.2], [2.2, 0.2, 0.2], "--", color=C_EDGE, lw=1.4)
    ax.text(1.5, 1.2, "$A$")
    assi(ax, (-0.3, 2.8), (-0.3, 2.7))
    ax.set_title("né aperto né chiuso", fontsize=10)
    # (b) semipiano chiuso (illimitato)
    ax = axs[1]
    xs = np.array([-0.3, 2.8])
    ax.fill_between(xs, 0.4 + 0.6 * xs, 2.7, color=C_SET, alpha=0.7)
    ax.plot(xs, 0.4 + 0.6 * xs, color=C_EDGE, lw=1.8)
    assi(ax, (-0.3, 2.8), (-0.3, 2.7))
    ax.set_title("chiuso (illimitato)", fontsize=10)
    # (c) disco chiuso
    ax = axs[2]
    ax.add_patch(Circle((1.3, 1.2), 0.8, facecolor=C_SET, edgecolor=C_EDGE, lw=1.8, alpha=0.9))
    ax.text(1.3, 1.2, "$C$", ha="center", va="center")
    assi(ax, (-0.3, 2.8), (-0.3, 2.7))
    ax.set_title("chiuso (e limitato)", fontsize=10)
    # (d) aperto
    ax = axs[3]
    bx, by = blob(1.3, 1.2, 0.65)
    ax.fill(bx, by, color=C_SET, alpha=0.7)
    ax.plot(bx, by, "--", color=C_EDGE, lw=1.4)
    ax.text(1.3, 1.2, "$A$", ha="center", va="center")
    assi(ax, (-0.3, 2.8), (-0.3, 2.7))
    ax.set_title("aperto", fontsize=10)
    salva(fig, "fig_08")


def _griglia(lim=2.2, n=700):
    return np.meshgrid(np.linspace(-lim, lim, n), np.linspace(-lim, lim, n))


def fig_09():
    """Esercizio: E = {|y|<x, x^2+y^2<=3, y<x^2}, costruito passo per passo."""
    X, Y = _griglia()
    c1 = np.abs(Y) < X
    c2 = Y < X**2
    c3 = X**2 + Y**2 <= 3
    xx = np.linspace(-2.2, 2.2, 400)
    r3 = np.sqrt(3)
    fig, axs = plt.subplots(2, 2, figsize=(8, 8))
    pannelli = [
        (c1, r"(a) $|y|<x$", "#fbb4c4"),
        (c2, r"(b) $y<x^2$", "#fdd49e"),
        (c3, r"(c) $x^2+y^2\leq 3$", "#fff3a0"),
        (c1 & c2 & c3, r"(d) $E$: intersezione", C_SET),
    ]
    for ax, (m, tit, col) in zip(axs.flat, pannelli):
        ax.contourf(X, Y, m.astype(float), levels=[0.5, 1.5], colors=[col], alpha=0.9)
        ax.set_title(tit)
        assi(ax, (-2.2, 2.2), (-2.2, 2.2))
    # bordi dei singoli vincoli
    a = axs[0, 0]
    a.plot([0, 2.2], [0, 2.2], "--", color="#c51b7d")
    a.plot([0, 2.2], [0, -2.2], "--", color="#c51b7d")
    a.text(1.5, 1.8, "$y=x$")
    a.text(1.4, -1.9, "$y=-x$")
    a = axs[0, 1]
    xp = np.linspace(-1.5, 1.5, 200)
    a.plot(xp, xp**2, "--", color="#d95f0e")
    a.text(1.0, 1.9, "$y=x^2$")
    a = axs[1, 0]
    a.add_patch(Circle((0, 0), r3, fill=False, color="#b8860b", lw=1.6))
    a.text(1.0, 1.55, r"$r=\sqrt{3}$")
    # (d) frontiera di E: tratteggiata dove non appartiene, continua dove appartiene
    a = axs[1, 1]
    xm = np.sqrt(1.5)
    a.plot([0, xm], [0, -xm], "--", color=C_FRONT, lw=1.8)            # y = -x
    xp = np.linspace(0, 1, 100)
    a.plot(xp, xp**2, "--", color=C_FRONT, lw=1.8)                    # parabola
    a.plot([1, xm], [1, xm], "--", color=C_FRONT, lw=1.8)             # y = x
    th = np.linspace(-np.pi / 4, np.pi / 4, 100)
    a.plot(r3 * np.cos(th), r3 * np.sin(th), color=C_FRONT, lw=2.2)   # arco
    a.plot(0, 0, "o", mfc="white", mec=C_FRONT, ms=6)
    a.plot(1, 1, "o", color=C_FRONT, ms=3)
    a.text(1.02, 0.98, "$(1,1)$", ha="right", va="bottom", fontsize=9)
    a.text(0.9, 0.05, "$E$", fontsize=13)
    a.plot(xx, xx**2, ":", color="gray", lw=0.7)
    a.plot(xx, xx, ":", color="gray", lw=0.7)
    a.plot(xx, -xx, ":", color="gray", lw=0.7)
    a.add_patch(Circle((0, 0), r3, fill=False, ls=":", color="gray", lw=0.7))
    salva(fig, "fig_09")


def _clessidra(ax, chiusa=True, alpha=0.8):
    top = Polygon([(0, 0), (-1, 1), (1, 1)], closed=True)
    bot = Polygon([(0, 0), (-1, -1), (1, -1)], closed=True)
    ls = "-" if chiusa else "--"
    for tri in (top, bot):
        tri.set_facecolor(C_SET)
        tri.set_edgecolor(C_EDGE)
        tri.set_linestyle(ls)
        tri.set_linewidth(1.6)
        tri.set_alpha(alpha)
        ax.add_patch(tri)


def fig_10():
    """Clessidra senza frontiera (aperta): non e' connessa."""
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    _clessidra(ax, chiusa=False)
    ax.plot(0, 0, "o", mfc="white", mec=C_EDGE, ms=6)
    ax.plot([-0.3, 0.2], [0.7, -0.6], "o", color=C_VEC, ms=4)
    ax.text(-0.3, 0.75, "$P$", va="bottom", ha="center")
    ax.text(0.2, -0.65, "$Q$", va="top", ha="center")
    ax.text(0.15, 0.55, "$A_1$")
    ax.text(0.3, -0.35, "$A_2$")
    assi(ax, (-1.4, 1.4), (-1.3, 1.3))
    salva(fig, "fig_10")


def fig_11():
    """Convessi e non convessi."""
    fig, axs = plt.subplots(1, 4, figsize=(11, 2.9))
    for ax in axs:
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.3, 1.3)
    # disco
    axs[0].add_patch(Circle((0, 0), 1, facecolor=C_SET, edgecolor=C_EDGE, lw=1.6))
    axs[0].plot([-0.6, 0.5], [0.4, -0.6], "o-", color=C_VEC, ms=4)
    axs[0].set_title("convesso", fontsize=10)
    # ellisse
    axs[1].add_patch(Ellipse((0, 0), 2.8, 1.3, facecolor=C_SET, edgecolor=C_EDGE, lw=1.6))
    axs[1].plot([-1.0, 0.9], [0.1, -0.3], "o-", color=C_VEC, ms=4)
    axs[1].set_title("convesso", fontsize=10)
    # a forma di C
    th = np.linspace(np.pi / 4, 7 * np.pi / 4, 200)
    xo, yo = np.cos(th), np.sin(th)
    xi, yi = 0.5 * np.cos(th[::-1]), 0.5 * np.sin(th[::-1])
    axs[2].fill(np.r_[xo, xi], np.r_[yo, yi], facecolor=C_SET, edgecolor=C_EDGE, lw=1.6)
    p, q = (0.53, 0.53), (0.53, -0.53)
    axs[2].plot(*zip(p, q), "o-", color=C_FRONT, ms=4)
    axs[2].set_title("non convesso", fontsize=10)
    # corona circolare (ciambella)
    axs[3].add_patch(Circle((0, 0), 1, facecolor=C_SET, edgecolor=C_EDGE, lw=1.6))
    axs[3].add_patch(Circle((0, 0), 0.45, facecolor="white", edgecolor=C_EDGE, lw=1.6))
    axs[3].plot([-0.75, 0.75], [0.05, -0.05], "o-", color=C_FRONT, ms=4)
    axs[3].set_title("non convesso (ma connesso)", fontsize=10)
    salva(fig, "fig_11")


def fig_12():
    """Clessidra chiusa: stellata rispetto all'origine, non convessa;
    connessa per poligonali ma non connessa."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.4, 3.6))
    _clessidra(a)
    for p in [(-0.8, 0.9), (0.5, 0.7), (0.9, 0.95), (-0.3, -0.8), (0.7, -0.9), (-0.9, -0.95)]:
        a.plot([0, p[0]], [0, p[1]], color=C_VEC, lw=0.9)
        a.plot(*p, "o", color=C_VEC, ms=3)
    a.plot([0.8, 0.8], [0.9, -0.9], "--", color=C_FRONT, lw=1.4)
    a.plot([0.8, 0.8], [0.9, -0.9], "o", color=C_FRONT, ms=4)
    a.plot(0, 0, "*", color="gold", mec="k", ms=12)
    a.set_title("stellato rispetto a $O$, non convesso", fontsize=10)
    assi(a, (-1.4, 1.4), (-1.3, 1.3))

    _clessidra(b)
    P, Q = (0.6, 0.85), (-0.5, -0.8)
    b.plot([P[0], 0, Q[0]], [P[1], 0, Q[1]], "-", color=C_FRONT, lw=1.8)
    b.plot([P[0], Q[0]], [P[1], Q[1]], "o", color=C_FRONT, ms=4)
    b.text(P[0] + 0.05, P[1] + 0.05, "$P$")
    b.text(Q[0] - 0.05, Q[1] - 0.08, "$Q$", ha="right", va="top")
    b.set_title("connesso per poligonali (spezzata per $O$)", fontsize=10)
    assi(b, (-1.4, 1.4), (-1.3, 1.3))
    salva(fig, "fig_12")


def main():
    for f in (fig_01, fig_02, fig_03, fig_04, fig_05, fig_06,
              fig_07, fig_08, fig_09, fig_10, fig_11, fig_12):
        f()
        print("ok", f.__name__)


if __name__ == "__main__":
    main()
