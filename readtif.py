from skimage import io
import csv
import numpy as np

def ImportLocalizedPoint(Name):
    file = open(Name)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    row_count = sum(1 for row in csvreader)
    file.seek(0)
    rows = []
    id = []
    frame = []
    x_nm = []
    y_nm = []
    sigma = []
    intensity = []
    offset = []
    bkgstd = []
    uncertainty = []
    next(csvreader)
    for i in range(row_count):
        rows.append(next(csvreader))
    size = np.size(header)
    for i in range (row_count):
        for j in range(size):
            if j == 0:
                id.append(rows[i][j])
            if j == 1:
                frame.append(rows[i][j])
            if j == 2:
                x_nm.append(rows[i][j])
            if j == 3:
                y_nm.append(rows[i][j])
            if j == 4:
                sigma.append(rows[i][j])
            if j == 5:
                intensity.append(rows[i][j])
            if j == 6:
                offset.append(rows[i][j])
            if j == 7:
                bkgstd.append(rows[i][j])
            if j == 8:
                uncertainty.append(rows[i][j])
    return id,frame,x_nm,y_nm,sigma,intensity,offset,bkgstd,uncertainty,size

# Read the localized points
FileName='tubulin_localized.csv'
id = ImportLocalizedPoint(FileName)[0]
frame = ImportLocalizedPoint(FileName)[1]
x_nm = ImportLocalizedPoint(FileName)[2]
y_nm = ImportLocalizedPoint(FileName)[3]
sigma = ImportLocalizedPoint(FileName)[4]
intensity = ImportLocalizedPoint(FileName)[5]
offset = ImportLocalizedPoint(FileName)[6]
bkgstd = ImportLocalizedPoint(FileName)[7]
uncertainty = ImportLocalizedPoint(FileName)[8]
frame_number = ImportLocalizedPoint(FileName)[9]

# make the point spread function array
import numpy as np

def makeGaussian(size, intensity, sigma, center):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """
    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]
    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]
    return intensity*1/(2*np.pi*sigma)*np.exp(- ((x-x0)**2 + (y-y0)**2) / (2*sigma**2))

supres = io.imread('tubulin_superres.tif')

# Simulate the real data
import numpy as np
from PIL import Image
data = np.zeros([64,64])
background = np.zeros([64,64])+719
scale = 3
structure = io.imread('AVG_tubulin.tif')*scale
gauss_noise_std = 106.765
filenames = []

for i in range(np.size(id)):
    if float(frame [i])<2500:
        if frame[i+1] == frame [i]:
            data+=makeGaussian(64,float(intensity[i]),float(sigma[i]),[float(x_nm[i]),float(y_nm[i])])
        else:
            noise = np.zeros([64,64])
            for j in range(64):
                for k in range(64):
                    noise[j,k]=np.random.normal(0,gauss_noise_std)
            boolen1 = data<structure
            boolen2 = data>structure
            data = structure*boolen1+data*boolen2
            data += noise
            im = Image.fromarray(data.astype(np.uint16))
            im.save(str(frame[i])+'.tif')
            filename = str(frame[i])+'.tif'
            filenames.append(filename)
            data = np.zeros([64,64])

            
"""
import tifffile
with tifffile.TiffWriter('Stack.tif') as stack:
    for filename in filenames:
        stack.save(
            tifffile.imread(filename)
        )
import os
for filename in set(filenames):
    os.remove(filename)
# Calculate resolution from image
"""
