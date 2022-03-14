[Todo lists](https://docs.google.com/document/d/1PmqmAC3JLrxaWYusEgZz5_CUBiyhWrMrnnstpt6ula8/edit?usp=sharing)

## Deep tissue super-resolution imaging via two-photon spinning disk localization
[Photonic West](https://docs.google.com/document/d/1Y5SSFlGdQwiD2743RTZNmM7oJkpC0f3VwCBZsSFFnZw/edit?usp=sharing)

### Abstract
Recently, whole-*Drosophila*-brain structural mapping has been demonstrated with 50-nm resolution, but not *in vivo*. In this work, we combine two-photon excitation into a spinning disk confocal setup to enable 500 μm imaging depths in uncleared mouse brains (~100 μm in *Drosophila*), and wide-field optical sectioned detection, respectively. Through integration of photo-activated localization microscopy (PALM), which also reduces photodamage of the tissue, we achieve resolution down to 50 nm in an intact *Drosophila* brain, pushing to the limit of imaging depth and resolution. Our work paves the way toward *in vivo* functional connectome studies. 

### Introduction

Super-resolution imaging avails the imaging resolution down to tens of nanometers. We have demonstrated whole brain structural mapping in a cleared *Drosophila* brain with ~50 nm resolution, but current optical clearing techniques do not allow *in vivo* observation. A technical milestone is to achieve *in vivo* whole brain imaging with similar resolution. Although *in vivo* super-resolution imaging has been realized, it is limited to thin samples. The underlying reason is that current state-of-the-art techniques rely on either saturation plus wavefront engineering or localization with blinking fluorophores. The former imaging depth is limited due to aberration or scattering in living tissues, and the latter suffers from lack of optical-sectioning ability.

In this work, we combine two-photon excitation into a spinning disk confocal setup to enable deep-tissue penetration and wide-field optical sectioned detection, respectively. The two-photon spinning disk microscope offers ~500 μm and ~100 μm imaging depths in uncleared mouse and *Drosophila* brains, similar to typical single-point detection two-photon microscopy. Through integration of photo-activated localization microscopy (PALM), which also reduces photodamage of the tissue, we achieve resolution down to ~50 nm in an intact *Drosophila* brain, pushing to the limit of imaging depth and resolution. More importantly, the protocol works for living brains, so our work paves the way toward *in vivo* functional connectome studies. 


## The bleaching in PALM is time-consuming.
For PALM, typical bleaching time takes about 0.5-1s, and frame number is about $10^4$ to $10^5$ frames. ([ref](https://pubmed.ncbi.nlm.nih.gov/16902090/)) (2-10 hrs in total)

[PALM video](https://drive.google.com/file/d/1b6W5BdQX6stIgmMg8uTxuXoXUNvQl6vC/view?usp=sharing)

### Why we need that long time?
[Kaede bleaching dynamics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2745648/#SD1)

<!---
#### Nature of photobleaching
Photobleaching probability is virtually independent with spot intensity([ref](https://pubmed.ncbi.nlm.nih.gov/16538628/)). We can say that photobleaching is molecule-wise. 
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274867197_1393980431060470_4938471626513267009_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Q-hU4qZXPxUAX_sXgGG&_nc_ht=scontent-tpe1-1.xx&oh=03_AVL1XzlqiSWLznkELR8FKjjT9m9UOD7egYi8c9MYAAVaeA&oe=624F4592)
-->
#### Comparison between widefield bleaching and confocal bleaching
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

#### How to systematically compare the time needed for bleaching?

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

$t_{1/2}=\frac{t_{raw}XQ}{1000photons/s}$
$t_{1/2}$: time to bleach 50% starting from 1000 photons/s emission per chromophore 
$Q$: quantum efficiency
$t_{raw}$: time to drop to 50% of the initial intensity (measured)


Let's try to consider a typical case where the average powers of spinning confocal and widefield are the same. 
$\Rightarrow X_{wide}=X_{spinning}$, $Q$ is the same for identical molecules.

>$t_{1/2, spining}$ and $t_{1/2, wide}$ is dependent on $t_{raw,spinning}$ and $t_{raw,wide}$, respectively. **In most cases,  the calculated $t_{1/2}$ for confocal bleaching is more than an order of magnitude greater than that for widefield illumination.** ([ref](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/7191/719105/Evaluating-and-improving-the-photostability-of-fluorescent-proteins/10.1117/12.814684.full?SSO=1))

### Why we need that many frames?
Nyquist condition. Can be calculated...

## Why choose STORM?
>Unlike PALM that has fixed ON-state bleaching time, the ON/OFF states dynamics in dSTORM can be adjusted by external means. 
To capture single molecule signal, two conditions must be achieved. ([ref](https://www.nature.com/articles/nprot.2011.336.pdf))
>1. High enough contrast
>2. Only one ON-state molecule in the diffraction-limited region

#### The photoswitching mechanism (Theory)
###### 打561 Kaede會不會回到488的態? 也沒關係，還是在dark state
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

$\Rightarrow$ **Blinking rate** is dependent on $\lambda_3$ and labelling density.

[...]

### How many molecules do you need?
[Direct STORM](https://www.nature.com/articles/nprot.2011.336)
With an aim of 20-nm resolution, a fluorophore must be localized at least every 10 nm. In 2D, this means in $1\mu m^2$, there must be at least $(\frac{1\mu m}{10 nm})^2\approx10^4$ moleceles. In a diffraction-limited spot of size $250 nm$, there must be $600$ molecules but only one molecule can be in the ON state. This means that the **OFF state lifetime** should be at least 600 times longer than the **ON state life time**.  
![ON & OFF state](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274021654_1122525205211549_2958359896031346084_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Jqp_p3eLwf8AX-M2w7R&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIEcNA86NEAROLePkSPH_oNOhvVeXgNP87UoGMLaraecg&oe=62400AC2)
[...]

### How to determine the labeling density?
Let's assume the labeling density is $\frac{(L/d)^3}{L^3}=\frac{1}{d^3}$ 
$d=1,5,10,20,50,100nm$
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275395158_3097633807132677_5057225665692364082_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=gcFrQW0ezvgAX9VmzO4&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLccVTktG1s5lQiRkNarqzXR4MKJwHA3JUxl3C3rmVMkA&oe=6251BBD4)

#### Rh6G photophysical properties (Case study)

After several fitting procedures, we have

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274325058_926017408076972_7050144123343753985_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=2BW97AfH0y0AX89R9Bx&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLS3lFJTBFNkAqN1zHd1ecB9HOyLZ3PVWzvs0ANzAyycA&oe=624D1A14)

We can also obtain $k_{12}=\sigma_{exc}\times \frac{P}{\pi\omega_1^2}$

$\frac{P}{\pi\omega_1^2}$ needs to be expressed as photons per square meter per second. $P=P_{origin}*2.58*10^{18}$

#### DsRed photophysical properties (Case study)

#### Kaede photophysical properties (Case study)
[Photophysical properties of Kaede](https://ueaeprints.uea.ac.uk/id/eprint/53399/1/2015AddisonKPhD.pdf)
![Characterization of the Photoconversion on Reaction of the Fluorescent Protein Kaede on the Single-Molecule Level](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274309488_253777436833989_1708364374648674418_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=ae9488&_nc_ohc=p2HOGooN3joAX-Sj37B&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKuiFvSnQR6r_DNQu2sVH-9SV0d8IpCh5CpHH5qkuy-Cw&oe=6246EF1C)
![Han-Yuan's journal](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/273573200_376756070946666_2126222706031454664_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=WhExxP47MtsAX9VbkJB&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJ5xEjGf0X50k3ia8h9Z9K0Cu-IWP-o7eg8-K5rlBelRQ&oe=6245026A)
You can clearly see that the blinking dynamics is about submilliseconds. 250 ms exposure time is too long for resolving individual molecule. 
[...]

##### Intensity dependence of ACF (The most important application)
Here is the experimental results of ACF curve of red form Kaede when varying the excitation intensity (from $2.5$ to $78\frac{kW}{cm^2}$). 

After fitting with the model
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275184263_632338294498567_2914250142237772510_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=kwGErwIEvSAAX9wpAq6&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKUy8xS-TacV-8hBQtIsBIXUMJeuHYSrtyWHFA3KKByRg&oe=624F8332), where $\tau_i$ is the rate, and $F_i$ is the fraction, we have two blinking dynamics (i=2) with $\tau_1=6.5$ - $32$kHz(153$\mu s$-30$\mu s$), $F_1\approx30\%$, and $\tau_2=1.3$kHz - $10$kHz(769$\mu s$-100$\mu s$), $F_2\approx20\%$.
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/273648558_300396522012577_1102684933084334318_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=z9VyP9SEK5gAX-RrYIA&tn=kmMc2ol6ujtRzeuG&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLNAO7arsvHyt49Lwihhrm-Zxc1-WrLrwhwJqIOy_8e4Q&oe=6248DEB8)

### Related to speed issue: photon number
With neglegible fluorescent background and detection noise, the localization precision is $\mu\approx\frac{\sigma}{N}$, where $\sigma$ is the size of PSF, and $N$ is the number of photon detected. In typical PALM or FPALM, the frame rate is about 10-25 Hz to accomodate for the bleaching time of fluorophores. 

Papers:  
[3D STED](https://drive.google.com/file/d/15G1G0A-zgt5GrhK4TLFYyHvQrMD7oiez/view?usp=sharing)  
[Polarization-resolved two photon spinning disk](https://drive.google.com/file/d/1I7E_GrQpJe9I9jCjw4fikekqE2fGU0fL/view?usp=sharing)  
[Drosophila brain simulation](https://neurokernel.github.io/about.html)：羅中泉老師。  
[Drosophila as model animal1](https://www.jneurosci.org/content/33/45/17560), [2](https://pubmed.ncbi.nlm.nih.gov/20383202/)  
[Drosophila larvae imaging](https://elifesciences.org/articles/15567)