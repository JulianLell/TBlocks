#Terminal Blocks by Julian A. Lell / Jan-Feb 2024
import time,sys,termios,tty,select
aa = [255,240] + [128, 16]*24
def ab(aa,X,Y,ai):
 if X>=-1:
  ac=(aa[2*(Y+2)]&127)*256+aa[2*(Y+2)+1]>>5
  ad=(aa[2*Y]&127)*256+aa[2*Y+1]>>5
  ae=bool((ac>>X+1)%2)
  af=bool((ad>>X+1)%2)
  ag=bool((ac>>X+3)%2)
  ah=bool((ad>>X+3)%2)
  if ai==0:return ag&ae&(ah|af)
  elif ai==1:return ae&af&(ag|ah)
  elif ai==2:return ah&af&(ag|ae)
  else:return ag&ah&(ae|af)
 else:return False
aj = [[[[-1,0],[-1,1],[0,-2],[-1,-2]],[[1,0],[1,1],[0,-2],[1,-2]]],
         [[[1,0],[1,-1],[0,2],[1,2]],[[1,0],[1,-1],[0,2],[1,2]]],
        [[[1,0],[1,1],[0,-2],[1,-2]],[[-1,0],[-1,1],[0,-2],[-1,-2]]],
        [[[-1,0],[-1,-1],[0,-2],[-1,2]],[[-1,0],[-1,-1],[0,2],[-1,2]]]]
ak = [[[[-2,0],[1,0],[-2,-1],[1,2]],[[-1,0],[2,0],[-1,2],[2,-1]]],
         [[[-1,0],[2,0],[-1,2],[2,-1]],[[2,0],[-1,0],[2,1],[-1,-2]]],
        [[[2,0],[-1,0],[2,1],[-1,-2]],[[1,0],[-2,0],[1,-2],[-2,1]]],
        [[[1,0],[-2,0],[1,-2],[-2,1]],[[-2,0],[1,0],[-2,-1],[1,2]]]]
def al():
 if select.select([sys.stdin],[],[],0)==([sys.stdin],[],[]):
  return sys.stdin.read(1)
 else: return None
def am(an, ai):
 ao = [0,15,0,0,4,4,4,4,0,0,15,0,2,2,2,2,0,14,2,0,6,4,4,0,8,14,0,0,4,4,12,0,
       0,14,8,0,4,4,6,0,2,14,0,0,12,4,4,0,0,6,6,0,0,6,6,0,0,6,6,0,0,6,6,0,
       0,6,12,0,4,6,2,0,6,12,0,0,8,12,4,0,0,14,4,0,4,6,4,0,4,14,0,0,4,12,4,
       0,0,12,6,0,2,6,4,0,12,6,0,0,4,12,8,0]
 ap = an*16+ai*4
 return ao[ap:ap+4]
def aq(n):
 ar=str(time.perf_counter())
 return int(ar[::-1][:3])%n
def cw(bag):
 elementos=[0,1,2,3,4,5,6]
 while elementos!=[]:
  random_result=aq(len(elementos))
  bag.append(elementos.pop(random_result))
 return bag
def aa_p_ao(aa,cm,ai,X,Y):
 aa_=list(aa)
 for i in range(Y,Y+4):
  aa_[2*i+1]|=(cm[i-Y]<<(5+X))%256
  if X>=0:aa_[2*i]|=((cm[i-Y]<<X)>>3)%256
  else:aa_[2*i]|=(cm[i-Y]>>-X+3)%256
 return aa_
def au(at):
 aw = ' '*8
 for i in range(5):
  j=at[i];aoro=am(j,0)
  for k in range(2,-1,-1):
   av='{0:04b}'.format(aoro[k])
   if j==0:
    if k==2:av = ' '*8
    if k==1:av=u'\u2593'*8
   elif j==3:
    if k==1 or k==2: av='  '+u'\u2593'*4+'  '
   elif j!=0 and j!=3:
    if k==2 or k==1:
     av=av[0].replace('1',' '+u'\u2593'*2).replace('0','   ')+av[1:-1].replace('0','  ').replace('1',u'\u2593'*2)+' '
   if k==0:av=' '*8
   aw += av
 return aw
def ax(j):
 aw=' '*8
 aoro=am(j,0)
 for k in range(2,-1,-1):
  av = '{0:04b}'.format(aoro[k])
  if j==0:
   if k==2:av='        '
   if k==1:av=u'\u2593'*8
  elif j==3:
   if k==1 or k==2:av='  '+u'\u2593'*4+'  '
  elif j!=0 and j!=3:
   if k==2 or k==1:
    av=av[0].replace('1',' '+u'\u2593'*2).replace('0','   ')+av[1:-1].replace('0','  ').replace('1',u'\u2593'*2)+' '
  if k==0:av=' '*8
  aw+=av
 return aw
def ay(j,ai):
 aw='';aoro=am(j,ai)
 for k in range(3,-1,-1):aw+='{0:04b}'.format(aoro[k])
 return aw
def az(aa, ai):
 global Y,X,ba,bb,bc,bd,aw,be,bf,at,bg,j,cq,bh,bi
 bi=True;bj=1
 if Y>18:bk=range(Y,18,-1)
 elif Y<18:bk=range(Y,18)
 elif Y==18:bk=[Y]
 for Y in bk:
  for X in range(X, 12):
   bf=ay(j, ai);br(aa);time.sleep(0.02)
 bi = False
def br(aa):
 global ba,bb,bc,bd,aw,be,bf,at,bg,j,cq,bh,bi,bl,bm
 bo=['\033[36;48m','\033[33;48m','\033[34;48m','\033[1;33;48m','\033[31;48m','\033[35;48m','\033[32;48m']
 bp='\033[0m'
 bq = '===HOLD:====S:'+str(ba)+'========='[:-len(str(ba))]+'L:'+str(bb)+'=========='[:-len(str(bb))]+'NEXT:==\n'
 bq+=' '*11+u'\u2584'*22+'\n'
 for i in range(20,16,-1):
  bq_=('{0:08b}'.format(aa[2*i]))[1:]+('{0:08b}'.format(aa[2*i+1]))[:3]
  bq_=bq_.replace('1',u'\u2588'u'\u2588').replace('0','  ')+u'\u258F'+' '+bo[at[int((20-i)/3)]]+aw[160-i*8:168-i*8]+bp+'\n'
  bq+='  '+ bo[bg]+be[160-i*8:168-i*8]+bp+' '+u'\u2595'+bq_
 for i in range(16,0,-1):
  bq_=' '*11+u'\u2595'+('{0:08b}'.format(aa[2*i]))[1:]+('{0:08b}'.format(aa[2*i+1]))[:3]
  bq_=bq_.replace('1',u'\u2588'u'\u2588').replace('0','  ')+u'\u258F'+' '+ bo[at[int((20-i)/3)]]+aw[160-i*8:168-i*8]+bp+'\n'
  bq+=bq_
 bq+=' '*11+u'\u2580'*22+'\n'+bh+'\n J.LELL===============================2024'
 if bm>=1:bq+='\033[7;H'+' '+u'\u2605'+'COMBO X'+str(bm)
 bq+='\033[8;H'+' '+'LEVEL:'+str(bl);bn = '\033[C'*2*(12-X)
 if bi == False:
  bq='\033[2J\033[H' + bq
  bq+='\033['+str(21-cq)+';H'
  for i in range(3,-1,-1):
   if 16-cq+i>0:
    bq += bn+bo[j]+bf[i*4:4+i*4].replace('0','\033[C'*2).replace('1',u'\u2591'*2)+bp+'\033[F'
 else:bq='\033[2J\033[H'+bq+'\033[F';bn+='\033[C'
 bq += '\033['+str(23-Y)+';H'
 for i in range(3,-1,-1):
  if 18-Y+i>0:
   bq += bn+bo[j]+bf[i*4:4+i*4].replace('0','\033[C'*2).replace('1',u'\u2588'*2)+bp+'\033[F'
 bq+='\033[24;H'
 termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_settings)
 print(bq)
 tty.setraw(sys.stdin.fileno())
def bs(bt):
 l2er=len(bt);delay=0.015/l2er
 for j in range(l2er):
  termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_settings)
  print('\033['+str(23-bt[j])+';H'+'\033[C'*(12),end='')
  tty.setraw(sys.stdin.fileno());sys.stdout.flush()
  for i in range(19):
   termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_settings)
   print(' ',end='')
   tty.setraw(sys.stdin.fileno());sys.stdout.flush();time.sleep(delay)
 time.sleep(0.01)
 return
def bu(Y,aa,cm,ai):
 bt=[]
 for i in range(4):
  if cm[i]!=0:
   if ((aa[(Y+i)*2]&127)==127) and ((aa[(Y+i)*2+1]&224)==224):
    bt.append(Y+i)
 return bt
def bv(bt,aa):
 bx=bt+[20];bw=0
 for j in range(len(bx)-1):
  for i in range(bx[j]-bw,bx[j+1]-1):
   aa[i*2]=aa[(i+bw+1)*2];aa[i*2+1]=aa[(i+bw+1)*2+1]
  bw+=1
 return aa
def by(aa,bz,bt,ba,bb,ca,cb):
 global ce,bl,bm
 cc=0;cd=[1,3,5,8,12,18,20]
 bqcw=len(bt);bb+=bqcw
 if bz:
  btb_mult =1+0.5*int(ce);ca=False;cb=True
  cc+=int(bqcw*400*btb_mult)
 else:
  clear_bq = ((aa[2]%127)<<3)+((aa[3]%224)>>5)
  if clear_bq!=0:cc+=cd[bqcw-1]*100
  else:cc+=cd[bqcw+2]*100
  if ce==True and bqcw==4:cc+=1200
  ca=(bqcw==4);cb=False
 if bm>=1:cc+=50*bm
 if bl>1:cc*=min(bl,20)
 bl=int(bb/10);tau=max(int(50-46*bl/29),4);ba+=cc
 return ba,bb,ca,cb,tau
def cf(aa,cm,X,Y):
 cn=False
 for i in range(Y,Y+4):
  if aa[2*i+1]&((cm[i-Y]<<(5+X))%256)!=0:
   cn=True
   return cn
  if X>=0:
   if aa[2*i]&(int((cm[i-Y]<<X)>>3)%256)!=0:cn=True
  else:
   if aa[2*i]&(int(cm[i-Y]>>-X+3)%256)!=0:cn=True
 return cn
def cg(aa,cm,X,Y):
 cl=False;i=0
 while cl==False:i+=1;cl=cf(aa,cm,X,Y-i)
 return Y-i-1
def ch(aa, ci, j, ai, X, Y, cj, ck):
 ai_=(ai+ci)%4;cm=am(j,ai_)
 cl=cf(aa,cm,X,Y)
 if cl==True:
  if j==0:test_mov=ak
  else:test_mov=aj
  if ci==1:rot_index=0
  else:rot_index=1
  for i in range(4):
   X_t=X-test_mov[ai][rot_index][i][0]
   Y_t=Y+test_mov[ai][rot_index][i][1]
   cl=cf(aa,cm,X_t,Y_t)
   if cl==False:
    cj=True;ck=True
    return cm,ai_,X_t,Y_t,cj,ck
 else:
  cj=True;ck=False
  return cm,ai_,X,Y,cj,ck
 cm=am(j,ai)
 return cm,ai,X,Y,cj,ck
old_settings=termios.tcgetattr(sys.stdin);tty.setraw(sys.stdin.fileno())
X=3; Y=21;ai=0;cl=0;j=0;cr=0;tau=50
co='';ba=0;ca=False;bb=0;bc=False;bd=False
cb=False; bz = False; cj = False; ck = False
ce = False; bg_empty = True; be_enable = False; bg = 0
be = ' '*32;bh = ''
already_soft=False;cp=False;bi=False;bm=-1;bl=0;at=[]
at=cw(at);at=cw(at);j=at.pop(0);aw=au(at)
cm=am(j,ai);bf=ay(j, ai)
cq=cg(aa,cm,X,Y);br(aa)
while True:
 co=al()
 if cp==False:time.sleep(0.005)
 cp=False
 if bc==False and bd==False:cr+=0.4
 if int(cr)>=tau:
  cr=0;Y-=1;cl=cf(aa,cm,X,Y);already_soft=False
  if cl!=0:
   Y+=1;aa=aa_p_ao(aa,cm,ai,X,Y)
   if aa[42]!=128 or aa[43]!=16:
    bd=True;bh=' '*9+'GAME OVER / CONTINUE?(Y/N)'
    bf=ay(j,ai)
    cq=cg(aa,cm,X,Y);br(aa);continue
   if j==5 and cj==True:
    bz=ab(aa,X,Y,ai)
    if bz:bh=' '*19+'-T*SPIN-';ba+=400*min(bl,1)
   else:bz=False
   cs=bu(Y,aa,cm, ai)
   if cs!=[]:
    bm+=1;ce=False
    if ca or cb:ce=True
    ct=len(cs)
    if bz==False:
     bh=' '*18
     if ct==1:bh+='  -LINE-'
     elif ct==2:bh+=' -DOUBLE-'
     elif ct==3:bh+=' -TRIPLE-'
     elif ct==4:
      if ce:bh+='-B2B QUAD-'
      else:bh+='  -QUAD-'
    else:
     bh =' '*15
     if ce:bh+='-B2B T*SPIN '
     else:bh+=' -T*SPIN '
     if ct==1:bh+='SIMPLE-'
     elif ct==2:bh+='DOUBLE-'
     elif ct==3:bh+='TRIPLE-'
    bs(cs)
    ba,bb,ca,cb,tau=by(aa,bz,cs,ba,bb,ca,cb)
    aa=bv(cs,aa)
   else:
    bm=-1
    if bz and ck:cb=True
    if bz==False:bh=''
   Y=21;X=3;ai=0;cr=40;be_enable=True
   if len(at)>7:j=at.pop(0);aw=au(at)
   else:at=cw(at);j=at.pop(0);aw=au(at)
   cm=am(j,ai)
  bf=ay(j,ai);cq=cg(aa,cm,X,Y);br(aa)
 if co!=None:
  if bd==True:
   if co.lower()=='y':
    bh = '';aa=[255,240]+[128,16]*24
    bg_empty=True;be_enable=False;be=' '*32
    X=3; Y=21;ai=0;cl=0;j=0;cr=0;tau=50;bl=0;bm=-1
    co='';ba=0;ca=False;bb=0;bc=False;bd=False
    at =[];at=cw(at);at=cw(at);j=at.pop(0)
    aw = au(at);cm=am(j,ai)
    bf=ay(j,ai);br(aa)
    continue
   if co.lower()=='n':
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings);exit()
  if co.lower()=='q':
   termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_settings);exit()
  if co.lower()=='p':
   bc=not bc
   if bc==True:bh=' '*19+'-PAUSE-'
   else:bh=''
   bf=ay(j,ai);br(aa)
   continue
  if bc==False and bd==False:
    if co.lower()=='a':
     ci=-1
     cm,ai,X,Y,cj,ck=ch(aa,ci,j,ai,X,Y,cj,ck)
     bf=ay(j, ai)
     cq=cg(aa,cm,X,Y);br(aa)
     continue
    if co.lower()=='s':
     ci=1
     cm,ai,X,Y,cj,ck=ch(aa,ci,j,ai,X,Y,cj,ck)
     bf=ay(j,ai)
     cq = cg(aa,cm,X,Y);br(aa)
     continue
    if co.lower()=='z':
     if bg_empty==True:
      az(aa,ai);bg_empty=False;bg=j
      Y=21;X=3;ai=0;cr=40
      if len(at)>7:j=at.pop(0);aw=au(at)
      else:at=cw(at);j=at.pop(0);aw=au(at)
      cm=am(j,ai)
      be=ax(bg)+be[len(ax(bg)):]
      bf=ay(j,ai);br(aa)
      continue
     else:
      if be_enable==True and bg!=j:
       az(aa,ai);be_enable=False
       bg,j=j,bg;Y=21;X=3;ai=0;cr=40
       cm=am(j,ai)
       be=ax(bg)+be[len(ax(bg)):]
       bf=ay(j,ai);br(aa)
    if co.lower()=='j':
     if X<=10:
      X+=1;cl=cf(aa,cm,X,Y)
      if cl!=0:X-=1
      else:
       cj=False;ck=False
       bf=ay(j,ai)
       cq=cg(aa,cm,X,Y);br(aa)
       continue
    if co.lower()=='l':
     X-=1;cl=cf(aa,cm,X,Y)
     if cl!=0:X+=1
     else:
      cj=False;ck=False
      bf=ay(j,ai)
      cq=cg(aa,cm,X,Y);br(aa)
      continue
    if co.lower()=='k' and already_soft==False:
     Y-=1;cl = cf(aa,cm,X,Y)
     if cl!=0:
      already_soft=True;Y+=1;cr=15;cv=time.time()
      while (time.time()-cv)<0.1:cu=al()
     else:
      ba+=min(bl,1);cj=False;ck=False
      bf=ay(j,ai);br(aa)
    if co.lower()=='m':
     ba+=2*(Y-cq-2)*min(bl,1);Y=cq+2;cp=True;cr=tau
     bf=ay(j,ai);br(aa);cv=time.time()
     while (time.time()-cv)<0.1:cu=al()
exit()
