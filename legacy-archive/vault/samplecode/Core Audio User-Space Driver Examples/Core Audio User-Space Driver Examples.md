---
title: Core Audio User-Space Driver Examples
apple_id: DTS40013590
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2013-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/AudioDriverExamples/Introduction/Intro.html
archived_at: '2026-07-27T06:57:05.105608Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Core Audio User-Space Driver Examples

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2013-10-04 Fix to show the nominal sample rate and transport type in AMS. [(Full Revision History)](https://developer.apple.com/library/archive/samplecode/AudioDriverExamples/History/History.html#//apple_ref/doc/uid/DTS40013590-RevisionHistory-DontLinkElementID_1) |
| __Build Requirements:__ | OS X 10.9 or later, Xcode 5.0 & 10.9 SDK or later |
| __Runtime Requirements:__ | OS X 10.9 or later |

This project has two examples of writing user land audio drivers that conform to the plug-in API in <CoreAudio/AudioServerPlugIn.h>. Each example is documented with commentary inline with the code.

The first example, NullAudio, creates a driver that supports single audio device. Written in C, this example shows what it takes to write a drive that achieves the bare minimum of support while still being fully functional as an AudioDevice.

The second example, SimpleAudio, is a more functional driver. Written in C++, this driver is written for a dynamic environment where it has to support potentially many instances of the same device getting plugged into the system. This example also shows how a user-land driver interacts with hardware that requires a kernel extension to talk to. As such, it shows dealing with IOKit matching notifications as well as dealing with calls into the IOKit driver.

Note: An earlier version of this sample was called "User-Space Driver Reference". This updated version for OS X 10.9 and later contains bug fixes and the Null driver has added support for Audio Boxes.

[Next](ReadMe.txt.md)
