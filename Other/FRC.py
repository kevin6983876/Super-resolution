from skimage import io
import numpy as np
import matplotlib.pyplot as plt

pixel=640
image_size = 6400
def cart2pol(x, y, center):
    rho = np.sqrt((x-center[0])**2 + (y-center[1])**2)
    return rho
q = np.zeros([pixel,pixel])  ## coordinate transformation
for i in range(pixel):
    for j in range(pixel):
        q[i,j]=round(cart2pol(i,j,[pixel/2-0.5,pixel/2-0.5]))

img_c1 = io.imread("STD_tubulin0000-1.tif", 0)
img_c2 = np.fft.fft2(img_c1)
f1 = np.fft.fftshift(img_c2)
f1_c = np.conjugate(f1)

img_c5 = io.imread("STD_tubulin0001-1.tif", 0)
img_c6 = np.fft.fft2(img_c5)    
f2 = np.fft.fftshift(img_c6)
f2_c = np.conjugate(f2)

A = f1*f2_c
B = f1*f1_c
C = f2*f2_c

## Do FRC
FRC = np.zeros(int(pixel/2))
p = np.zeros([pixel,pixel])
for i in range(int(pixel/2)):
    p=np.zeros([pixel,pixel])
    p+=i+1
    coor = ((q-p)==0)
    FRC[i]=np.abs(np.sum(A*coor)/((np.sum(B*coor))**0.5*np.sum((C*coor))**0.5))

plt.plot(np.linspace(0,pixel/2/image_size,int(pixel/2)),FRC, 'r', label='FRC(q)')
plt.legend(loc='best')
plt.xlabel('q(nm^-1)')
plt.grid()
plt.savefig("FRC_123456890-1.png") 




from PIL import Image
plt.figure(figsize=(6.4*2, 4.8*2), constrained_layout=False)

plt.subplot(131), plt.imshow(img_c1, "gray"), plt.title("Original Image")
plt.subplot(132), plt.imshow(np.log(1+np.abs(f1)), "gray"), plt.title("Centered Spectrum")
plt.subplot(133), plt.imshow(q, "gray"), plt.title("Centered Spectrum")


#im = Image.fromarray(np.log(1+np.abs(img_c3)).astype(np.uint16))
#im.save('even.tif')

plt.show()