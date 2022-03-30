##### KEY QUESTION: WHAT ARE GOOD IMAGING RESULTS?

>How to quantify resoltuion in localization images?
>- Localization precision?
>- Labeling density?

Can we generate a formula to calculate the resolution solely from the image?
### Fourier ring correlation (FRC)

The advantage of FRC[[Ref](https://www.nature.com/articles/nmeth.2448)]:
- Prior information free (localization precision, density,…)
- Based solely on image analysis

Suppose there is a set of localization emitters. We divide the emitters into two groups and construct two images according to the two groups.

#### Parameters
$f_1(\vec{r})$: the intensity function in the first image.
$f_2(\vec{r})$: the intensity function in the second image.
$\hat{f_1}(\vec{q})$: Fourier transform of $f_1(\vec{r})$
$\hat{f_2}(\vec{q})$: Fourier transform of $f_2(\vec{r})$
$\vec{q}$: spatial frequency with magnitude $|\vec{q}|$
The formula of FRC:
![](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/275520689_296608949246755_686138927508404033_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=BOORKIrvzDwAX91p4bm&_nc_ht=scontent-tpe1-1.xx&oh=03_AVJOj_99M2g8_K-ZHRVQ0xgeIpK0tlgOsw-GD6JPcv_YkA&oe=625C9789)
#### What is the physical meaning of FRC?
Original paper of FRC concept [[Ref](https://www.sciencedirect.com/science/article/pii/0304399187900106)].

[NPC paper](https://www.nature.com/articles/s41592-019-0574-9)

[WE Moerner review](https://pubs.acs.org/doi/10.1021/jacs.0c08178)