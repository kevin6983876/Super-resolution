[Presentation file](https://docs.google.com/presentation/d/1o4MUe4M_gPMq75otwBRVJiN_-dqbV-rV/edit?usp=sharing&ouid=102138553756025019371&rtpof=true&sd=true)
> Presenting paper: Super-resolution Microscopy with Single Molecules in Biology and Beyond−Essentials, Current Trends, and Future Challenges

First author: Leonhard Möckl
Institution: Max Planck Institute for the Science of Light (MPL)
Research: he used single-molecule techniques to investigate the glycocalyx and furthermore developed deep-learning based approaches for single-molecule studies.
![](https://mpl.mpg.de/fileadmin/_processed_/c/3/csm_Bild_Leonhard_daeaba0f79.jpg)

Corresponding auther: W.E. Moerner
Institute: Stanford Chemistry
Research: he has conducted resesarch in physical chemistry, biophysics, and the optical properties of single molecules, and is actively involved in the development of 2D and 3D super-resolution imaging for cell biology.
![](https://chemistry.stanford.edu/sites/g/files/sbiybj11986/f/styles/large-square/public/c39bebe712744602a57711150967c60a.jpg?itok=QNZOESMT)

### Background
#### First revolution of single molecule imaging
##### Problem
To sense a single molecule, it must be efficiently excited, and the emiited signal must be recorded with high sensitivity. 

Previous method: ensemble average $\rightarrow$ much detail is lost. 

##### Solution
Laser and EMCCD camera. 

#### Second revolution of single molecule imaging: single molecule super-resolution imaging
##### Problem: blinking and fluctuation
The fluctuation or blinking of the single molecule was first thought as a problem since during camera capture, some frames will be lack of signals. 

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/277077683_435135045039643_8921503517217314163_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=qqlzRxmdKdUAX84IiJe&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLO2RYES47UsJNbWxnnUjgVXfhE873LVdMc2WH9uj5yGg&oe=626AB629)
*A sequence of 100 images of the emission from a single green fluorescent protein mutant molecule trapped in a gel. Each frame corresponds to a 100-ms exposure with a 488-nm-wavelength laser in a total-internal-reflection geometry.*
[Source](https://www.science.org/doi/full/10.1126/science.277.5329.1059)

##### Problem: imaging resolution limit
When two single emitters are two close, we cannot distinguish two signals due to the interference of the two. 
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/276301958_687976215858028_67602249707925598_n.png?_nc_cat=100&ccb=1-5&_nc_sid=ae9488&_nc_ohc=4odhGeqbeKQAX_opZXJ&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKU__mmBQfMnA4Ks2gk1TccO41b9b4jVWzar67S88151g&oe=62678493)
[Source](https://www.dl.begellhouse.com/journals/4b27cbfc562e21b8,4566441101015d3d,2c0b905277d0ad89.html)

##### Solution
The blinking behavior turns out to be useful in solving the problem of resolution limit. Here are the procedures. When the molecule is in the bright state, we can determine the position of the molecule in a precise manner (a step to be called as *localization*.) During the imaging, we can localize many molecules and then reconstruct a high-resolved image.  
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/277146833_2766380623668453_8889030564926801383_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=bOKyxDZhC0oAX_OP4eQ&tn=keTzxKsx3oMeGvL-&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIdwC16HdCXatI5wJNNfS0eP0rmnkgqBpS9o2lJzkOTCw&oe=6269A51C)
[Source](https://pubs.acs.org/doi/full/10.1021/jacs.0c08178)

##### Application 
Using single molecule super-resolution imaging, we can visualize previous unresolved structures. 
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/276975795_700827061059282_7235732115933631759_n.png?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=fJmvSd-v5LUAX_3C9JC&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJZgF_O8mnH6A4IPRKwBYoGIjl1LkkbfJs8kz8OKAxD6g&oe=6268719A)
[Source](https://pubs.acs.org/doi/full/10.1021/jacs.0c08178)

### Experimental considerations
There are three *component* in the single molecule super-resolution microscope. 
1. The sample
2. The optical setup
3. Data analysis

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/277455202_708690973818570_6489683772679116518_n.png?_nc_cat=100&ccb=1-5&_nc_sid=ae9488&_nc_ohc=7gd90mHZTgQAX971OyQ&_nc_ht=scontent-tpe1-1.xx&oh=03_AVIN4bZpmsSV0P1727VyjlrtyAXm2K9I2kBzK8_ZztW4Dw&oe=6269DF19)

#### The sample
##### Optimization consideration 1: the dye.
###### High photostability.
Cryogenic (low temperature) imaging
###### High quantum yield.
###### Good blinking statistics.
1. **Photoactivation**: a dye is converted from a dark state to a bright state by another beam.
2. **Photoinduced blinking**: In principle, all types of dyes has blinking behavior. However,  photophysical condition of desirable blinking statistics needs to be explored.  
3. **PAINT**: a diffusing fluorophore can bind to the target structure and emit a burst of fluorescence. This method uncouples the blinking statstics and the specific dye. 

A good blinking statistics should obey Nyquist-Shannon sampling criterion
##### Optimization consideration 2: labeling methods
Common strategy: immunochemistry protocol

Problem: the size of the antibody is about $10$ nm. In a densely-packed region, the labeling may be unspecific. 
**Try to reduce the size of antibody**

Triad of a good localization image:
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275910520_367589885255513_4723944715057726317_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_ohc=sksKLRAN590AX-ZCcsL&_nc_ht=scontent-tpe1-1.xx&oh=03_AVKKctc4QERqsKDb6dGCX86D1uAj92A1EZqz4jbZWKtbew&oe=6267ADBA)

##### Optimization consideration 3: Tissue section
Problem: unspecific bindings, autofluorescence, strong aberration.
**According to this perspective, this is the hardest part of optimization.**

#### Optical setup
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/277487055_950346965846459_2365840978413471170_n.png?_nc_cat=103&ccb=1-5&_nc_sid=ae9488&_nc_ohc=J8ESvQIfoWQAX9TgYbt&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLvHhJaktmHYemttAIb2JwGZ3PUKlNCWrmjVNPfhYUf3g&oe=6269070C)
#### Data analysis
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/276970238_1729710890706166_6612078214859940937_n.png?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=aSK7FhgTZzwAX-Tn6F3&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJKz40Qaxw_fyTquWG7pJbU0uJ3cW1h_yp7Fd74_4cCaQ&oe=626A1320)

### Where is the territory of my study?
- Optical setup
    - setup design
      - two-photon spinning-disk excitation

![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/276945180_511147343839337_3667453461422940419_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=TWZB5zt4clkAX-jCCnA&_nc_ht=scontent-tpe1-1.xx&oh=03_AVLbuALqQVvO5nsgfuljvCjle8Ti_CNm2ToQHeZ7GZwavw&oe=626A3196)
[Source](https://www.jstage.jst.go.jp/article/analsci/31/4/31_307/_article/-char/ja/)

### Back to the fundamentals
What is really needed to achieve super-resolution via localization of an individual signal? 
1. An emitter
2. The emitter must undergo detetable changes, yielding non-overlapping signals in the spatial (or another imaging) dimension.
3. The expected profile of the emission on the detector must be known reasonably well to allow for fitting of an appropriate model function to extract the single emitter position precisely.
4. The time scale of the emission on−off process must be fast enough. 

For example, [single molecular spin](https://www.nature.com/articles/363242a0).