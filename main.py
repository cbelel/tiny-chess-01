import json,os,urllib.request as u
E=os.environ.get("MAKEFUN_ENV_URL","")
V=[0,100,320,330,500,900,0]
T=bytes.fromhex("b2b2b2b2b2b2b2b28a8a949e9e948a8a85858a99998a85858080809494808080857b768080767b85858a8a6ec26e8a8a8080")
def F(f):
 p=f.split();a=[0]*128;r=c=0
 for ch in p[0]:
  if ch=='/':r+=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:q="PNBRQKpnbrqk".index(ch);a[r*16+c]=(q%6+1)*(1-2*(q>5));c+=1
 return a,1 if p[1]=='w' else -1
def A(x,q,y):
 for d in(1,-1,16,-16,15,17,-15,-17):
  t=q+d
  while not t&136:
   v=x[t]
   if v:
    if v*y>0 and(abs(v)==5 or(abs(v)==4 and d in(1,-1,16,-16))or(abs(v)==3 and d in(15,17,-15,-17))or(abs(v)==6 and abs(t-q) in(1,15,16,17))):return 1
    break
   t+=d
 for d in(31,33,14,18,-31,-33,-14,-18):
  t=q+d
  if not t&136 and x[t]*y>0 and abs(x[t])==2:return 1
 d=16*y
 for t in(q+d-1,q+d+1):
  if not t&136 and x[t]==y:return 1
 return 0
def G(x,s):
 m=[]
 for f in range(128):
  if f&136:continue
  p=x[f]
  if p*s<=0:continue
  a=abs(p)
  if a==1:
   d=-16*s
   for t in(f+d,f+2*d):
    if t&136 or x[t]:break
    if t==f+2*d and(f>>4)!=(7+5*s)//2:break
    m.append((f,t,0))
    if t==f+2*d:break
   for t in(f+d-1,f+d+1):
    if t&136:continue
    if x[t]*s<0:
     pr=5 if(t>>4)==(7-7*s)//2 else 0
     if pr:
      for q in(2,3,4,5):m.append((f,t,q))
     else:m.append((f,t,0))
  elif a in(2,6):
   for d in{2:(31,33,14,18,-31,-33,-14,-18),6:(1,-1,16,-16,15,17,-15,-17)}[a]:
    t=f+d
    if not t&136 and x[t]*s<=0:m.append((f,t,0))
  elif a in(3,4,5):
   D={3:(15,17,-15,-17),4:(1,-1,16,-16),5:(1,-1,16,-16,15,17,-15,-17)}[a]
   for d in D:
    t=f+d
    while not t&136:
     if x[t]*s>0:break
     m.append((f,t,0))
     if x[t]:break
     t+=d
 return m
def m(x,v,s):
 f,t,pr=v;pc=x[f];cp=x[t];x[t]=pr*s if pr else pc;x[f]=0;rf=rt=-1
 if abs(pc)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);x[rt]=x[rf];x[rf]=0
 return (f,t,pr,pc,cp,rf,rt)
def n(x,z):
 f,t,pr,pc,cp,rf,rt=z;x[f]=pc;x[t]=0
 if cp:x[t]=cp
 if rf>=0:x[rf]=x[rt];x[rt]=0
def e(x,s):
 z=sum((V[abs(p)]+(T[(7-(i>>4)if p<0 else i>>4)*8+(i&7)-8]-128 if abs(p)==1 else 0)*(1 if p>0 else -1)for i in range(128)if not i&136 and(p:=x[i])))
 return z if s>0 else -z
N=[0];L=100000
def O(x,m):
 return sorted(m,key=lambda v:V[abs(x[v[1]])]*10-V[abs(x[v[0]])]if x[v[1]] else 0,reverse=True)
def K(x,s):
 for i in range(128):
  if not i&136 and x[i]==6*s:return i
 return -1
def Q(x,s,a,be,pl):
 N[0]+=1
 if N[0]>L:return 0
 k=K(x,s);ic=k>=0 and A(x,k,-s)
 if not ic:
  st=e(x,s)
  if st>=be:return be
  if st>a:a=st
 for v in G(x,s):
  f,t,pr=v
  if not ic and not x[t]:continue
  z=m(x,v,s);k=K(x,s)
  if k>=0 and A(x,k,-s):n(x,z);continue
  sc=-Q(x,-s,-be,-a,pl+1);n(x,z)
  if N[0]>L:return 0
  if sc>=be:return be
  if sc>a:a=sc
 if ic and a==-10**9:return-100000+pl
 return a
def S(x,s,d,a,be,pl):
 N[0]+=1
 if N[0]>L:return 0
 if d<=0:return Q(x,s,a,be,pl)
 bs=-10**9
 for v in O(x,G(x,s)):
  if N[0]>L:return 0
  z=m(x,v,s);k=K(x,s)
  if k>=0 and A(x,k,-s):n(x,z);continue
  sc=-S(x,-s,d-1,-be,-a,pl+1);n(x,z)
  if N[0]>L:return 0
  if sc>bs:bs=sc
  if sc>a:a=sc
  if a>=be:break
 if bs==-10**9:
  k=K(x,s)
  return-100000+pl if k>=0 and A(x,k,-s) else 0
 return bs
def U(v):
 f,t,pr=v;return chr(97+(f&7))+str(8-(f>>4))+chr(97+(t&7))+str(8-(t>>4))+("nbrq"[pr-2]if pr else"")
def D(u):
 return(ord(u[0])-97+(8-int(u[1]))*16,ord(u[2])-97+(8-int(u[3]))*16,"nbrq".index(u[4])+2 if len(u)>4 else 0)
def C(fen,lg):
 x,s=F(fen);N[0]=0;bm=D(lg[0]);lm=O(x,[D(u) for u in lg])
 for d in range(1,12):
  if N[0]>L:break
  cb=None;cs=-10**9
  for v in lm:
   if N[0]>L:break
   z=m(x,v,s);k=K(x,s)
   if k>=0 and A(x,k,-s):n(x,z);continue
   sc=-S(x,-s,d-1,-10**9,-cs,1);n(x,z)
   if sc>cs:cs=sc;cb=v
  if cb and N[0]<=L:bm=cb
 return U(bm)
def P(p,b):
 q=u.Request(E+p,data=json.dumps(b).encode(),headers={"Content-Type":"application/json"})
 return json.loads(u.urlopen(q).read())
def main():
 while 1:
  d=P("/game",{});g=d["game"]
  if d["status"]!="your_move":break
  mv=C(d["fen"],d["legal_moves"])
  r=P("/move",{"game":g,"move":mv})
  if r["status"]=="done":break
main()
