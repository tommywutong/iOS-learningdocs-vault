---
title: FilterDemo
apple_id: DTS10003570
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-08-28'
source_url: https://developer.apple.com/library/archive/samplecode/FilterDemo/Introduction/Intro.html
archived_at: '2026-07-18T03:08:31.500877Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AUPublic-AUBase-AUBase.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# FilterDemo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.01, 2012-08-28 Analyzer errors are fixed. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjxgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.7 or later Xcode 4.3 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

This project will build a simple Audio Unit effect and a Cocoa UI to go along with it. The effect is a simple resonant low-pass filter which has two parameters: cutoff frequency and resonance. It demonstrates how to implement a custom property for communicating information between the Audio Unit and its view. Also, it shows how to publish factory presets. The Cocoa view features a resizeable real-time display of the frequency-response curve which can be directly manipulated through a control point.

[Next](AUPublic-AUBase-AUBase.cpp.md)

