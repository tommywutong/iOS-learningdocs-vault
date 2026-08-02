---
title: VelEng FFT
apple_id: DTS10000458
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VelEng_FFT/Introduction/Intro.html
archived_at: '2026-07-18T03:27:42.119989Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Test%20vBigDSP.c.md)

# VelEng FFT

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 G4 Velocity Engine implementation of Fast Fourier Transform (FFT) and associated convolution/correlation routines. |
| __Build Requirements:__ | Mac OS X, Xcode 2.2 |
| __Runtime Requirements:__ | Carbon Altivec |

G4 Velocity Engine implementation of fast Fourier transform (FFT) and associated convolution/correlation routines. Though arbitrary signal lengths (i.e. all powers of 2) are handled, our design emphasis is on very long signals (length N >= 2^16 and on into the millions), for which cache considerations are paramount. The core of the library is a particular variant of full-complex FFT that for signal length N = 2^10 executes at 1.15 giga ops (500 MHz G4). This cache-friendly, core FFT plays a dominant role in the long-signal cases such as two-dimensional FFT and convolution. More important perhaps than the core performance benchmark is the manner in which one can sift through the myriad prevailing (and new) FFT frameworks, to arrive at a suitable such framework for the Velocity Engine. Requirements: G4 Keywords: Velocity Engine, Altivec, FFT, Fast Fourier Transform

[Next](Test%20vBigDSP.c.md)

