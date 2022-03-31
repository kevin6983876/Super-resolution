Title: Microscope alignment using real-time imaging FCS

#### Problem
To calculate correlation functions, one has to record the data and analyze the data *in sequence*. Such acquisition and data analysis should repeat many times, which takes minites in Imaging FCS. 

#### Contribution: direct camera readout
1. Fast data acquisition and real-time read-out of images enable users to judge the image quality during the acquisition. 

#### Methods
##### Software

[...]
4 modes:
1. live video mode
2. single capture mode
3. calibration mode: evaluate the data online
4. FCS acquisition mode

##### Theory
FCS curves have two main parameters: 
1. Width = the average time $\tau_D$ diffusing particles need to transit through the observation volume
   1. $\tau_D\propto\omega^2$, where $\omega$ is the $e^{-2}$ radius of the observation volume. 
   2. The smaller the width, the smaller the volume, and hence the better the alignment.
2. Amplitude $G(0)$.
   1. The FCS amplitude is inversely proportional to the number of particles, $N$, in the observation volume. 
   2. $G_{2D}(0)=\frac{1}{N}\propto\frac{1}{\omega^2}$, where $\omega$ is the $e^{-2}$ radius of the observation volume. 
   3. The larger the amplitude, the smaller the volume, and hence the better the alignment. 

In general, amplitude is more sensitive to the volume size except when the background is strong. 

#### Results
With the advance of camera acquisition rate, researchers can now compute correlation functions for each pixel and can utilize this correlation functions for alignment. 
##### Long-term imaging FCS measurement
> In page 3, The current program displays the development of correlation functions live, obtains correlation functions of selected ROI at user-defined time intervals and registers plots of average **D** and **N** to help the user decide whether the experiment should continue, need to be stopped, or adjustments need to be made.
> I guess D is diffusion coeffient and N is the number of particles. They should be written. 

[...]
##### Aligning TIRF

[...]
##### Aligning light sheet
[...]
##### Aligning for dual color experiment
[...]


#### Conclusion
Real-time calculations of temporal and spatial correlation functions.