import numpy as np
from matplotlib import pyplot as plt

rowmax = int(1879)
colmax = int(1919)

batas1 = int(0.2*rowmax)
batas2 = int(0.4*rowmax)
batas3 = int(0.6*rowmax)
batas4 = int(0.8*rowmax)

gambar = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.uint8)
# for i in range(0,rowmax+1):
#     for j in range(0, colmax+1):
#         if (i >= 0 and i < batas1):
#             gambar[i,j,0] = 255
#         if (i >= batas1 and i < batas2):
#             gambar[i,j,1] = 255
#         if (i >= batas2 and i < batas3):
#             gambar[i,j,2] = 255
#         if (i >= batas3 and i < batas4):
#             gambar[i,j,0] = 255
#             gambar[i,j,1] = 255
#         if (i >= batas4 and i <= rowmax):
#             gambar[i,j,0] = 255
#             gambar[i,j,2] = 255
gambar[0:batas1, 0:colmax+1, 0] = 255
gambar[batas1:batas2, 0:colmax+1, 1] = 255
gambar[batas2:batas3, 0:colmax+1, 2] = 255
gambar[batas3:batas4,0:colmax+1, 0] = 255
gambar[batas3:batas4,0:colmax+1 , 1] = 255
gambar[batas4:, 0:colmax+1, 0] = 255
gambar[batas4:, 0:colmax+1, 2] = 255

print(type(gambar))
plt.imsave('rainbow.jpg', gambar)
plt.figure()
plt.imshow(gambar)
plt.show()
    