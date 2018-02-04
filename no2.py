
s=6
n=40
x=32
sb=0.5
ap=6.3
g=-1.833
min=x-n
hasil=float(min/(s/ap))
print("s=6")
print("n=40")
print("simpangan baku=0,5")
print("akar pangkat 40=6,3")
print("Ho: M = 40 GB")
print("H1: M < 40 GB")
print("t= 32-40/(6/6,3)")
print("t= -8/(6/6,3)")
print("t= -8/0,95")
print("t=",hasil)
print("t 0,5 g=-1,833")


if hasil:
    print("Jadi Ho Ditolak, H1 Diterima")


