[Todo lists](https://docs.google.com/document/d/1PmqmAC3JLrxaWYusEgZz5_CUBiyhWrMrnnstpt6ula8/edit?usp=sharing)

## Deep tissue super-resolution imaging via two-photon spinning disk localization
[Photonic West](https://docs.google.com/document/d/1Y5SSFlGdQwiD2743RTZNmM7oJkpC0f3VwCBZsSFFnZw/edit?usp=sharing)

### Abstract
Recently, whole-*Drosophila*-brain structural mapping has been demonstrated with ~50-nm resolution, but not *in vivo*. In this work, we combine two-photon excitation into a spinning disk confocal setup to enable ~500 μm imaging depths in uncleared mouse brains (~100 μm in *Drosophila*), and wide-field optical sectioned detection, respectively. Through integration of photo-activated localization microscopy (PALM), which also reduces photodamage of the tissue, we achieve resolution down to ~50 nm in an intact *Drosophila* brain, pushing to the limit of imaging depth and resolution. Our work paves the way toward *in vivo* functional connectome studies. 

### Introduction

Super-resolution imaging avails the imaging resolution down to tens of nanometers. We have demonstrated whole brain structural mapping in a cleared *Drosophila* brain with ~50 nm resolution, but current optical clearing techniques do not allow *in vivo* observation. A technical milestone is to achieve *in vivo* whole brain imaging with similar resolution. Although *in vivo* super-resolution imaging has been realized, it is limited to thin samples. The underlying reason is that current state-of-the-art techniques rely on either saturation plus wavefront engineering or localization with blinking fluorophores. The former imaging depth is limited due to aberration or scattering in living tissues, and the latter suffers from lack of optical-sectioning ability.

In this work, we combine two-photon excitation into a spinning disk confocal setup to enable deep-tissue penetration and wide-field optical sectioned detection, respectively. The two-photon spinning disk microscope offers ~500 μm and ~100 μm imaging depths in uncleared mouse and *Drosophila* brains, similar to typical single-point detection two-photon microscopy. Through integration of photo-activated localization microscopy (PALM), which also reduces photodamage of the tissue, we achieve resolution down to ~50 nm in an intact *Drosophila* brain, pushing to the limit of imaging depth and resolution. More importantly, the protocol works for living brains, so our work paves the way toward *in vivo* functional connectome studies. 

## Why is blinking necessary?
refer to [nature protocol](https://www.nature.com/articles/nprot.2011.336.pdf)
To achieve single molecule imaging, blinking is necessary. Otherwise, it is very hard to distinguish single molecule. 

### How many molecules do you need?
With an aim of 20-nm resolution, a fluorophore must be localized at least every 10 nm. In 2D, this means in $1\mu m^2$, there must be at least $(\frac{1\mu m}{10 nm})^2\approx10^4$ moleceles. In a diffraction-limited spot of size $250 nm$, there must be $600$ molecules but only one molecule can be in the ON state. This means that the OFF state lifetime should be at least 600 times longer than the ON state life time.  
![ON & OFF state](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274021654_1122525205211549_2958359896031346084_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Jqp_p3eLwf8AX-M2w7R&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIEcNA86NEAROLePkSPH_oNOhvVeXgNP87UoGMLaraecg&oe=62400AC2)

### What is the lifetime of the molecule?
Unlike PALM that has fixed ON-state bleaching time, the ON/OFF states dynamics in dSTORM can be adjusted by external means. 
[...]
#### The photoswitching mechanism (Theory)
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
A typical relation between $\lambda_3$(related to flickering rate) and intensity.
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274652847_5168091999896421_1049625651085026328_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=PeWX2R0j-bEAX-oltq3&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIFIzqhBILNuxOd2LnCLmNQdNVbRlczL6Lqcqo_JEcYiw&oe=624DFFA2)
#### Rh6G photophysical properties (Case study)

After several fitting procedures, we have

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274325058_926017408076972_7050144123343753985_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=2BW97AfH0y0AX89R9Bx&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLS3lFJTBFNkAqN1zHd1ecB9HOyLZ3PVWzvs0ANzAyycA&oe=624D1A14)

We can also obtain $k_{12}=\sigma_{exc}\times \frac{P}{\pi\omega_1^2}$

#### DsRed photophysical properties (Case study)

#### Kaede photophysical properties (Case study)
[Photophysical properties of Kaede](https://ueaeprints.uea.ac.uk/id/eprint/53399/1/2015AddisonKPhD.pdf)
![Characterization of the Photoconversion on Reaction of the Fluorescent Protein Kaede on the Single-Molecule Level](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274309488_253777436833989_1708364374648674418_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=ae9488&_nc_ohc=p2HOGooN3joAX-Sj37B&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKuiFvSnQR6r_DNQu2sVH-9SV0d8IpCh5CpHH5qkuy-Cw&oe=6246EF1C)
![Han-Yuan's journal](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/273573200_376756070946666_2126222706031454664_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=WhExxP47MtsAX9VbkJB&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJ5xEjGf0X50k3ia8h9Z9K0Cu-IWP-o7eg8-K5rlBelRQ&oe=6245026A)
You can clearly see that the blinking dynamics is about submilliseconds. 250 ms exposure time is too long for resolving individual molecule. 
[...]

##### Intensity dependece of ACF (The most important application)
Here is the experimental results of ACF curve of red form Kaede when varying the excitation intensity (from $2.5$ to $78\frac{kW}{cm^2}$). 

After fitting with the model
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275184263_632338294498567_2914250142237772510_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=kwGErwIEvSAAX9wpAq6&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKUy8xS-TacV-8hBQtIsBIXUMJeuHYSrtyWHFA3KKByRg&oe=624F8332), where $\tau_i$ is the rate, and $F_i$ is the fraction, we have two blinking dynamics (i=2) with $\tau_1=6.5$ - $32$kHz(153$\mu s$-30$\mu s$), $F_1\approx30\%$, and $\tau_2=1.3$kHz - $10$kHz(769$\mu s$-100$\mu s$), $F_2\approx20\%$.
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/273648558_300396522012577_1102684933084334318_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=z9VyP9SEK5gAX-RrYIA&tn=kmMc2ol6ujtRzeuG&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLNAO7arsvHyt49Lwihhrm-Zxc1-WrLrwhwJqIOy_8e4Q&oe=6248DEB8)


### How to determine the labeling density?

### Related to speed issue: photon number
With neglegible fluorescent background and detection noise, the localization precision is $\mu\approx\frac{\sigma}{N}$, where $\sigma$ is the size of PSF, and $N$ is the number of photon detected. In typical PALM or FPALM, the frame rate is about 10-25 Hz to accomodate for the bleaching time of fluorophores. 

Papers:  
[3D STED](https://drive.google.com/file/d/15G1G0A-zgt5GrhK4TLFYyHvQrMD7oiez/view?usp=sharing)  
[Polarization-resolved two photon spinning disk](https://drive.google.com/file/d/1I7E_GrQpJe9I9jCjw4fikekqE2fGU0fL/view?usp=sharing)  
[Drosophila brain simulation](https://neurokernel.github.io/about.html)：羅中泉老師。  
[Drosophila as model animal1](https://www.jneurosci.org/content/33/45/17560), [2](https://pubmed.ncbi.nlm.nih.gov/20383202/)  
[Drosophila larvae imaging](https://elifesciences.org/articles/15567)