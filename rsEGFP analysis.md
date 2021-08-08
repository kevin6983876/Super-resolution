### Test of its photoswitchability among different aqueous environments
#### Date: 2021/08/05
#### [Source data](https://drive.google.com/drive/folders/10tY20jet_P9uzQImR_vD4n9jD1AVueYX?usp=sharing)
#### Experimental setup: 
- Andor Spinning disk
- Objective lens: 40X silicone oil immersion(n=1.406), NA = 1.25
- Camera: 
  - Zyla4
- Sample conditions

|Sample|PA|PBS|FC|
|----|----|------|----|
|PBS|X|V|X|
|PA+PBS|V|V|X|
|PA+FC|V|X|V|
- Genotype 

![Picture](https://lh6.googleusercontent.com/TV3AiHvKeGxcnTOA1PpWsJXOZVjeF_6u88QMOocujZ9zYSkz2RKtyOeS46JzhH8U7XJPlzRZmW74Z0WZE4ypVyRP8EqvB2GmzeuW2K8qdV2-ZmWeaOZuJT5tc823rkNFsA=w1280)

#### Results
- Excitation conditions

|Item|Period 1|Period 2|Period 3|Period 4|
|----|----|---|---|----|
|Laser|488|488|405|488|
|Laser power|100%|100%|90%|100%|
|Exposure time|0.25s|N.A|0.1s|0.25s|
|Frames|500|5min|500|200+|

|Item|Period 5|
|----|-------|
|Laser*|488/405|
|Laser power|50%/100%|
|Exposure time|0.1s/0.2s|
|Frames|500|

\*lasers are shined alternatively

|PBS|PA+PBS|PA+FC|
|---|---|---|
|[Figure 1](https://drive.google.com/file/d/1GESbU9k7TRpTLKJ9IRVhaYdFNiP8-9-5/view?usp=sharing)|[Figure 2](https://drive.google.com/file/d/1yfeM4A_3Z3bu04pm6eeHaTHDiy_pFWEu/view?usp=sharing)|[Figure 3](https://drive.google.com/file/d/18eITysKapninKHygN7QHNKNW8dKt249R/view?usp=sharing)|

scale bar = 100 um

<img src="https://lh3.googleusercontent.com/aZkt7XWKLu4vAc2se5ZkzYimg9MKnpFMzkV3coPBTXttgh2EhKCuu8djoo0WcmSSjEeAgI39-A-eaMWOcoZMVjY8x4aBAdq0iLF_0-mvgjDXAgdCAFnFVY0oYlttzGE2JA=w1280" width="600"> Figure 4

<img src="https://lh5.googleusercontent.com/XboX2pMGkA5F0Jsw78ZNszlT6jchD1wYgU59GW2Rw292Ek4QVrOXcBgx2B3VR40ZFFXqWJjGNig1FfO3jD5xfZj6FQ9ARPeCC6gC95yaAP1WXs10ae2BgxPTJwKGVyyFGw=w1280" width="600"> Figure 5

#### Discussion
Keeping all excitation conditions fixed, we can see much more fluorophores are switched on again in the sample with PA+FC immersion (Figure 4). 
When 488-nm and 405-nm lasers are shined alternatively, sample with PA+FC experiences the largest signal increase compared to that with PBS or PA+PBS (Figure 5). 

##### Data fitting

rsEGFP<sub>on</sub> &rlarr; rsEGFP<sub>off</sub>

$k_+$: forward rate constant, is dependent on light intensity

$k_-$: backward rate constant

$\frac{d[rsEGFP_{on}]}{dt}=-k_+[rsEGFP_{on}]+k_-[rsEGFP_{off}]$

$\frac{d[rsEGFP_{off}]}{dt}=k_+[rsEGFP_{on}]-k_-[rsEGFP_{off}]$

