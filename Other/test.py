import numpy as np

T_shape = np.zeros([3,3]) #T 
T_shape[0,0]=T_shape[0,1] =T_shape[0,2] =T_shape[1,1] =T_shape[2,1] = 1
T_shape_90 = np.zeros([3,3]) 
T_shape_90[0,2]=T_shape_90[1,0]=T_shape_90[1,1]=T_shape_90[1,2]=T_shape_90[2,2]=1
T_shape_180 = np.zeros([3,3]) 
T_shape_180[0,1] =T_shape_180[1,1]=T_shape_180[2,0]=T_shape_180[2,1]=T_shape_180[2,2]=1
T_shape_270 = np.zeros([3,3]) 
T_shape_270[0,0] =T_shape_270[1,0] =T_shape_270[1,1] =T_shape_270 [1,2]=T_shape_270[2,0] =1


short_T_shape = np.zeros([3,3]) #T 
short_T_shape[0,0]=short_T_shape[0,1] =short_T_shape[0,2] =short_T_shape[1,1] = 1
short_T_shape_90 = np.zeros([3,3]) 
short_T_shape_90[0,2]=short_T_shape_90[1,1]=short_T_shape_90[1,2]=short_T_shape_90[2,2]=1
short_T_shape_180 = np.zeros([3,3]) 
short_T_shape_180[1,1]=short_T_shape_180[2,0]=short_T_shape_180[2,1]=short_T_shape_180[2,2]=1
short_T_shape_270 = np.zeros([3,3]) 
short_T_shape_270[0,0] =short_T_shape_270[1,0] =short_T_shape_270[1,1] =short_T_shape_270[2,0] =1


LargeL_shape = np.zeros([3,3]) #LargeL
LargeL_shape[0,0]=LargeL_shape[1,0]=LargeL_shape[2,0]=LargeL_shape[2,1]=LargeL_shape[2,2]=1
LargeL_shape_90 = np.zeros([3,3]) #LargeL
LargeL_shape_90[0,0]=LargeL_shape_90[0,1]=LargeL_shape_90[0,2]=LargeL_shape_90[1,0]=LargeL_shape_90[2,0]=1
LargeL_shape_180 = np.zeros([3,3]) #LargeL
LargeL_shape_180[0,0]=LargeL_shape_180[0,1]=LargeL_shape_180[0,2]=LargeL_shape_180[1,2]=LargeL_shape_180[2,2]=1
LargeL_shape_270 = np.zeros([3,3]) #LargeL
LargeL_shape_270[0,2]=LargeL_shape_270[1,2]=LargeL_shape_270[2,0]=LargeL_shape_270[2,1]=LargeL_shape_270[2,2]=1

L_shape = np.zeros([3,3]) #LargeL
L_shape[0,0]=L_shape[1,0]=L_shape[2,0]=L_shape[2,1]=1
L_shape_90 = np.zeros([3,3]) #LargeL
L_shape_90[0,0]=L_shape_90[0,1]=L_shape_90[0,2]=L_shape_90[1,0]=1
L_shape_180 = np.zeros([3,3]) #LargeL
L_shape_180[0,1]=L_shape_180[0,2]=L_shape_180[1,2]=L_shape_180[2,2]=1
L_shape_270 = np.zeros([3,3]) #LargeL
L_shape_270[1,2]=L_shape_270[2,0]=L_shape_270[2,1]=L_shape_270[2,2]=1

inverse_L_shape = np.zeros([3,3]) #LargeL
inverse_L_shape[0,2]=inverse_L_shape[1,2]=inverse_L_shape[2,1]=inverse_L_shape[2,2]=1
inverse_L_shape_90 = np.zeros([3,3]) #LargeL
inverse_L_shape_90[1,0]=inverse_L_shape_90[2,0]=inverse_L_shape_90[2,1]=inverse_L_shape_90[2,2]=1
inverse_L_shape_180 = np.zeros([3,3]) #LargeL
inverse_L_shape_180[0,0]=inverse_L_shape_180[0,1]=inverse_L_shape_180[1,0]=inverse_L_shape_180[2,0]=1
inverse_L_shape_270 = np.zeros([3,3]) #LargeL
inverse_L_shape_270[0,0]=inverse_L_shape_270[0,1]=inverse_L_shape_270[0,2]=inverse_L_shape_270[1,2]=1

small_L_shape = np.zeros([2,2]) 
small_L_shape[0,0]=small_L_shape[1,0]=small_L_shape[1,1]=1
small_L_shape_90 = np.zeros([2,2]) 
small_L_shape_90[0,0]=small_L_shape_90[0,1]=small_L_shape_90[1,1]=1

square = np.zeros([2,2])
square += 1

five = np.zeros([1,5])
five+=1

ver_five = np.zeros([5,1])
ver_five+=1

four = np.zeros([1,4])
four+=1

ver_four = np.zeros([4,1])
ver_four+=1

three = np.zeros([1,3])
three+=1

ver_three = np.zeros([3,1])
ver_three+=1

two = np.zeros([1,2])
two+=1

ver_two = np.zeros([2,1])
ver_two+=1

one = np.zeros([1,1])
one+=1

mo_shape = np.zeros([3,3])
mo_shape[0,0]=mo_shape[0,1]=mo_shape[0,2]=mo_shape[1,0]=mo_shape[1,2]=1
mo_shape_90 = np.zeros([3,3])
mo_shape_90[0,1]=mo_shape_90[0,2]=mo_shape_90[1,2]=mo_shape_90[2,1]=mo_shape_90[2,2]=1
mo_shape_180 = np.zeros([3,3])
mo_shape_180[1,0]=mo_shape_180[1,2]=mo_shape_180[2,0]=mo_shape_180[2,1]=mo_shape_180[2,2]=1
mo_shape_270 = np.zeros([3,3])
mo_shape_270[0,0]=mo_shape_270[0,1]=mo_shape_270[1,0]=mo_shape_270[2,0]=mo_shape_270[2,1]=1


s_shape = np.zeros([3,3])
s_shape[1,1]=s_shape[1,2]=s_shape[2,0]=s_shape[2,1]=1
s_shape_90 = np.zeros([3,3])
s_shape_90[0,1]=s_shape_90[1,1]=s_shape_90[1,2]=s_shape_90[2,2]=1
inverse_s_shape = np.zeros([3,3])
inverse_s_shape[1,0]=inverse_s_shape[1,1]=inverse_s_shape[2,1]=inverse_s_shape[2,2]=1
inverse_s_shape_90 = np.zeros([3,3])
inverse_s_shape_90[0,1]=inverse_s_shape_90[1,0]=inverse_s_shape_90[1,1]=inverse_s_shape_90[2,0]=1

board = np.zeros([9,9])

while True:
    shape = input('step:')
    if shape =='T_shape':
        print(T_shape)
    if shape =='T_shape_90':
        print(T_shape_90)
    if shape =='T_shape_180':
        print(T_shape_180)
    if shape =='T_shape_270':
        print(T_shape_270)
    if shape =='short_T_shape':    
        print(short_T_shape)
    if shape =='short_T_shape_90':    
        print(short_T_shape_90)
    if shape =='short_T_shape_180':    
        print(short_T_shape_180)
    if shape =='short_T_shape_270':
        print(short_T_shape_270)
    if shape =='LargeL_shape':
        print(LargeL_shape)
    if shape =='LargeL_shape_90':
        print(LargeL_shape_90)
    if shape =='LargeL_shape_180':
        print(LargeL_shape_180)
    if shape =='LargeL_shape_270':
        print(LargeL_shape_270)
    if shape =='L_shape':
        print(L_shape)
    if shape =='L_shape_90':
        print(L_shape_90)
    if shape =='L_shape_180':
        print(L_shape_180)
    if shape =='L_shape_270':    
        print(L_shape_270)
    if shape =='inverse_L_shape':
        print(inverse_L_shape)
    if shape =='inverse_L_shape_90':
        print(inverse_L_shape_90)
    if shape =='inverse_L_shape_180':
        print(inverse_L_shape_180)
    if shape =='inverse_L_shape_270':    
        print(inverse_L_shape_270)
    if shape =='small_L_shape':
        print(small_L_shape)
    if shape =='small_L_shape_90':
        print(small_L_shape_90)
    if shape =='mo_shape':
        print(mo_shape)
    if shape =='mo_shape_90':
        print(mo_shape_90)
    if shape =='mo_shape_180':
        print(mo_shape_180)
    if shape =='mo_shape_270':
        print(mo_shape_270)
    if shape =='s_shape':
        print(s_shape)
    if shape =='s_shape_90':
        print(s_shape_90)
    if shape =='inverse_s_shape':
        print(inverse_s_shape)
    if shape =='inverse_s_shape_90':
        print(inverse_s_shape_90)
    if shape =='square':
        print(square)
    if shape =='ver_five':
        print(ver_five)
    if shape =='five':
        print(five)
    if shape =='ver_four':
        print(ver_four)
    if shape =='four':
        print(four)
    if shape =='ver_three':
        print(ver_three)
    if shape =='three':
        print(three)
    if shape =='ver_two':
        print(ver_two)
    if shape =='two':
        print(two)
    if shape =='one':
        print(one)