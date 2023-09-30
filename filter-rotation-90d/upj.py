##Filter rotation 90 degree, using transpose algorithm
import numpy as np
import matplotlib.pyplot as plt
nfile = 'upj.jpg'
pic = plt.imread(nfile)
new_file = plt.imsave(f'{nfile}_new.jpg',pic)
row,col,ch = pic.shape
print(row,col,ch)
hasil_row=col ; hasil_col=row ; hasil_ch = ch
gambar = np.zeros(shape=(hasil_row, hasil_col, ch), dtype=np.uint8)

# #  Right Rotate          
for i in range(row):
    for j in range(col):
        gambar[j, row - 1 - i, :] = pic[i, j, :]


# Left rotate
for i in range(row):
    for j in range(col):
        gambar[j, i, :] = pic[i, col - 1 - j, :]

# for i in range(0, hasil_row):
#     for j in range(0, hasil_col):
#         for k in range(0, ch):
#             # gambar[i, j, k] = pic[j, col - i - 1, k] # Rotasi 90 derajat berlawanan jarum jam
#             gambar[i, j, k] = pic[row - j - 1, i, k] # Rotasi 90 derajat searah jarum jam 

plt.figure(1)
plt.imshow(gambar)
plt.show()
