---
title: avTouch
apple_id: DTS40008636
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-02-12'
source_url: https://developer.apple.com/library/archive/samplecode/avTouch/Introduction/Intro.html
archived_at: '2026-07-18T03:28:55.704560Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# avTouch

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.4.3, 2014-02-12 Updated for iOS 7 SDK. Removed use of deprecated AudioSession, now using AVAudioSession. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnrtgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 7.0 SDK |
| __Runtime Requirements:__ | iOS 7.0 or later |

The avTouch sample demonstrates use of the AVAudioPlayer class for basic audio playback.

The code in avTouch uses the AV Foundation framework to play a file containing AAC audio data. The application uses Core Graphics and OpenGL to display sound volume meters during playback.

This application shows how to:

\* Create an AVAudioPlayer object from an input audio file.

\* Use OpenGL and Core Graphics to display metering levels.

\* Use Audio Session Services to set an appropriate audio session category for playback.

\* Use the AVAudioPlayer interruption delegate methods to pause playback upon receiving an interruption, and to then resume playback if the interruption ends.

\* Demonstrates a technique to perform Fast Forward and Rewind

avTouch does not demonstrate how to play multiple files, nor does it demonstrate more advanced use of AV Foundation.

[Next](ReadMe.txt.md)

