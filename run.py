#!/usr/bin/python
# coding:utf-8
import requests
import re
import time
char = 'zzv,bkk,eer,eii,hff,iuu,kkq,ouu,rre,see,ssh,urr,uub,uyy,vxx,vzz,xnn,xpp,xxt,bzb,eie,iei,jfj,nhn,qeq,uau,ueu,vav,vnv,vxv,yiy,zvt,ahq,any,api,but,cla,dsr,efq,exn,exv,eyh,ezj,faj,gzs,idv,ifr,ihy,ilt,iro,izl,jkt,jxq,kbx,lab,lpo,man,mxq,naq,nhj,oia,oxl,qad,qcb,qfg,qfv,qje,qkj,qkr,qmj,qxa,raw,rem,sfv,suw,tqo,unw,upk,uqy,vfj,vhw,vqj,vqk,vqz,vxj,wef,wek,weu,wev,wiq,xnq,xoy,xvh,xvl,yqv,yvq,zdq,zq0,zq2,zq6,zq8,zq9,zr3,zr5,zr6,zs4,zt6,zu3,zu6,zu8,zu9,zv0,zv2,zv4,zv7,zv8,zw0,zw5,zw7,zw9,zy8,aa2,aa5,aa9,ad5,am1,ao6,aq0,aq3,aq4,aq6,aq7,aq8,au5,ax5,ay6,ay7,ay8,az5,az9,bh3,bi9,bj6,bl5,bn6,bo5,bp8,bq3,bq6,bq8,br6,bu5,bu7,bu8,bv0,bv3,bw5,bw8,bx5,bx6,bx9,by5,by8,bz6,bz7,bz8,ca6,cc6,ce6,ce9,cg2,cg4,ch1,ch6,ci6,co0,co4,co5,co7,cp7,cq0,cq4,cq7,cq8,cu4,cu6,cu9,cw5,cw6,cx6,cz3,cz4,cz5,dd7,df5,dq5,dq8,du5,du9,dw5,ea2,ea3,eb6,ec6,ef1,ef2,ef5,eg5,eg6,eh6,eh9,ei0,ei3,ei4,ei5,ei6,ei9,ej5,ej6,ek2,ek5,ek6,el9,en6,en7,en9,eo6,eo8,eo9,ep6,ep8,ep9,eq7,eq9,et6,eu3,eu5,eu6,eu7,eu9,ev6,ev7,ew7,ey0,ey2,ey5,ey7,ey9,ez7,fa5,fa6,fb6,fb8,fc5,fc9,fe3,fe8,fg4,fh5,fh9,fj6,fk6,fk8,fl6,fn4,fn5,fn6,fn8,fo6,fo7,fo8,fo9,fp2,fp6,fp8,fq0,fq3,fq4,fq5,fq6,fq7,fq8,fq9,fs4,ft6,ft7,fu0,fu1,fu2,fu3,fu4,fu5,fu6,fu8,fv2,fx1,fx6,fy4,fy7,fy8,fz5,fz8,ga5,ga9,gc9,gd5,gf0,gh5,gh9,gi7,gj5,gj9,gn1,gn5,gn6,gq3,gq6,gq7,gq8,gq9,gv4,gv5,gv7,gw5,gx0,gy4,gy6,gz4,gz8,hd8,he6,hf5,hf6,hj4,hj9,hl0,hl6,hn4,ho4,ho5,hp6,hp9,hq2,hq3,hq4,hq8,ht8,hv0,hv2,hv6,hv7,hv9,hw8,hw9,hx6,hy2,hy4,hy6,hz0,hz5,hz6,hz8,ia8,ia9,ib6,ic6,ie3,ie5,ie7,ie8,if8,ig5,ih4,ih6,ih9,ii6,ij0,ij3,ij4,ij5,ij6,ij9,ik7,il4,il6,iq5,iq6,is1,is5,iu0,iu1,iu3,iu5,iu6,iv5,iv6,iv8,iw2,iw7,iw8,iw9,ix6,ix7,ix8,iy0,iy1,iy3,iy4,iy5,iy6,iy7,iy8,iz2,iz5,iz8,ja8,je6,jh4,ji3,ji9,jm5,jo5,jo6,jq6,jq7,jq8,ju3,jx6,jx8,jy7,jy8,jz0,ka9,kd6,ke3,kf6,kl1,kq0,kq1,kq4,kq6,kq9,kw0,kw5,kw6,kw9,kx5,ky6,kz5,kz6,kz8,la5,ld6,ld8,le8,lf9,lg6,lh4,lj2,lj5,lk7,ll3,lq5,lq7,lr6,lr8,ls9,lv8,lw4,lw8,ma0,mj3,mj5,mj7,mk1,mm4,mn4,mn6,mo7,ms7,mu0,mu4,mx5,mz9,na2,na6,na9,nb4,nb5,nb6,nb9,nc5,nc8,nd5,nd9,ne4,ne9,nf5,nf7,nf8,nh8,nh9,ni6,nj5,nl6,nl7,nm5,nq2,nq3,nq5,nq6,nq9,nt0,nu5,nu8,nu9,nv1,nv8,nw9,nx5,ny4,ny5,ny6,ny7,ny9,nz4,nz8,oa5,oa8,oa9,ob0,oc0,oc5,od2,od6,od8,oe0,oe4,oe5,oe6,oe7,oe8,of3,of8,of9,oh3,oh6,oh7,oi5,oj0,oj1,oj2,oj4,oj6,oj9,ol2,ol5,ol6,ol8,om6,on4,oq0,oq1,oq4,oq5,oq6,oq7,oq8,oq9,or5,or6,os5,os8,ot5,ot6,ot9,ou0,ou4,ou5,ou6,ou8,ou9,ov6,ov8,ow3,ow4,ow5,ow6,ow8,ox6,ox9,oy2,oy5,oy6,oy9,pb9,pc1,pd6,pe9,pl2,pl6,pn3,pq5,pq6,pq7,pq8,pr4,pr5,pr6,pr7,pr8,pr9,pu2,pu5,pu7,pu8,pu9,pw0,pw5,pw7,pw9,px8,pz8,pz9,qa4,qb2,qb4,qb8,qc2,qc5,qc6,qc7,qc8,qc9,qd0,qd1,qd2,qd4,qd5,qd6,qd8,qe0,qe3,qe4,qe5,qe6,qe7,qe8,qe9,qf0,qf9,qg1,qg2,qg3,qg4,qg5,qg6,qg8,qg9,qh1,qh2,qh4,qh5,qh6,qh8,qi5,qj0,qj1,qj3,qj4,qj5,qj6,qj8,qj9,qk5,qk7,qk8,qk9,ql0,ql2,ql3,ql4,ql5,ql6,qm2,qm4,qm5,qm8,qn2,qn3,qn6,qn7,qn9,qo1,qo2,qo3,qo4,qo5,qo6,qo9,qp2,qp5,qp6,qr0,qr1,qr6,qs1,qs2,qs4,qs5,qs6,qs7,qs8,qs9,qu4,qu5,qu7,qv1,qv2,qv3,qv4,qv5,qv6,qv7,qv8,qv9,qw7,qw8,qx6,qy0,qy2,qy4,qy5,qy6,qy7,qy8,qz4,qz5,qz6,rd5,rf4,rf6,ri8,rl7,rq5,rq6,rs5,ru6,rw6,rw8,ry4,ry9,sd4,sh5,so3,sq0,sq5,sq6,ss0,su9,sv6,sv9,sx5,sz5,ta5,tb9,te9,tg4,tg5,tg9,ti6,tl6,to5,tp8,tq4,tq6,tq7,tr3,tr4,tu9,tx5,ty3,ty6,ty9,tz4,tz5,ua0,ua4,ua5,ua6,ua8,ua9,ub0,ub4,ub5,ub6,ub9,uc5,uc6,uc9,ud5,ud8,ud9,ue5,ue6,ue9,uf1,uf3,uf4,uf5,uf7,ug2,ug5,ug6,ug9,uh0,uh3,uh5,uh6,uh7,uh8,uh9,uj4,uj5,uj6,uj7,uj8,uj9,uk4,uk5,uk6,ul0,ul5,ul6,ul7,ul9,um0,um1,um2,um6,um7,um8,un4,un5,un6,un7,uo0,uo4,uo7,uo9,uq0,uq2,uq3,uq4,uq5,uq6,uq7,uq8,uq9,ur3,ur8,ur9,ut0,ut6,ut9,uv6,uv8,uw1,uw2,uw4,uw5,uw6,uw7,uw8,uw9,ux4,ux6,ux8,uy0,uy2,uy4,uy5,uy6,uy8,uy9,uz3,uz4,uz6,uz7,uz8,va4,va8,vd8,vd9,ve4,vf2,vf3,vf4,vf5,vf6,vf7,vf8,vf9,vg4,vh0,vh4,vh5,vh9,vi2,vi4,vi5,vi6,vi8,vi9,vj0,vj6,vj8,vk3,vn1,vn2,vn5,vo5,vo6,vo8,vo9,vq0,vq1,vq2,vq3,vq4,vq5,vq6,vq7,vq8,vq9,vs4,vs5,vs6,vt4,vt5,vu6,vu7,vu9,vv0,vv5,vw0,vw1,vw3,vw4,vw5,vy0,vy3,vy5,vy6,vy8,vz4,vz5,vz6,vz8,vz9,wa5,wa6,wa9,wb8,wc5,wc6,wc9,wd6,we0,wf0,wf3,wg5,wg6,wg9,wi4,wj5,wj9,wk5,wn0,wn3,wn4,wn5,wn6,wn7,wo5,wo9,wq4,wq8,wr0,wr2,wr4,wr5,wr6,wr7,wr8,ws5,ws8,wt0,wu6,wv3,wv4,wv5,wv6,wv7,wv8,wv9,wx4,wx9,wy4,wz4,wz5,wz6,wz7,wz8,xa1,xa2,xa3,xa6,xa7,xb2,xb4,xb5,xb7,xd5,xd9,xe6,xe7,xe8,xf5,xg2,xg6,xg7,xh2,xh6,xh8,xj3,xj8,xk7,xl9,xm5,xn5,xn6,xo2,xo4,xo5,xo7,xp6,xq2,xq3,xq4,xq5,xr5,xs5,xv3,xv4,xv5,xv6,xv9,xw1,xw4,xw8,xx5,xx6,xx8,xy3,xz4,ya6,ya8,yb0,yb6,yb8,yb9,yd0,yd5,yd6,yd8,yd9,ye4,ye6,ye7,yf4,yf9,yg4,yg5,yg8,yi5,yj4,yj5,yl4,yl5,ym0,ym4,ym7,yn0,yn4,yn6,yn8,yo8,yo9,yp0,yp3,yp6,yp9,yq4,yq5,yq6,yq9,yr3,yr9,yt4,yt6,yv0,yv2,yv3,yv5,yv6,yv9,yw4,yw6,yx1,yx4,yx9,yz5,za5,za6,za7,zb4,zb5,zb6,zd2,zd4,zd5,zd7,zd8,ze3,ze6,ze7,ze8,ze9,zf3,zf6,zf9,zg8,zg9,zi5,zj5,zj7,zk5,zk6,zk8,zl5,zl7,zl8,zm6,zo4,zo5'
char = char.split(',')
print('Begin Find\n------------------------------------')
http = requests.Session()
def getRes():
    res = http.get("https://github.com").text
    loc1 = re.search('auto-check src="\/signup_check\/username" csrf="(\S+)"', res).span()
    res = res[loc1[0]:loc1[1]]
    loc2 = re.search('csrf="', res).span()
    res = res[loc2[1]:len(res) - 1]
    return res
def getCode(form):
    code = http.post('https://github.com/signup_check/username', data=form).status_code
    if code == 429:
        time.sleep(5)
        res = getRes()
        return getCode(form)
    return code
res = getRes()
for value in char:
    form = {"referer":"https://github.com",'authenticity_token':res,'value':value}
    code = getCode(form)
    print(str(code) + ': '+ value)
print('------------------------------------\nEnd Find')
