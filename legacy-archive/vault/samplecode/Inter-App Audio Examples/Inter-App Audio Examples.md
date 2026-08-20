---
title: Inter-App Audio Examples
apple_id: DTS40013418
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2014-03-24'
source_url: https://developer.apple.com/library/archive/samplecode/InterAppAudioSuite/Introduction/Intro.html
archived_at: '2026-07-18T03:13:02.068335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Inter-App Audio Examples

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1.2, 2014-03-24 Updated for 7.1 SDK and Xcode 5.1. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbrhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.1 or later; iOS SDK 7.1 or later. |
| __Runtime Requirements:__ | iOS 7.0 or later. |

This suite of samples includes three projects that together illustrate Inter-App Audio feature.

Inter-App Audio allows audio apps that are instruments, effects, or generators to publish an output object which can be used by other audio apps. An app that publishes an output is called a node. An app that connects and uses one or more nodes is called a host.

Included in this suite are:

InterAppAudioHost - This app acts as a host for the two included node projects, InterAppAudioDelay and InterAppAudioSampler.

InterAppAudioDelay - This app acts as a node and illustrates how to publish and control a delay effect that can be used by another app. On its own, this app does not produce sound. Use it in conjunction with the InterAppAudioHost app.

InterAppAudioSampler - This app is a sampler acts as a node and publishes itself as a remote instrument and a generator. InterAppAudioHost uses InterAppAudioSampler as a remote instrument, which then plays audio upon receiving MIDI events from the host.

[Next](ReadMe.txt.md)

