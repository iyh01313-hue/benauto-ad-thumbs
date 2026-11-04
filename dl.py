import sys,io,requests
from PIL import Image
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.strip()
    if not line: continue
    i,u=line.split(' ',1)
    r=requests.get(u,timeout=30,headers={'User-Agent':'Mozilla/5.0'})
    im=Image.open(io.BytesIO(r.content)).convert('RGB')
    im.thumbnail((360,360))
    im.save(f'thumbs/{i}.jpg',quality=82)
    print(i,r.status_code,im.size)
