import os,io,math,random
from PIL import Image,ImageOps,ImageDraw,ImageFilter
import cairosvg
from html import escape
W,H=1350,1688
rows=[
("01","TÜRKİYE","7. HAFTA: HAKEMLER AÇIKLANDI","9 maçın ataması belli oldu; Reis, Samsun'a rakip dönüyor"),
("02","İNGİLTERE","CITY DOSYASINDA İTİRAZ","100'ü aşkın ihlal kararı; Haaland'dan birlik çağrısı"),
("03","İSPANYA","DEVLER YENİDEN SAHADA","Barcelona–Getafe ve Real Madrid–Villarreal"),
("04","İTALYA","INTER'DE ÜÇ KUPA HEDEFİ","Marotta'dan çalışma vurgusu; Juventus Cagliari yolunda"),
("05","ALMANYA","DORTMUND 4'TE 4'LE LİDER","Bremen karşısında yenilgisiz seriyi korumak istiyor"),
("06","FRANSA","LYON'DA SAKATLIK ALARMI","Ouédraogo'nun çapraz bağı koptu; Tagliafico yok")]
svg=['''<svg xmlns="http://www.w3.org/2000/svg" width="1350" height="1688" viewBox="0 0 1350 1688"><defs>
<radialGradient id="bg"><stop stop-color="#511222"/><stop offset=".6" stop-color="#17141d"/><stop offset="1" stop-color="#080c12"/></radialGradient>
<linearGradient id="silver" x2="0" y2="1"><stop stop-color="#fff"/><stop offset=".6" stop-color="#d6d9df"/><stop offset="1" stop-color="#79838d"/></linearGradient>
<linearGradient id="card"><stop stop-color="#1b1c28"/><stop offset=".65" stop-color="#111820"/><stop offset="1" stop-color="#090d14"/></linearGradient>
<linearGradient id="red"><stop stop-color="#ff4763"/><stop offset=".55" stop-color="#e31839"/><stop offset="1" stop-color="#751127"/></linearGradient>
</defs>
<rect width="1350" height="1688" fill="url(#bg)"/>
<g opacity=".17" stroke="#ee3854" stroke-width="2">''']
for i in range(25):
 x=i*68
 svg.append(f'<path d="M{x} 0 L{x-280} 1688"/>')
for i in range(18):
 y=290+i*85
 svg.append(f'<path d="M0 {y} H1350"/>')
svg.append('''</g><g opacity=".25" stroke="#ff395d" fill="none"><circle cx="1250" cy="90" r="420" stroke-width="6"/><circle cx="1250" cy="90" r="490" stroke-width="2"/><path d="M0 1510 Q675 1250 1350 1510" stroke-width="5"/></g>
<rect x="374" y="56" width="490" height="62" rx="14" fill="url(#red)"/>
<text x="398" y="98" fill="#fff" font-size="31" font-family="DejaVu Sans" font-weight="bold">FUTBOL / GÜNLÜK RAPOR</text>
<text x="366" y="228" fill="url(#silver)" font-size="98" font-family="DejaVu Sans" font-weight="bold">BİR GÜNÜN</text>
<text x="366" y="355" fill="url(#silver)" font-size="151" font-family="DejaVu Sans" font-weight="bold">ÖZETİ</text>
<text x="1015" y="366" fill="#ffd58e" font-size="33" font-family="DejaVu Sans" font-weight="bold">08 EKİM 2026</text>
<path d="M68 392 H1284" stroke="#f02a49" stroke-width="7"/>
<text x="78" y="440" fill="#aeb8c8" font-size="29" font-family="DejaVu Sans">6 LİG  •  TÜRKİYE  •  AVRUPA  •  KUPALAR</text>''')
for i,(no,cat,title,desc) in enumerate(rows):
 y=475+i*172
 svg.append(f'''<rect x="57" y="{y-4}" width="1244" height="160" rx="29" fill="#ff183f" opacity=".25"/>
<rect x="62" y="{y}" width="1232" height="150" rx="25" fill="url(#card)" stroke="#f02c4d" stroke-width="3"/>
<rect x="80" y="{y+22}" width="111" height="103" rx="17" fill="#4a1729"/>
<text x="99" y="{y+89}" fill="#ff3156" font-size="53" font-family="DejaVu Sans" font-weight="bold">{no}</text>
<path d="M218 {y+22} V{y+128}" stroke="#e82b4b" stroke-width="4"/>
<text x="245" y="{y+42}" fill="#ffcf84" font-size="24" font-family="DejaVu Sans" font-weight="bold">{escape(cat)}</text>
<text x="245" y="{y+92}" fill="#f8f9fc" font-size="43" font-family="DejaVu Sans" font-weight="bold">{escape(title)}</text>
<text x="245" y="{y+130}" fill="#b3bfcd" font-size="26" font-family="DejaVu Sans">{escape(desc)}</text>''')
svg.append('''<path d="M70 1536 H1280" stroke="#f02a49" stroke-width="5"/>
<text x="76" y="1590" fill="#fff" font-size="37" font-family="DejaVu Sans" font-weight="bold">BİR GÜNÜN ÖZETİ  |  08.10.2026</text>
<text x="76" y="1643" fill="#adb6c6" font-size="21" font-family="DejaVu Sans">KAYNAKLAR: TFF · AA · REUTERS · JUVENTUS · DPA · LYON</text>
<text x="1054" y="1654" fill="#ffd58e" font-size="24" font-family="DejaVu Sans" font-weight="bold">ZAMAN &amp; ORAN</text></svg>''')
raw=cairosvg.svg2png(bytestring="".join(svg).encode())
im=Image.open(io.BytesIO(raw)).convert("RGBA")
logo=Image.open("images/zamanveoran-onayli-logo.png").convert("RGBA")
logo=ImageOps.contain(logo,(255,255),Image.Resampling.LANCZOS)
im.alpha_composite(logo,(65+(255-logo.width)//2,44+(255-logo.height)//2))
d=ImageDraw.Draw(im)
d.ellipse((64,43,322,301),outline="#f3284c",width=6)
from PIL import ImageFont
f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",29)
d.text((80,308),"@zamanveoran",font=f,fill="#f8f8f8")
os.makedirs("images",exist_ok=True)
out="images/zo-bir-gunun-ozeti-20261008.png"
im.convert("RGB").save(out,optimize=True)
print("FINAL_PNG",out,os.path.getsize(out),im.size)
