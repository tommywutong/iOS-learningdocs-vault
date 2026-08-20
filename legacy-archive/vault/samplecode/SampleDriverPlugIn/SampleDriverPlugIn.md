---
title: SampleDriverPlugIn
apple_id: DTS40008642
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDriverPlugIn/Introduction/Intro.html
archived_at: '2026-07-18T03:23:00.591181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SampleDriverPlugIn

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2009-04-15 This project illustrates implementing a plug-in for Core Audio HAL that conforms to the API in <CoreAudio/AudioDriverPlugIn.h> |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

This project illustrates implementing a plug-in to the Core Audio HAL that conforms to the API in <CoreAudio/AudioDriverPlugIn.h>.

The purpose of this kind of plug-in is to give IOAudio-based drivers a way to provide custom properties for their devices through the HAL's API. This API allows for the plug-in to override standard properties that do not affect I/O.

The plug-in the project implements the following:

- all the bundle entry points via the base class HP_DriverPlugIn.h

- a single device wide property called Foo whose value is a UInt32

- opening a connection to the IOAudioEngine in the driver and setting up a mach port to receive notifications from the engine

[Next](ReadMe.txt.md)

