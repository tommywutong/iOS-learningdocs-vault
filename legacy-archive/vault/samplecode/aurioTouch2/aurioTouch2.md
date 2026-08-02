---
title: aurioTouch2
apple_id: DTS40011369
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2011-12-06'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch2/Introduction/Intro.html
archived_at: '2026-07-18T03:28:54.103790Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

Relevant replacement documents include:

- [https://developer.apple.com/library/ios/samplecode/aurioTouch/Introduction/Intro.html#//apple_ref/doc/uid/DTS40007770](https://developer.apple.com/library/ios/samplecode/aurioTouch/Introduction/Intro.html#//apple_ref/doc/uid/DTS40007770)

# aurioTouch2

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2011-12-06 iOS 5.0+ AURemoteIO example to monitor audio input and play it out (duplex audio I/O) |
| __Build Requirements:__ | XCode 4.0 or later, iOS SDK 5.0 or later |
| __Runtime Requirements:__ | iOS 5.0 or later |

aurioTouch2 demonstrates use of the remote i/o audio unit (AURemoteIO) for handling audio input and output. The application can display the input audio in one of the forms, a regular time domain waveform, a frequency domain waveform (computed by performing a fast fourier transform on the incoming signal), and a sonogram view (a view displaying the frequency content of a signal over time, with the color signaling relative power, the y axis being frequency and the x as time).

The code in aurioTouch2 uses the remote i/o audio unit (AURemoteIO) for input and output of audio, and OpenGL for display of the input waveform. The application also uses Audio Session Services to manage route changes (as described in Core Audio Overview).

aurioTouch2 supports iOS 5 or later.

[Next](ReadMe.txt.md)

