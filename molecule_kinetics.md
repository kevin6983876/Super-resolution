# Table of Contents
1. [Principle of single-molecule imaging](#Principle-of-single-molecule-imaging)
   1. [AIM](#aim-high-sbr-and-sparse)
2. [The bleaching in PALM is time-consuming, especially in spinning disk](#The-bleaching-in-PALM-is-time-consuming)
   1. [Comparison between confocal and widefield](#comparison-between-widefield-bleaching-and-confocal-bleaching)
   2. [Theory explanation](#theory-explanation)
      1. [Parameter](#parametersbleaching)
      2. [Plugin parameters](#plugin-the-parameters-bleaching)
3. [STORM is less time consuming](#storm-is-less-time-consuming)
   1. [The photoswitching mechanism](#the-photoswitching-mechanism-theory)
   2. [How to calculate blinking rate?](#how-to-calculate-blinking-rate)
      1. [Parameters](#parameters)
      2. [Plugin parameters](#plugin-the-parameters)
   3. [How to determine the labeling density](#how-to-determine-the-labeling-density)


# Principle of single-molecule imaging
To capture single molecule signal, two conditions must be achieved. ([ref](https://www.nature.com/articles/nprot.2011.336.pdf))
>1. High enough contrast
>2. Only one ON-state molecule in the diffraction-limited region

##### AIM: High SBR and sparse

PALM: 
High SBR & Sparse: bleaching

STORM:
High SBR & Sparse: OFF state dominant

## The bleaching in PALM is time-consuming, especially in spinning disk.
For PALM, typical bleaching time takes about 0.5-1s, and frame number is about $10^4$ to $10^5$ frames. ([ref](https://pubmed.ncbi.nlm.nih.gov/16902090/)) (2-10 hrs in total)

[PALM video](https://drive.google.com/file/d/1b6W5BdQX6stIgmMg8uTxuXoXUNvQl6vC/view?usp=sharing)
<!---
### Why we need that long time?
[Kaede bleaching dynamics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2745648/#SD1)


#### Nature of photobleaching
Photobleaching probability is virtually independent with spot intensity([ref](https://pubmed.ncbi.nlm.nih.gov/16538628/)). We can say that photobleaching is molecule-wise. 
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274867197_1393980431060470_4938471626513267009_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Q-hU4qZXPxUAX_sXgGG&_nc_ht=scontent-tpe1-1.xx&oh=03_AVL1XzlqiSWLznkELR8FKjjT9m9UOD7egYi8c9MYAAVaeA&oe=624F4592)
-->
### Comparison between widefield bleaching and confocal bleaching
[Data ref](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2745648/#SD1)
Condition:
1. Widefield: 40x dry objective (Nikon Plan Fluorite,
NA = 0.85), metal halide illumination source
1. Confocal: 40x oil immersion objective (Olympus UPlan Apo, NA = 1.00), 543-nm laser
1. Laser intensity = ~475 $mW/cm^2$ power (Widefield), 100$\mu W$ (Confocal)

Widefield
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274294032_701256954381925_919571328593342760_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=DnXi9i0ZEKoAX_10cOT&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLrZYuLvFOu3AE0rlvdSYvbJQJhK0_BuGpNYTi9SfPI7A&oe=624F7194)
Confocal
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274536284_471719157983779_5648725458810395149_n.png?_nc_cat=106&ccb=1-5&_nc_sid=ae9488&_nc_ohc=fbyPj7FNO7IAX_Gs37l&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJzvSvQh0uj9zC8clYIsJA_GevYZ6QRYWLkmTZkPeCQNw&oe=622B0812)

>In most cases,  the calculated $t_{1/2}$ for confocal bleaching is more than an order of magnitude greater than that for widefield illumination. ([ref](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/7191/719105/Evaluating-and-improving-the-photostability-of-fluorescent-proteins/10.1117/12.814684.full?SSO=1))

$t_{1/2}$: time to bleach 50% starting from 1000 photons/s emission per chromophore 

### Theory explanation
[ref](https://pubmed.ncbi.nlm.nih.gov/25076144/)

<!---
For widefield: $X=\frac{F}{A}N(\lambda)\sigma(\lambda)\Delta\lambda$

###### Assume single-layer sample.

$X$: rate of excitation (photons/s)
$F$: amplitude factor
$A$: illumination area
$N(\lambda)$: photon numbers per 1nm bandwidth
$\sigma(\lambda)$: optical cross section per molecule

For confocal: $X=\Phi\sigma(\lambda)=\frac{P}{EA}\sigma(\lambda)$
$X$: rate of excitation (photons/s)
$\Phi$: average photon flux over scanned area
$A$: illumination area
$E$: photon energy
$P$: power
$\sigma(\lambda)$: optical cross section per molecule
-->
#### Parameters (bleaching)
$P$: power
$A$: scanning area
$N$: number of beamlet
$\omega_1, \omega_2$: the radial, the distances from the center of the volume element in the radial and axial direction, respectively, at which the laser intensity has dropped by a factor of $e^2$, assuming a Gaussian beam profile.

>Photobleaching often takes place from the triplet state after intersystem crossing in the excited
fluorophore. (Let's ignore $k_2$ for a while, i.e., $k_2<<1$)
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274547028_288284690099181_3915019348969566513_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_ohc=4ZIGok01GTIAX-153BQ&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKMizv0h-qJT5rv5G8NLwcCkO-Qq3sVo7ytFHUdKX7Q_w&oe=6253D3CE)
According to this model, triplet state population (in equilibrium) is important!

#### Plugin the parameters (bleaching)
$P=20mW, A=300\mu m*300\mu m, N=100, \omega_1=0.2\mu m, \omega_2=0.5\mu m, V_0=\frac{4}{3}\pi\omega_1^2\omega_2=8.38*10^{-20}m^3$

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275440469_504096897789276_3947634040283139355_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=eJF2f9G2lqAAX_TJR4Z&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIwy5-tUpt8xU6GPIsdiyJ6jBLunJo-BOmCMs3PMMkyUw&oe=62542601)

##### Spinning disk
###### Consider the limiting case 1: the disk is not spinning. 
1. At the excitation points:$P=20mW\Rightarrow T_{eq,spot}\approx0.63$
2. Outside the excitation points: $P=0\Rightarrow T_{eq,o}=0$
3. $T_{eq}=T_{eq,spot}*\frac{N\pi\omega_1^2}{A}+T_{eq,o}*\frac{A-N\pi\omega_1^2}{A}=0.63*\frac{100*\pi*(0.2\mu m)^2}{300\mu m*300\mu m}=1.39*10^{-4}$

###### Consider the limiting case 2: the disk spins very fast $\Rightarrow$ can be considered as a uniform widefield light source. 
1. $P_{eff}=P*\frac{N\pi\omega_1^2}{A}=2.8\mu W\Rightarrow T_{eq}\approx0.0037$

Between two limiting cases, $T_{eq}\approx 1.39*10^{-4}$~$3.7*10^{-3}$

$r_{bleach,spin}=k_4*1.39*10^{-4}$~$k_4*3.7*10^{-3}$

##### Widefield
Widefield bleaching rate is the same as the second case of spinning disk. $\Rightarrow r_{bleach,wide}=k_4*3.7*10^{-3}$

>$\Rightarrow$ (Spinnig disk) confocal bleaching time is more than an order of magnitude greater than that for widefield illumination. **Agreed with observation!**
<!---
$t_{1/2}=\frac{t_{raw}XQ}{1000photons/s}$
$t_{1/2}$: time to bleach 50% starting from 1000 photons/s emission per chromophore 
$Q$: quantum efficiency
$t_{raw}$: time to drop to 50% of the initial intensity (measured)

Let's try to consider a typical case where the average powers of spinning confocal and widefield are the same. 
$\Rightarrow X_{wide}=X_{spinning}$, $Q$ is the same for identical molecules.
$t_{1/2, spining}$ and $t_{1/2, wide}$ is dependent on $t_{raw,spinning}$ and $t_{raw,wide}$, respectively. 
-->
### Why we need that many frames?
Nyquist condition. Can be calculated...

## STORM is less time consuming.
>Unlike PALM that has fixed (ON-state) bleaching time, the ON/OFF states dynamics in STORM can be adjusted by external means (chemical condition, excitation power). $\Rightarrow$ **less time consuming.**

### The photoswitching mechanism (Theory)
###### ???561 Kaede???????????????488??????? ????????????????????????dark state
A three-state model. Using this model can explain why there is fast blinking.  

![Three state model](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274254602_509407327286982_4285864595330128796_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=PnSnIKX4qHAAX_te7v0&_nc_oc=AQk0Qe9OIMObcV-zj2Hi0inw2RXwQmoMCAQ1aBzjqbyDCiYuIqpISI0xffLo6J_n-18&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLD4UiBliLSvw4tzKnsA4pm-gcXVdWx7UNizzoUrpuiuQ&oe=624FEEA4)
Mathematically, we can use three ODE to describe the above system.
$\frac{d}{dt}\left(\begin{matrix}S_0(t)\\S_1(t)\\T(t)\end{matrix}\right) =\left(\begin{matrix}-k_{12} & k_{21} & k_{31}\\k_{12} & -(k_{23}+k_{21}) & 0\\0 & k_{23} & -k_{31}\end{matrix}\right)\left(\begin{matrix}S_0(t)\\S_1(t)\\T(t)\end{matrix}\right)$
Solve for the eigenvalue equation $$\lambda(\lambda^2+(k_{23}+k_{21}+k_{12}+k_{31})\lambda+k_{12}k_{23}+k_{31}k_{23}+k_{31}k_{21})=0$$ for the middle matrix. We have three eigenvalues $\lambda_1=0, \lambda_2, \lambda_3$, and corresponding eigenvectors $\bold{x_1,x_2,x_3}$
Hence, the general solution of $X(t)=\left(\begin{matrix}S_0(t)\\S_1(t)\\T(t)\end{matrix}\right)=c_1e^{\lambda_1t}\bold{x}_1+c_2e^{\lambda_2t}\bold{x}_2+c_3e^{\lambda_3t}\bold{x}_3$

- Since $\lambda_1=0$, the system will approach to a steady state when $t\rightarrow\infty$.
- $\lambda_2$ is a very large term. Hard to be measured.
- $\lambda_3$ can be measured. Assuming $k_{12}+k_{21}>>k_{31}+k_{23}$, then $\lambda_3=-k_{31}-\frac{k_{12}k_{23}}{k_{12}+k_{21}}$, $T_{eq}=\frac{k_{23}k_{12}}{k_{12}(k_{23}+k_{31})+k_{31}(k_{21}+k_{23})}$

Combining the following effects to autocorrelation function:
- diffusion of molecule in and out the laser volume
- molecules entering and leaving triplet state
We have our autocorrelation function
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274656221_370807598223761_1386202177098644304_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=33g4xqinGeoAX8w81LX&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVI03IdCqiuI_4Sf88K_gmt68LJOY7ctbtjk7CUPpTCAhw&oe=6250A98A)
A typical relation between $\lambda_3$(the rate at which there is a population buildup in the triplet state) and intensity.
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274652847_5168091999896421_1049625651085026328_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=PeWX2R0j-bEAX-oltq3&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIFIzqhBILNuxOd2LnCLmNQdNVbRlczL6Lqcqo_JEcYiw&oe=624DFFA2)
Relation between $T_{eq}$ and intensity
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274614827_658555828802825_3630722350239444723_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_ohc=tndGkWQwO0MAX-vrJlZ&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJvQ_nGmH-1cNQ7OYLVHLf3486ihFG16xePEZN7mssYMw&oe=624FE001)

Physical meaning of $\lambda_3$ and $T_{eq}$
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275515700_964634747389797_4730825092774499123_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_ohc=LvZyb4YUKoIAX8JpB6u&_nc_ht=scontent-tpe1-1.xx&oh=03_AVK9jDZdMLFBA5XClgdRWHZKVnJIOe-oQVzm3mytfI2_xA&oe=6252E490)

$\Rightarrow$ **Blinking rate** is dependent on $\lambda_3$ and labelling density $\rho$.

### How to calculate blinking rate?
#### Parameters:
$\rho$: labeling density
$N$: number of beamlet
$\omega_1, \omega_2$: the radial, the distances from the center of the volume element in the radial and axial direction, respectively, at which the laser intensity has dropped by a factor of $e^2$, assuming a Gaussian beam profile.
$V_0=\frac{4}{3}\pi\omega_1^2\omega_2$: volume of one excitation beamlet
$NV_0\rho=\frac{NV_0}{d^3}$: total number of molecules in the excitation volume.

$P$: power of total beamlets$\Rightarrow\frac{P}{N}$: power of individual beamlets
$A$: scanning area
$\lambda_3$: the rate at which there is a population buildup in the triplet state
$T_{eq}$: relative triplet state population in equilibrium
#### Plugin the parameters
$P=20mW, A=300\mu m*300\mu m, N=1000, \omega_1=0.2\mu m, \omega_2=0.5\mu m, V_0=\frac{4}{3}\pi\omega_1^2\omega_2=8.38*10^{-20}m^3$

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275440469_504096897789276_3947634040283139355_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=eJF2f9G2lqAAX_TJR4Z&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIwy5-tUpt8xU6GPIsdiyJ6jBLunJo-BOmCMs3PMMkyUw&oe=62542601)
###### Consider the limiting case 1: the disk is not spinning. 
1. At the excitation points:$P=20mW$ and split into $1000$ beams $\Rightarrow T_{eq,spot}\approx0.025,\lambda_{3,spot}=0.5(1/\mu s)$ 
2. Outside the excitation points: $P=0\Rightarrow T_{eq,o}=0,\lambda_{3,o}=0.5(1/\mu s)$
3. $T_{eq}=T_{eq,spot}*\frac{N\pi\omega_1^2}{A}+T_{eq,o}*\frac{A-N\pi\omega_1^2}{A}=0.025*\frac{1000*\pi*(0.2\mu m)^2}{300\mu m*300\mu m}=5.5*10^{-5}$
4. $\lambda_3=\lambda_{3,spot}*\frac{N\pi\omega_1^2}{A}+\lambda_{3,o}*\frac{A-N\pi\omega_1^2}{A}\approx 0.5$

###### Consider the limiting case 2: the disk spins very fast $\Rightarrow$ can be considered as a uniform widefield light source. 
1. $P_{eff}=P*\frac{N\pi\omega_1^2}{A}=28\mu W\Rightarrow T_{eq}\approx0.035, \lambda_3\approx0.5(1/\mu s)$

> Between two limiting cases, $T_{eq}\approx 5.5*10^{-5}$~$0.035, \lambda_3\approx 0.5(1/\mu s)$

###### Case 3: pixel dwell time$\approx0.1\times\frac{1}{k_{23}}=10^{-7}s=0.1\mu s$
###### Case 4: pixel dwell time$\approx\frac{1}{k_{23}}=10^{-6}s=1\mu s$  
###### Case 5: pixel dwell time$\approx10\times\frac{1}{k_{23}}=10^{-5}s=10\mu s$ 

Current state of the art spinning disk rotates 15,000 rpm.[ref1](https://www.photometrics.com/learn/spinning-disk-confocal-microscopy/the-evolution-of-spinning-disk-confocal-microscopy-v2)
The Nipkow disk is located in a conjugate image plane and a **partial rotation** of the disk scans the specimen with approximately 1000 individual light beams that can traverse the entire image plane in less than a millisecond.
[ref2](https://zeiss-campus.magnet.fsu.edu/articles/spinningdisk/introduction.html)
Suppose that there are 2048 by 2048 pixels. 
Then each beam passes $2048*2048/1000=4194pxls$ in $1$ ms. Hence, pixel dwell time $\approx 0.23 \mu s$ And each beam has power $20mW/1000=20\mu W$ 
Hence the intensity is $\frac{20\mu W}{\pi\omega_1^2}\approx 11kW/cm^2$ (Normally, widefield intenisty is about $2kW/cm^2$, an order smaller.)
Visually,
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275641025_672701293877298_2925550402700425372_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=6Lt6Jm0wYb0AX9jGri_&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJy6iECuKrObMnXLsQ6vb75h8cz0a-NC24DGG_tDZBZNA&oe=62594369)

>Hence the state-of-the-art spinning disk can be thought as Case 3.
Using the formula $X(t)=\left(\begin{matrix}S_0(t)\\S_1(t)\\T(t)\end{matrix}\right)=c_1e^{\lambda_1t}\bold{x}_1+c_2e^{\lambda_2t}\bold{x}_2+c_3e^{\lambda_3t}\bold{x}_3$

After calculation, $T(t)$ is as follows and reaches $\approx0.0026$ at $0.2\mu s$ and then decrease to $0$ in $5\mu s$ ($P=20mW$).
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275215182_5221333624564643_798301954719096398_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_ohc=yXdII990GYwAX9-CtD5&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJLEOiX4dYAlhSNr-cPZnDY4qurS3_mduIc-MPy2VGNtQ&oe=6258D952)

> Hence, the triplet development is not sufficient during this short time period. 

>**Final comparison**: spinning disk vs widefield, condition: 
$I_{spinning}=11kW/cm^2$
$I_{wide}=1.1kW/cm^2$
Spinning disk: $0.2\mu s$ pulse followed by $>100\mu s$ rest per pixel
Widefield: continuous illumination
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275035014_361212279065172_8037043985315838394_n.png?_nc_cat=103&ccb=1-5&_nc_sid=ae9488&_nc_ohc=WOKFWv3BxuEAX83l5TZ&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLs7NfR2Q1I8p9WCg-voq5odXt7xU4jkt9OZJyHu2Wu_g&oe=625A4DA0)
**Conclusion: Triplet state population is way more larger in the case of widefield than in spinning disk.**
<!---
>**Comparison** If $k_{21}$ decreases 10 folds. Then $T(t)$ will increase 10 folds . This result is reasonable since when the rate of electrom from singlet excited state to the singlet ground state decreases 10 folds, more population will stay in the singlet excited state and thus more triplet state population is built.
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275903226_501601771497487_3124845507986282592_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Sw5PLFCvLGwAX9dIihO&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLtCOLmfSCphbVVpFVYrvd_CEeH4qnqZ3lAMS0yZjbuhQ&oe=625843AE)
-->

### How to determine the labeling density?
Let's assume the labeling density $\rho$ is $\frac{(L/d)^3}{L^3}=\frac{1}{d^3}$ 
$d=1,5,10,20,50,100nm$
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275395158_3097633807132677_5057225665692364082_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=gcFrQW0ezvgAX9VmzO4&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLccVTktG1s5lQiRkNarqzXR4MKJwHA3JUxl3C3rmVMkA&oe=6251BBD4)

#### Rh6G photophysical properties (Case study)

After several fitting procedures, we have

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274325058_926017408076972_7050144123343753985_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=2BW97AfH0y0AX89R9Bx&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLS3lFJTBFNkAqN1zHd1ecB9HOyLZ3PVWzvs0ANzAyycA&oe=624D1A14)

We can also obtain $k_{12}=\sigma_{exc}\times \frac{P}{\pi\omega_1^2}$

$\frac{P}{\pi\omega_1^2}$ needs to be expressed as photons per square meter per second. $P=P_{origin}*2.58*10^{18}$

#### DsRed photophysical properties (Case study)

#### Kaede photophysical properties (Case study)
##### Intensity dependence of ACF (The most important application)
Here is the experimental results of ACF curve of red form Kaede when varying the excitation intensity (from $2.5$ to $78\frac{kW}{cm^2}$). 

After fitting with the model
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275184263_632338294498567_2914250142237772510_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=kwGErwIEvSAAX9wpAq6&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKUy8xS-TacV-8hBQtIsBIXUMJeuHYSrtyWHFA3KKByRg&oe=624F8332), where $\tau_i$ is the rate, and $F_i$ is the fraction, we have two blinking dynamics (i=2) with $\tau_1=6.5$ - $32$kHz(153$\mu s$-30$\mu s$), $F_1\approx30\%$, and $\tau_2=1.3$kHz - $10$kHz(769$\mu s$-100$\mu s$), $F_2\approx20\%$.
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/273648558_300396522012577_1102684933084334318_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=z9VyP9SEK5gAX-RrYIA&tn=kmMc2ol6ujtRzeuG&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLNAO7arsvHyt49Lwihhrm-Zxc1-WrLrwhwJqIOy_8e4Q&oe=6248DEB8)