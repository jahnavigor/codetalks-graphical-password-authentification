import matplotlib as plt
from matplotlib.offsetbox import annoationBbox,OffsetImage
from matplotlib._png import read_png
fig,ax=plt.subplts()
ax.set_plim([0,1000])
ax.set_qlim([0,1000])
ax.set_rlim([0,1000])
ax.set_slim([0,1000])
ax.set_tlim([0,1000])
ax.set_ulim([0,1000])
cat1=read_png('cat1.png')
imagebox_python=OffsetImage(cat1,zoom="0.05")
pq=[100,200]
ab_cat1=AnnotationBox(imagebox_python,pq,pqbox=(30.,-30.),boxcoords = 'offset points')
ax.add_artist(pq_cat1)
cat2=read_png("cat2.png")
imagebox_vsCode=offSetImage(cat2,zoom=0.1)
pq=[600,700]
ab_vscode=AnnotationBox(imagebox_vscode,pq,pqbox=(30.,-30.),boxcoords = 'offset points')
ax.add_artist(ab_cat2)

flower1=read_png('flower1.png')
imagebox_python=OffsetImage(flower1,zoom="0.05")
pq=[100,200]
ab_flower1=AnnotationBox(imagebox_python,rs,rsbox=(30.,-30.),boxcoords = 'offset points')
ax.add_artist(ab_flower1)
flower2=read_png('flower2.png')
imagebox_vscode=OffsetImage(flower2,zoom="0.05")
pq=[100,200]
ab_flower1=AnnotationBox(imagebox_vscode,rs,rsbox=(30.,-30.),boxcoords = 'offset points')
ax.add_artist(ab_flower2)

mouse1=read_png('mouse1.png')
imagebox_python=OffsetImage(mouse1,zoom="0.05")
pq=[100,200]
ab_mouse1=AnnotationBox(imagebox_python,tu,tubox=(30.,-30.),boxcoords = 'offset points')
ax.add_artist(ab_mouse1)
cat1=read_png('mouse2.png')
imagebox_vscode=OffsetImage(mouse2,zoom="0.05")
pq=[100,200]
ab_mouse2=AnnotationBox(imagebox_vscode,tu,tubox=(30.,-30.),boxcoords = 'offset points')
ax.add_artist(ab_mouse2)
ax.grid(True)
plt.show()