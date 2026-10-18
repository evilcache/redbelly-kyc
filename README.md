# KYC and Wallet Activation Explainer

A plain language guide for the Redbelly DAO community. It answers whether you need KYC on Redbelly, how to get verified through Redbelly Access and Averer, and what to do when something goes wrong.

Last verified 18 Oct 2026.

## What is in this repo

| File | What it is |
| --- | --- |
| `index.html` | The guide, Parts A to D, with the source list. Open it in any browser. |
| `assets/decision-guide.png` | Part A decision guide as an image, 1080 x 1080. |
| `pin.md` | Short version for pinning in Discord or Telegram. Post it with the image. |
| `assets/decision-guide.svg` | Same guide as SVG with the DAO logo embedded. |
| `build_assets.py` | Rebuilds the PNG and SVG. Run `./fetch_logos.sh` first. |
| `fetch_logos.sh` | Downloads the DAO logo files from the Task Board brand kit. |

## Run it locally

It is a static page with no build step. Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Regenerate the image

```bash
pip install pillow
./fetch_logos.sh
python3 build_assets.py
```

The script downloads Be Vietnam Pro and JetBrains Mono from GitHub on first run. If a download fails it falls back to a system font.

## Deploy

Vercel: import the repo, set framework to Other, leave the build command empty and the output directory as `.`.

Any static host works. Upload `index.html` and the `assets` folder.

## Keeping it accurate

Facts here can expire. Before relying on the page, recheck the sources listed at the bottom of `index.html`. Items marked unconfirmed in the guide have no official page behind them. Update the date in the page and in the image when you recheck.

## Style rules

The page follows the Task Board brand kit: Be Vietnam Pro for text, JetBrains Mono for machine values, one red accent, no emoji, and no em dashes or en dashes anywhere, including commit messages.
