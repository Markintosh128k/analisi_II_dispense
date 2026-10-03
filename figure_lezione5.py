#!/usr/bin/env python3
"""Figure della dispensa di Analisi II, lezione 5 (figura fig_13).

Uso: python3 figure_lezione5.py  ->  salva figure/fig_NN.pdf
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

CARTELLA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figure")


def salva(fig, nome):
    os.makedirs(CARTELLA, exist_ok=True)
    fig.savefig(os.path.join(CARTELLA, nome + ".pdf"), bbox_inches="tight")
    plt.close(fig)


def graffa_orizzontale(ax, x0, x1, y, altezza, **kw):
    """Disegna una graffa orizzontale da x0 a x1 con la punta verso l'alto."""
    # due mezze graffe: profilo che sale ai bordi e fa la punta al centro
    meta = 0.5 * (x1 - x0)
    s = np.linspace(0.0, 1.0, 200)
    profilo = altezza * (0.5 / (1 + np.exp(-40 * (s - 0.08)))
                         + 0.5 / (1 + np.exp(-40 * (s - 0.92))))
    xs = np.concatenate([x0 + meta * s, x0 + meta + meta * s])
    ys = np.concatenate([y + profilo, y + profilo[::-1]])
    ax.plot(xs, ys, **kw)


def parentesi(ax, x, verso, altezza, **kw):
    """Parentesi quadra disegnata sull'asse: verso=+1 per '[', -1 per ']'."""
    d = 0.025 * verso
    ax.plot([x + d, x, x, x + d], [altezza, altezza, -altezza, -altezza], **kw)


def fig_13():
    """Compatti [-r, r] sempre più grandi dentro ]-rho, rho[ (appunti p. 3, audio 0:22:56)."""
    rho = 1.0
    fig, ax = plt.subplots(figsize=(7.5, 2.6))

    # asse reale e intervallo aperto di convergenza
    ax.plot([-1.25, 1.25], [0, 0], color="0.6", lw=1.0, zorder=1)
    ax.plot([-rho, rho], [0, 0], color="tab:blue", lw=3, zorder=2)
    for s in (-1, 1):
        ax.plot(s * rho, 0, "o", ms=8, mfc="white", mec="tab:blue", mew=2, zorder=4)
    ax.text(-rho, -0.16, r"$-\rho$", ha="center", va="top", fontsize=13)
    ax.text(rho, -0.16, r"$\rho$", ha="center", va="top", fontsize=13)
    ax.plot([0, 0], [-0.03, 0.03], color="black", lw=1)
    ax.text(0, -0.16, r"$0$", ha="center", va="top", fontsize=12)

    # compatti annidati [-r_k, r_k]
    colori = ("tab:orange", "tab:green", "tab:red")
    raggi = (0.55, 0.75, 0.92)
    for r, c in zip(raggi, colori):
        parentesi(ax, -r, +1, 0.07, color=c, lw=2, zorder=3)
        parentesi(ax, r, -1, 0.07, color=c, lw=2, zorder=3)
    ax.text(-raggi[0], -0.16, r"$-r$", ha="center", va="top", fontsize=11,
            color=colori[0])
    ax.text(raggi[0], -0.16, r"$r$", ha="center", va="top", fontsize=11,
            color=colori[0])

    # i compatti si allargano verso gli estremi, che non vengono mai presi
    for s in (-1, 1):
        ax.annotate("", xy=(s * 0.97, -0.33), xytext=(s * 0.55, -0.33),
                    arrowprops=dict(arrowstyle="->", color="0.4"))
    ax.text(0, -0.33, "si allargano verso gli estremi", ha="center",
            va="center", fontsize=9, color="0.3")

    # graffa: continuità in ogni compatto
    graffa_orizzontale(ax, -raggi[-1], raggi[-1], 0.11, 0.12, color="0.2", lw=1.2)
    ax.text(0, 0.28, r"$S$ continua in ogni compatto $[-r,r]\subset\,]{-\rho},\rho[$",
            ha="center", va="bottom", fontsize=11)

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-0.45, 0.45)
    ax.set_yticks([])
    ax.set_xticks([])
    for lato in ("left", "right", "top", "bottom"):
        ax.spines[lato].set_visible(False)
    ax.set_xlabel(r"asse reale $x$ (adimensionale)")
    salva(fig, "fig_13")


def main():
    fig_13()


if __name__ == "__main__":
    main()
