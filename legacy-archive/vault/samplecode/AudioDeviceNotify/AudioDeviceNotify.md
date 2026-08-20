---
title: AudioDeviceNotify
apple_id: DTS10003925
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2012-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/AudioDeviceNotify/Introduction/Intro.html
archived_at: '2026-07-18T03:01:22.544414Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AudioDeviceNotify

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.1.1, 2012-11-29 Editorial [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojsguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.5 or later, OS X 10.7 SDK or later. |
| __Runtime Requirements:__ | OS X 10.7 or later. |

Demonstrates how to enumerate all audio devices attached to a system and display each device's basic information (id, name, number of channels). This sample also demonstrates how to setup and receive notifications from Core Audio when audio devices are installed or removed from the system.

The AudioDeviceNotify project contains two Targets -- AudioDeviceNotify and AudioDeviceNotify2. The targets build samples that are exactly identical in functionality but differ in the implementation files they contain as described:

AppController.m demonstrates the above functionality using standard CoreAudio AudioObject APIs and is only included in the AudioDeviceNotify Target which builds AudioDeviceNotify.app AppController.mm demonstrates the above functionality using the Core Audio Utility Classes and is only included in the AudioDeviceNotify2 Target and builds AudioDeviceNotify2.app.

All source in the PublicUtility Group are only included in the AudioDeviceNotify2 project.

Having two implementations building separate targets yet performing the exact same task (one with and one without the use of Public Utility helpers) allows developers to easily compare and contrast how using the Core Audio Utility classes may be useful to simplify and speed up their work with the Core Audio APIs.

Core Audio Utility Classes download here: http://developer.apple.com/library/mac/#samplecode/CoreAudioUtilityClasses/Introduction/Intro.html

We recommend being completely familiar with the standard C APIs before jumping into the C++ Utility classes.

[Next](ReadMe.txt.md)

