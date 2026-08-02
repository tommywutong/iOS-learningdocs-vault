---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Introduction/Intro.html
archived_at: '2026-07-18T03:28:52.207074Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# aurioTouch

|  |  |
| --- | --- |
| __Last Revision:__ | Version 5.0, 2016-08-12 Updated to Xcode 7, fixed deprecated API warnings and added NSMicrophoneUsageDescription string. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzxgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.11+, Xcode 7.3.1, iOS 9+, iOS SDK 9 or later |
| __Runtime Requirements:__ | iOS 9 or later |

aurioTouch demonstrates use of the remote i/o audio unit for handling audio input and output. The application can display the input audio in one of the forms, a regular time domain waveform, a frequency domain waveform (computed by performing a fast fourier transform on the incoming signal), and a sonogram view (a view displaying the frequency content of a signal over time, with the color signaling relative power, the y axis being frequency and the x as time). Tap the sonogram button to switch to a sonogram view, tap anywhere on the screen to return to the oscilloscope. Tap the FFT button to perform and display the input data after an FFT transform. Pinch in the oscilloscope view to expand and contract the scale for the x axis.

The code in aurioTouch uses the remote i/o audio unit (AURemoteIO) for input and output of audio, and OpenGL for display of the input waveform. The application also uses AVAudioSession to manage route changes (as described in the Audio Session Programming Guide).

[Next](main.m.md)

