map(int,input().split())

#再帰 RE出たらこれを疑え！！！！！
import sys
sys.setrecursionlimit(10**8)

# Union-Find 再帰注意！

par=[-1]*N

def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def union(x,y):
    p,q=find(x),find(y)
    if p==q:
        return
    if p>q:
        p,q=q,p
    par[p]+=par[q]
    par[q]=p   

def size(x):
    return -par[find(x)]

def same(x,y):
    return find(x)==find(y)

# フェルマーの小定理
a**(p-1)==1 #(mod p)

# 組み合わせ(1個だけ求める版)(NでかくてもK次第でいける)

mod=10**9+7

def comb(n,k):
    l=m=1
    for i in range(k):
        l*=n-i
        m*=i+1
        l%=mod
        m%=mod
    return l*pow(m,-1,mod)%mod

# 組み合わせ(階乗だけ先に求める版)
fac=[1]*(N)
for i in range(2,N):
    fac[i]=fac[i-1]*i%mod

inv=[1]*(N)
inv[N-1]=pow(fac[N-1],mod-2,mod)
for i in range(N-2,1,-1):
    inv[i]=inv[i+1]*(i+1)%mod
    
def comb(n,r):
    ret=fac[n]*inv[r]*inv[n-r]%mod
    return ret


# 約数 #順番はバラバラ
def make_divisors(n):
    divisors=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
 
    return divisors

# 素因数分解(n>=2) #素数とその回数返す
def factorization(n):
    ret=[]
    tmp=n
    for i in range(2,int(n**0.5)+1):
        if tmp%i==0:
            cnt=0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            ret.append([i, cnt])
 
    if tmp!=1:
        ret.append([tmp, 1])
 
    return ret