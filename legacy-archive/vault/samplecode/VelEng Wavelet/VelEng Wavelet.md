---
title: VelEng Wavelet
apple_id: DTS10000460
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VelEng_Wavelet/Introduction/Intro.html
archived_at: '2026-07-18T03:27:45.766176Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](source-BasicDebugHeaders.h.md)

# VelEng Wavelet

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 This demonstrates a Velocity Engine (G4) implementation of wavelet processing of color images |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon G4 |

There are various approaches to wavelet processing of color images, and machine architecture dictates in large measure which algorithm is optimal. This sample is a Velocity Engine (G4) implementation in which pixels are processed as four-dimensional (RGBA) vector entities. In this mode the vector machinery performs the (Daubechies D4) wavelet algebra in only three vector operations per pixel. We also implemented a more standard, channel-correlation scenario, with YUV-decomposed RGB images (with UV sub-sampling) and a biorthogonal (Burt 5/7) wavelet transform applied thrice. A key to these fast vector implementations is the adoption of certain rational approximations-we call "shift-rational" forms-to the true wavelet coefficients, allowing for efficient Velocity Engine arithmetic. Other Velocity Engine enhancements include very fast subsampling for the UV channels, via vector-average instructions. Timing experiments show a Velocity Engine speedup of 5x or more over corresponding scalar (G3) implementation in the RGBA approach. For the YUV approach, the speedup is likewise impressive, with a complete inverse-wavelet-YUV image reconstruction on a 320-by-240 full color image taking less than 0.005 second on 300 MHz. G4. Requirements: G4 Keywords: Velocity Engine, AlitVec, Wavelet, Daubechies,

[Next](source-BasicDebugHeaders.h.md)

