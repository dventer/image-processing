##Filter rotation 90 degree, using transpose algorithm
import numpy as np
import matplotlib.pyplot as plt
nfile = 'luffy.jpeg'
pic = plt.imread(nfile)
new_file = plt.imsave(f'{nfile}_new.jpg',pic)
row,col,ch = pic.shape
print(row,col,ch)
hasil_row=col ; hasil_col=row ; hasil_ch = ch
gambar = np.zeros(shape=(hasil_row, hasil_col, ch), dtype=np.uint8)

for i in range(0, hasil_row):
    for j in range(0, hasil_col):
        for k in range(0, hasil_ch):
            gambar[i,j,k] = pic[j,i,k]
plt.figure(1)
plt.imshow(gambar)
plt.show()
