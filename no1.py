n=5
X=214200
sb=0.99

print("n=5")
print("Total Sampel =214200")
print("Simpangan Baku = 0,01")
print("t= Simpangan Baku/2 : n-1")
print("t= 0,99/2 : 5-1")
t=sb/2
print("t=",t," : 4 =2,776")
print("Rumus = X-t(simpangan baku/2):n-2 (akar pangkat)n < M < X-t(simpangan baku/2):n-1 (akar pangkat)n")
print("      =214200-2,776 .(akar pangkat)5 < M <214200+2,776 .(akar pangkat)5 ")
print("      =214200-2,776 .2,236 < M <214200+2,776 . 2,236")
print("      =214200-6,2 < M <214200+6,2")
h1=X-6.2
h2=X+6.2
print("Hasil =",h1," < M <", h2)
