import urllib.request, os
from PIL import Image, ImageDraw, ImageFont
B="https://raw.githubusercontent.com/google/fonts/main/ofl/"
F={"bold":"bevietnampro/BeVietnamPro-Bold.ttf","semi":"bevietnampro/BeVietnamPro-SemiBold.ttf","reg":"bevietnampro/BeVietnamPro-Regular.ttf","mono":"jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"}
os.makedirs("/tmp/f",exist_ok=True)
def font(k,s):
    p="/tmp/f/"+k+".ttf"
    if not os.path.exists(p):
        try: urllib.request.urlretrieve(B+F[k],p)
        except Exception as e: print("font fail",k,e)
    try: return ImageFont.truetype(p,s)
    except: return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
W=H=1080
im=Image.new("RGB",(W,H),"#0c1317"); d=ImageDraw.Draw(im)
d.text((60,50),"DOCUMENTATION",font=font("bold",20),fill="#ffb3ae")
d.text((60,84),"Do I need KYC on Redbelly?",font=font("bold",56),fill="#f1f5f8")
d.text((60,160),"Native mainnet activity needs KYC. Wrapped RBNT on other chains does not.",font=font("reg",22),fill="#c2ced6")
rows=[("RBNT on an exchange","NOT NEEDED","#86EFAC","The exchange sets its own KYC"),
("Wrapped RBNT on Ethereum or Base","NOT NEEDED","#86EFAC","The token is not on Redbelly"),
("Bridging RBNT to Redbelly mainnet","UNCONFIRMED","#FCD34D","Official pages do not say"),
("Using Redbelly mainnet","NEEDED","#EF5350","Send, swap or deploy"),
("Staking on Redbelly mainnet","NEEDED","#EF5350","Staking is a mainnet transaction")]
y=215
for a,tag,c,why in rows:
    d.rounded_rectangle((60,y,W-60,y+135),radius=8,fill="#141f26",outline="#263641",width=2)
    d.text((90,y+22),a,font=font("semi",30),fill="#f1f5f8")
    d.text((90,y+78),why,font=font("reg",22),fill="#c2ced6")
    f=font("bold",22); tw=d.textlength(tag,font=f)
    x1=W-90; x0=x1-tw-32
    d.rounded_rectangle((x0,y+26,x1,y+68),radius=4,outline=c,width=2)
    d.text((x0+16,y+34),tag,font=f,fill=c)
    y+=151
d.text((60,H-70),"DAO: any region can join. Network: 18 jurisdictions not served (terms, clause 15.1).",font=font("reg",20),fill="#c2ced6")
d.text((60,H-38),"Last verified 16 Oct 2026",font=font("mono",18),fill="#8fa1ad")
im.save("assets/decision-guide.png"); print(im.size)
