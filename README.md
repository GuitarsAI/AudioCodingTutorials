# Audio Coding Video Tutorials and Python Notebooks
<p align="center">
    <img src="./images/ac_header.png">
</p>

#### Prof. Dr. -Ing. Gerald Schuller <br> Jupyter Notebooks and Videos: Renato Profeta
[Applied Media Systems Group](https://www.tu-ilmenau.de/en/applied-media-systems-group/) <br>
[Technische Universität Ilmenau](https://www.tu-ilmenau.de/)

# Content
## 01 Basics of Multirate Signal Processing:<br> [![NBViewer](https://badgen.net/badge/Launch/on%20NBViewer/blue?icon=terminal)](https://nbviewer.jupyter.org/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_01_Basics_Multirate.ipynb)[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GuitarsAI/AudioCodingTutorials/master?filepath=AC_01_Basics_Multirate.ipynb)[![Google Colab](https://badgen.net/badge/Launch/on%20Google%20Colab/black?icon=terminal)](https://colab.research.google.com/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_01_Basics_Multirate.ipynb)[![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://youtu.be/Tp96ICZ_pMg)

  - Sampling
    - Sampling a Discrete Time Signal
    - Downsampling
    - Upsampling
    - Real-Time Python Example: Sampling
  - Effects in the z-Domain
  - Modulation
    - Real-Time Python Example: Modulating a Speech Signal
  - Mid-rise and Mid-tread quantization
    - Real-Time Python Example: Quantization

## 02 Filter Banks I :<br> [![NBViewer](https://badgen.net/badge/Launch/on%20NBViewer/blue?icon=terminal)](https://nbviewer.jupyter.org/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_02_FilterBanks1.ipynb)[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GuitarsAI/AudioCodingTutorials/master?filepath=AC_02_FilterBanks1.ipynb)[![Google Colab](https://badgen.net/badge/Launch/on%20Google%20Colab/black?icon=terminal)](https://colab.research.google.com/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_02_FilterBanks1.ipynb)[![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://youtu.be/Zk8Oum6LtUc)

  - Filter Banks
  - Downsampling
  - Upsampling
  - Filter Bank Structure
  - Perfect Reconstruction
  - Analysis Filter Bank
  - Synthesis Filter Bank
  - Polyphase
  - Transforms as Filter Banks
  - Real-Time Python Examples

## 03 Filter Banks II :<br> [![NBViewer](https://badgen.net/badge/Launch/on%20NBViewer/blue?icon=terminal)](https://nbviewer.jupyter.org/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_03_FilterBanks2.ipynb)[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GuitarsAI/AudioCodingTutorials/master?filepath=AC_03_FilterBanks2.ipynb)[![Google Colab](https://badgen.net/badge/Launch/on%20Google%20Colab/black?icon=terminal)](https://colab.research.google.com/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_03_FilterBanks2.ipynb)[![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://youtu.be/f1ykTtvWkwM)

  - Modulated Filter Banks - Extending the DCT
  - Modulated Filter Banks
    - Frequency Shifts
    - The Window Function
  - Fast Implementation: Analysis Polyphase Matrix
  - The MDCT Filter Bank
  - Graphical Interpretation of Analysis Matrix  𝐹𝑎
  - MDCT, Perfect Reconstruction
  - MDCT Filter Banks, Sine Window
    - Sine-Window Frequency Response
  - MDCT, Advantages
  - MDCT Filter Banks, Impulse Responses
  - MDCT Filter Banks, Frequency Responses
  - MDCT: Python Examples
    - MDCT Fast Implementation
  - Extending the Length of the MDCT
    - Zero-Delay Matrix
    - Maximum-Delay Matrix
    - Design Method
    - Real-Time Example
    
## 03b Filter Banks III :<br> [![NBViewer](https://badgen.net/badge/Launch/on%20NBViewer/blue?icon=terminal)](https://nbviewer.jupyter.org/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_03b_FilterBanks3.ipynb)[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GuitarsAI/AudioCodingTutorials/master?filepath=AC_03b_FilterBanks3.ipynb)[![Google Colab](https://badgen.net/badge/Launch/on%20Google%20Colab/black?icon=terminal)](https://colab.research.google.com/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_03b_FilterBanks3.ipynb)[![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://youtu.be/eLHqX6qZcX4)

  - Block Switching
  - Wavelets, QMF (Quadradutre Mirror Filter) Filter Banks
    - QMF (Quadrature Mirror Filter)
  - CQMF: Conjugate QMF
  - Pseudo-QMF (PQMF)
    - PQMF used in MPEG4
    
## 04 Psychoacoustics :<br> [![NBViewer](https://badgen.net/badge/Launch/on%20NBViewer/blue?icon=terminal)](https://nbviewer.jupyter.org/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_04_psychoAcoustics.ipynb)[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GuitarsAI/AudioCodingTutorials/master?filepath=AC_04_psychoAcoustics.ipynb)[![Google Colab](https://badgen.net/badge/Launch/on%20Google%20Colab/black?icon=terminal)](https://colab.research.google.com/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_04_psychoAcoustics.ipynb)[![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://youtu.be/Dp9NhFShaPM)

  - Block Diagram of a Perceptual Audio Encoder
  - Structure of the Human Ear
    - Cochlea
    - Organ of Corti
  - Preprocessing of Sound in the Peripheral System
  - Information Processing in the Auditory System
  - Sound Perception
    - Frequency and Level Range of Human Hearing
    - Threshold in Quiet or the Absolute Threshold
    - Hearing Threshold and Age
    - Loudness
    - Critical Bands
        - Frequency Grouping in Human Hearing
        - Excursus - Critical Bands and Loudness
    - Bark Scale
    - Masking
        - Masking of Pure Tones by Noise -Broad-Band Noise
        - Masking of Pure Tones by Noise -Narrow-Band Noise
        - Masking of Pure Tones by Low-Pass or High-Pass Noise
        - Masking of Pure Tones by Pure Tone
        - Masking of Pure Tone by Complex Tones
        - Tonality
        - Masking - Spreading Function
        - Calculating the Masking Threshold
        - In-Band Making
        - Masking Neighboring Bands
        - Temporal Masking Effects
        
## 05 Psychoacoustics Models :<br> [![NBViewer](https://badgen.net/badge/Launch/on%20NBViewer/blue?icon=terminal)](https://nbviewer.jupyter.org/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_05_psychoAcousticsModels.ipynb)[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GuitarsAI/AudioCodingTutorials/master?filepath=AC_05_psychoAcousticsModels.ipynb)[![Google Colab](https://badgen.net/badge/Launch/on%20Google%20Colab/black?icon=terminal)](https://colab.research.google.com/github/GuitarsAI/AudioCodingTutorials/blob/master/AC_05_psychoAcousticsModels.ipynb)[![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://youtu.be/CulE7VNtf5Q)

    - Spreading Function: Python Example
    - Masking Neighboring Bands Non-Linear Superposition
    - Bark Scale Approximations:
        - Zwicker&Terhard
        - Traunmueller
        - Schröder
    - Bark Scale Approximations: Comparisons
    - Bark Scale Mapping
    - Mapping from Bark scale back to Linear
    - Hearing Threshold in Quiet
    - The Complete Psycho-Acoustic Model
    - Physical Models of Hearing
    
 # YouTube Playlist
 [![Youtube](https://badgen.net/badge/Launch/on%20YouTube/red?icon=terminal)](https://www.youtube.com/playlist?list=PL6QnpHKwdPYjRWkWLswWmxFrDmj6leRwh)
 
# Requirements
Please check the following files at the 'binder' folder:
  - environment.yml
  - postBuild
  
 # Note
 Examples requiring a microphone will not work on remote environments such as Binder and Google Colab. 
