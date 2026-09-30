"""
figure.py — figure per la dispensa di Analisi Matematica II, lezione 2
(successioni di funzioni: continuità del limite, passaggio al limite
sotto il segno di integrale e sotto il segno di derivata).

Tutte le grandezze sono adimensionali: gli assi non portano unità di misura.
Ogni funzione salva figure/fig_NN.pdf ; il main le genera tutte.
"""

import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

CARTELLA = "figure"


def _salva(fig, nome):
    os.makedirs(CARTELLA, exist_ok=True)
    fig.savefig(os.path.join(CARTELLA, nome + ".pdf"), bbox_inches="tight")
    plt.close(fig)


def fig_01():
    """x^n in [0,1]: successione di funzioni continue con limite discontinuo."""
    x = np.linspace(0.0, 1.0, 2001)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for n in (1, 2, 5, 10, 50):
        ax.plot(x, x ** n, lw=1.3, label=r"$n=%d$" % n)
    ax.plot([0.0, 1.0], [0.0, 0.0], "k--", lw=1.8, label="limite puntuale $f$")
    ax.plot([1.0], [1.0], "ko", ms=6)
    ax.plot([1.0], [0.0], "o", ms=6, mfc="white", mec="k")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_n(x)=x^n$")
    ax.set_title(u"Convergenza puntuale non uniforme in $[0,1]$")
    ax.set_xlim(0.0, 1.05)
    ax.set_ylim(-0.05, 1.1)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)
    _salva(fig, "fig_01")


def fig_02():
    """arctg(nx): limite discontinuo in x = 0."""
    x = np.linspace(-2.0, 2.0, 4001)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for n in (1, 3, 10, 50):
        ax.plot(x, np.arctan(n * x), lw=1.3, label=r"$n=%d$" % n)
    ax.plot([-2.0, 0.0], [-np.pi / 2, -np.pi / 2], "k--", lw=1.8,
            label="limite puntuale $f$")
    ax.plot([0.0, 2.0], [np.pi / 2, np.pi / 2], "k--", lw=1.8)
    ax.plot([0.0], [0.0], "ko", ms=6)
    ax.axvline(0.0, color="0.6", lw=0.8)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_n(x)=\arctan(nx)$")
    ax.set_title(u"Restrizione a $[a,+\\infty[$ con $a>0$ per avere uniformità")
    ax.set_yticks([-np.pi / 2, 0.0, np.pi / 2])
    ax.set_yticklabels([r"$-\pi/2$", r"$0$", r"$\pi/2$"])
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", fontsize=8)
    _salva(fig, "fig_02")


def fig_03():
    """n x (1-x^2)^n in [0,1]: limite nullo ma integrale che tende a 1/2."""
    x = np.linspace(0.0, 1.0, 4001)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for n in (2, 5, 20, 50):
        y = n * x * (1.0 - x ** 2) ** n
        ax.plot(x, y, lw=1.3,
                label=r"$n=%d$, $\int_0^1 f_n=%.3f$" % (n, n / (2.0 * (n + 1))))
    ax.plot([0.0, 1.0], [0.0, 0.0], "k--", lw=1.8, label=r"limite $f\equiv 0$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_n(x)=n\,x\,(1-x^2)^n$")
    ax.set_title(u"Il passaggio al limite sotto il segno di integrale non vale")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    _salva(fig, "fig_03")


def fig_04():
    """n x e^{-n x} in [0,1]: convergenza solo puntuale ma integrale che tende a 0."""
    x = np.linspace(0.0, 1.0, 4001)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for n in (2, 5, 20, 50):
        ax.plot(x, n * x * np.exp(-n * x), lw=1.3, label=r"$n=%d$" % n)
    ax.axhline(1.0 / np.e, color="0.4", ls=":", lw=1.2,
               label=r"massimo $1/e$ (indipendente da $n$)")
    ax.plot([0.0, 1.0], [0.0, 0.0], "k--", lw=1.8, label=r"limite $f\equiv 0$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_n(x)=n\,x\,e^{-nx}$")
    ax.set_title(u"Convergenza non uniforme, ma il passaggio al limite vale")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    _salva(fig, "fig_04")


def fig_05():
    """sqrt(x^2 + 1/n): limite uniforme non derivabile in 0."""
    x = np.linspace(-1.5, 1.5, 4001)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for n in (1, 4, 25, 100):
        ax.plot(x, np.sqrt(x ** 2 + 1.0 / n), lw=1.3, label=r"$n=%d$" % n)
    ax.plot(x, np.abs(x), "k--", lw=1.8, label=r"limite $f(x)=|x|$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_n(x)=\sqrt{x^2+1/n}$")
    ax.set_title(u"Funzioni derivabili con limite uniforme non derivabile")
    ax.set_ylim(-0.1, 1.6)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper center", fontsize=8)
    _salva(fig, "fig_05")


def fig_06():
    """sin(nx)/n e la successione delle derivate cos(nx)."""
    x = np.linspace(-np.pi, np.pi, 4001)
    fig, assi = plt.subplots(1, 2, figsize=(9.5, 3.8))
    for n in (1, 3, 10):
        assi[0].plot(x, np.sin(n * x) / n, lw=1.3, label=r"$n=%d$" % n)
        assi[1].plot(x, np.cos(n * x), lw=1.3, label=r"$n=%d$" % n)
    assi[0].plot([-np.pi, np.pi], [0.0, 0.0], "k--", lw=1.8,
                 label=r"limite $f\equiv 0$")
    assi[1].plot([0.0], [1.0], "ko", ms=6)
    assi[0].set_xlabel(r"$x$")
    assi[0].set_ylabel(r"$f_n(x)=\dfrac{\sin(nx)}{n}$")
    assi[0].set_title(u"Convergenza uniforme a $f\\equiv 0$")
    assi[1].set_xlabel(r"$x$")
    assi[1].set_ylabel(r"$f_n'(x)=\cos(nx)$")
    assi[1].set_title(u"Le derivate non ammettono limite")
    for a in assi:
        a.grid(alpha=0.3)
        a.legend(loc="upper right", fontsize=8)
    _salva(fig, "fig_06")


def fig_07():
    """x/(1+n^2 x^2) e le sue derivate: limite delle derivate non uniforme."""
    x = np.linspace(0.0, 1.0, 4001)
    fig, assi = plt.subplots(1, 2, figsize=(9.5, 3.8))
    for n in (1, 3, 10):
        assi[0].plot(x, x / (1.0 + n ** 2 * x ** 2), lw=1.3, label=r"$n=%d$" % n)
        assi[1].plot(x, (1.0 - n ** 2 * x ** 2) / (1.0 + n ** 2 * x ** 2) ** 2,
                     lw=1.3, label=r"$n=%d$" % n)
    assi[0].plot([0.0, 1.0], [0.0, 0.0], "k--", lw=1.8, label=r"limite $f\equiv 0$")
    assi[1].plot([0.0, 1.0], [0.0, 0.0], "k--", lw=1.8, label="limite puntuale")
    assi[1].plot([0.0], [1.0], "ko", ms=6)
    assi[1].plot([0.0], [0.0], "o", ms=6, mfc="white", mec="k")
    assi[0].set_xlabel(r"$x$")
    assi[0].set_ylabel(r"$f_n(x)=\dfrac{x}{1+n^2x^2}$")
    assi[0].set_title(u"Convergenza uniforme a $f\\equiv 0$")
    assi[1].set_xlabel(r"$x$")
    assi[1].set_ylabel(r"$f_n'(x)=\dfrac{1-n^2x^2}{(1+n^2x^2)^2}$")
    assi[1].set_title(u"Le derivate convergono solo puntualmente")
    for a in assi:
        a.grid(alpha=0.3)
        a.legend(loc="upper right", fontsize=8)
    _salva(fig, "fig_07")


def fig_08():
    """Esercizio degli appunti: arctg(m(1+x^2))/(1+m^2x^2) + x in [0,+infinito[."""
    x = np.linspace(0.0, 3.0, 4001)
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for m in (1, 3, 10, 50):
        y = np.arctan(m * (1.0 + x ** 2)) / (1.0 + m ** 2 * x ** 2) + x
        ax.plot(x, y, lw=1.3, label=r"$m=%d$" % m)
    ax.plot(x[x > 0.0], x[x > 0.0], "k--", lw=1.8, label=r"limite $f(x)=x$")
    ax.plot([0.0], [np.pi / 2], "ko", ms=6)
    ax.plot([0.0], [0.0], "o", ms=6, mfc="white", mec="k")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f_m(x)$")
    ax.set_title(u"Limite discontinuo in $x=0$: niente uniformità in $[0,+\\infty[$")
    ax.set_xlim(-0.05, 3.0)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)
    _salva(fig, "fig_08")

def fig_09():
    """Schema delle implicazioni fra i quattro tipi di convergenza."""
    fig, ax = plt.subplots(figsize=(6.4, 2.8))
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)

    nodi = {
        "TOTALE": (1.4, 2.5),
        "ASSOLUTA": (5.0, 4.0),
        "UNIFORME": (5.0, 1.0),
        "PUNTUALE": (8.6, 2.5),
    }
    stile = dict(
        ha="center",
        va="center",
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.25", lw=1.0),
    )
    for testo, (x, y) in nodi.items():
        ax.text(x, y, testo, **stile)

    frecce = [
        ("TOTALE", "ASSOLUTA"),
        ("ASSOLUTA", "PUNTUALE"),
        ("TOTALE", "UNIFORME"),
        ("UNIFORME", "PUNTUALE"),
    ]
    for a, b in frecce:
        ax.add_patch(
            FancyArrowPatch(
                nodi[a],
                nodi[b],
                arrowstyle="-|>",
                mutation_scale=12,
                lw=1.1,
                color="0.25",
                shrinkA=32,
                shrinkB=32,
            )
        )

    ax.add_patch(
        FancyArrowPatch(
            (5.0, 3.5),
            (5.0, 1.5),
            arrowstyle="<|-|>",
            mutation_scale=12,
            lw=1.0,
            ls="--",
            color="C3",
            shrinkA=4,
            shrinkB=4,
        )
    )
    ax.plot([4.75, 5.25], [2.35, 2.65], color="C3", lw=1.4)
    ax.plot([4.75, 5.25], [2.65, 2.35], color="C3", lw=1.4)
    ax.text(5.45, 2.5, "nessun legame", color="C3", fontsize=8.5, va="center")
    ax.text(
        5.0,
        0.1,
        "il criterio di Weierstrass è la freccia TOTALE $\\Rightarrow$ UNIFORME",
        ha="center",
        fontsize=8.5,
        color="0.3",
    )
    _salva(fig, "fig_09")

def main():
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    fig_08()
    fig_09()


if __name__ == "__main__":
    main()
