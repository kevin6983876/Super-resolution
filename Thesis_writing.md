[Todo lists](https://docs.google.com/document/d/1PmqmAC3JLrxaWYusEgZz5_CUBiyhWrMrnnstpt6ula8/edit?usp=sharing)

## Deep tissue super-resolution imaging via two-photon spinning disk localization
[Photonic West](https://docs.google.com/document/d/1Y5SSFlGdQwiD2743RTZNmM7oJkpC0f3VwCBZsSFFnZw/edit?usp=sharing)

### Abstract
Recently, whole-*Drosophila*-brain structural mapping has been demonstrated with ~50-nm resolution, but not *in vivo*. In this work, we combine two-photon excitation into a spinning disk confocal setup to enable ~500 μm imaging depths in uncleared mouse brains (~100 μm in *Drosophila*), and wide-field optical sectioned detection, respectively. Through integration of photo-activated localization microscopy (PALM), which also reduces photodamage of the tissue, we achieve resolution down to ~50 nm in an intact *Drosophila* brain, pushing to the limit of imaging depth and resolution. Our work paves the way toward *in vivo* functional connectome studies. 

### Introduction

Super-resolution imaging avails the imaging resolution down to tens of nanometers. We have demonstrated whole brain structural mapping in a cleared *Drosophila* brain with ~50 nm resolution, but current optical clearing techniques do not allow *in vivo* observation. A technical milestone is to achieve *in vivo* whole brain imaging with similar resolution. Although *in vivo* super-resolution imaging has been realized, it is limited to thin samples. The underlying reason is that current state-of-the-art techniques rely on either saturation plus wavefront engineering or localization with blinking fluorophores. The former imaging depth is limited due to aberration or scattering in living tissues, and the latter suffers from lack of optical-sectioning ability.

In this work, we combine two-photon excitation into a spinning disk confocal setup to enable deep-tissue penetration and wide-field optical sectioned detection, respectively. The two-photon spinning disk microscope offers ~500 μm and ~100 μm imaging depths in uncleared mouse and *Drosophila* brains, similar to typical single-point detection two-photon microscopy. Through integration of photo-activated localization microscopy (PALM), which also reduces photodamage of the tissue, we achieve resolution down to ~50 nm in an intact *Drosophila* brain, pushing to the limit of imaging depth and resolution. More importantly, the protocol works for living brains, so our work paves the way toward *in vivo* functional connectome studies. 

### Trade-off between excitation power and sample collapse

## Why is blinking necessary?
To achieve single molecule imaging, blinking is necessary. Otherwise, it is very hard to distinguish single molecule. 

### How many molecules do you need?
With an aim of 20-nm resolution, a fluorophore must be localized at least every 10 nm. In 2D, this means in $1\mu m^2$, there must be at least $(\frac{1\mu m}{10 nm})^2\approx10^4$ moleceles. In a diffraction-limited spot of size $250 nm$, there must be $600$ molecules but only one molecule can be in the ON state. This means that the OFF state lifetime should be at least 600 times longer than the ON state life time.  
![ON & OFF state](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/274021654_1122525205211549_2958359896031346084_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Jqp_p3eLwf8AX-M2w7R&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIEcNA86NEAROLePkSPH_oNOhvVeXgNP87UoGMLaraecg&oe=62400AC2)

### What is the lifetime of the molecule?
Unlike PALM that has fixed ON-state bleaching time, the ON/OFF states dynamics in dSTORM can be adjusted by external means. 

#### The photoswitching mechanism
Alexa Fluor and ATTO dyes can be photoreduced in the presence of electron donors (GSH or Trp), especially in a basic condition (pH~9).
![Typical photoswitching mechanism of Alexa Fluor](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/273553073_423614409536286_5486102589772724378_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_ohc=TwfHBIH-kqEAX9UNXmF&_nc_ht=scontent-tpe1-1.xx&oh=03_AVINNhKg9ONqG_xfQgQCCIHnIbpNeOXBaowy4oGL6KGqXA&oe=6243549D)

$k_{exc}$:??
$k_{fl}$:??
$k_{isc}$:??


### How to determine the labeling density?

### Related to speed issue: photon number
With neglegible fluorescent background and detection noise, the localization precision is $\mu\approx\frac{\sigma}{N}$, where $\sigma$ is the size of PSF, and $N$ is the number of photon detected. In typical PALM or FPALM, the frame rate is about 10-25 Hz to accomodate for the bleaching time of fluorophores. 

Papers:  
[3D STED](https://drive.google.com/file/d/15G1G0A-zgt5GrhK4TLFYyHvQrMD7oiez/view?usp=sharing)  
[Polarization-resolved two photon spinning disk](https://drive.google.com/file/d/1I7E_GrQpJe9I9jCjw4fikekqE2fGU0fL/view?usp=sharing)  
[Drosophila brain simulation](https://neurokernel.github.io/about.html)：羅中泉老師。  
[Drosophila as model animal1](https://www.jneurosci.org/content/33/45/17560), [2](https://pubmed.ncbi.nlm.nih.gov/20383202/)  
[Drosophila larvae imaging](https://elifesciences.org/articles/15567)