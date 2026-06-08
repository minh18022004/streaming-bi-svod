from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
FIG_DIR = Path(__file__).resolve().parents[1] / "figures"

def savefig(plt, name: str, tight=True, dpi=150):
    p = FIG_DIR / f"{name}.png"
    if tight:
        plt.tight_layout()
    plt.savefig(p, dpi=dpi)
    print(f"Saved figure to {p}")
