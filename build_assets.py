"""Builds assets/decision-guide.png and assets/decision-guide.svg with the DAO logo.
Run fetch_logos.sh first so assets/dao-logo-on-dark.png exists."""
import os, base64, urllib.request
from PIL import Image, ImageDraw, ImageFont
B = "https://raw.githubusercontent.com/google/fonts/main/ofl/"
F = {"bold": "bevietnampro/BeVietnamPro-Bold.ttf", "semi": "bevietnampro/BeVietnamPro-SemiBold.ttf",
     "reg": "bevietnampro/BeVietnamPro-Regular.ttf", "mono": "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"}
os.makedirs("/tmp/f", exist_ok=True)
def font(k, s):
    p = "/tmp/f/" + k + ".ttf"
    if not os.path.exists(p):
        try: urllib.request.urlretrieve(B + F[k], p)
        except Exception as e: print("font download failed", k, e)
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", s)

LOGO = "assets/dao-logo-on-dark.png"
if not os.path.exists(LOGO): raise SystemExit("Missing " + LOGO + ". Run ./fetch_logos.sh first.")
logo = Image.open(LOGO).convert("RGBA")
LH = 110                                   # scale by height, width follows
logo = logo.resize((round(logo.width * LH / logo.height), LH), Image.LANCZOS)

W = H = 1080
DATE = "Last verified 18 Oct 2026"
TITLE = "Do I need KYC on Redbelly?"
SUB = "Native mainnet activity needs KYC. Wrapped RBNT on other chains does not."
FOOT = "DAO: any region can join. Network: 18 jurisdictions not served (terms, clause 15.1)."
rows = [("RBNT on an exchange", "NOT NEEDED", "#86EFAC", "The exchange sets its own KYC"),
        ("Wrapped RBNT on Ethereum or Base", "NOT NEEDED", "#86EFAC", "The token is not on Redbelly"),
        ("Bridging RBNT onto Redbelly mainnet", "NEEDED", "#EF5350", "Verify and enable first, then bridge"),
        ("Using Redbelly mainnet", "NEEDED", "#EF5350", "Send, swap or deploy"),
        ("Staking on Redbelly mainnet", "NEEDED", "#EF5350", "Staking is a mainnet transaction")]

im = Image.new("RGB", (W, H), "#0c1317"); d = ImageDraw.Draw(im)
im.paste(logo, (W - 60 - logo.width, 40), logo)
d.text((60, 50), "DOCUMENTATION", font=font("bold", 20), fill="#ffb3ae")
d.text((60, 84), TITLE, font=font("bold", 52), fill="#f1f5f8")
d.text((60, 160), SUB, font=font("reg", 22), fill="#c2ced6")
y = 215
for a, tag, c, why in rows:
    d.rounded_rectangle((60, y, W - 60, y + 135), radius=8, fill="#141f26", outline="#263641", width=2)
    d.text((90, y + 22), a, font=font("semi", 30), fill="#f1f5f8")
    d.text((90, y + 78), why, font=font("reg", 22), fill="#c2ced6")
    f = font("bold", 22); tw = d.textlength(tag, font=f); x1 = W - 90; x0 = x1 - tw - 32
    d.rounded_rectangle((x0, y + 26, x1, y + 68), radius=4, outline=c, width=2)
    d.text((x0 + 16, y + 34), tag, font=f, fill=c)
    y += 151
d.text((60, H - 70), FOOT, font=font("reg", 20), fill="#c2ced6")
d.text((60, H - 38), DATE, font=font("mono", 18), fill="#8fa1ad")
im.save("assets/decision-guide.png"); print("png", im.size)

# SVG with the logo embedded. Text uses the brand fonts with system fallbacks.
b64 = base64.b64encode(open(LOGO, "rb").read()).decode()
lw = round(logo.width)
s = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
     '<style>.t{font-family:"Be Vietnam Pro",system-ui,sans-serif}.m{font-family:"JetBrains Mono",ui-monospace,monospace}</style>',
     f'<rect width="{W}" height="{H}" fill="#0c1317"/>',
     f'<image x="{W-60-lw}" y="40" width="{lw}" height="{LH}" xlink:href="data:image/png;base64,{b64}"/>',
     '<text class="t" x="60" y="68" font-size="20" font-weight="700" fill="#ffb3ae" letter-spacing="2">DOCUMENTATION</text>',
     f'<text class="t" x="60" y="130" font-size="52" font-weight="700" fill="#f1f5f8">{TITLE}</text>',
     f'<text class="t" x="60" y="178" font-size="22" fill="#c2ced6">{SUB}</text>']
y = 215
for a, tag, c, why in rows:
    tw = len(tag) * 14 + 32
    s += [f'<rect x="60" y="{y}" width="{W-120}" height="135" rx="8" fill="#141f26" stroke="#263641" stroke-width="2"/>',
          f'<text class="t" x="90" y="{y+55}" font-size="30" font-weight="600" fill="#f1f5f8">{a}</text>',
          f'<text class="t" x="90" y="{y+100}" font-size="22" fill="#c2ced6">{why}</text>',
          f'<rect x="{W-90-tw}" y="{y+26}" width="{tw}" height="42" rx="4" fill="none" stroke="{c}" stroke-width="2"/>',
          f'<text class="t" x="{W-90-tw/2}" y="{y+55}" font-size="22" font-weight="700" fill="{c}" text-anchor="middle">{tag}</text>']
    y += 151
s += [f'<text class="t" x="60" y="{H-52}" font-size="20" fill="#c2ced6">{FOOT}</text>',
      f'<text class="m" x="60" y="{H-24}" font-size="18" fill="#8fa1ad">{DATE}</text>', '</svg>']
open("assets/decision-guide.svg", "w", encoding="utf-8").write("\n".join(s)); print("svg ok")
