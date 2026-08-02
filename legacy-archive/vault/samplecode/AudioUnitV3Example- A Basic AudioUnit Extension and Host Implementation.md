---
title: 'AudioUnitV3Example: A Basic AudioUnit Extension and Host Implementation'
apple_id: TP40016185
resource_type: Sample Code
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-11-14'
source_url: https://developer.apple.com/library/archive/samplecode/AudioUnitV3Example/Introduction/Intro.html
archived_at: '2026-07-27T06:57:10.229828Z'
---
> 导航：[总目录](../README.md) · [samplecode](../_indexes/samplecode.md)



# AudioUnitV3Example: A Basic AudioUnit Extension and Host Implementation

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.5, 2016-11-14 Fixed DSPKernel.mm to handle late events, updated for Xcode 8.1 and fixed minor UI issues and storyboard constraints. [(Full Revision History)](https://developer.apple.com/library/archive/samplecode/AudioUnitV3Example/History/History.html#//apple_ref/doc/uid/TP40016185-RevisionHistory-DontLinkElementID_1) |
| __Build Requirements:__ | Xcode 8.1, iOS 9.3 SDK, macOS 10.11 SDK |
| __Runtime Requirements:__ | iOS 9.3+, macOS 10.11+ |

Demonstrates how to build functioning examples of two Audio Unit extensions and a simple Audio Unit host app for iOS and macOS with the version 3 Audio Unit APIs.

The Audio Unit Extensions API introduces a mechanism for developers to deliver Audio Units on both iOS and OS X using the same API and also provides a bridging mechanism for existing version 2 Audio Units and hosts allowing them to work with new version 3 Audio Units.

The targets in this sample are all prefixed by their respective platform designation, "iOS" or "OSX":

- FilterDemoApp, FilterDemoAppExtension - Effect Audio Unit
- InstrumentDemoApp, InstrumentDemoAppExtension - Instrument Audio Unit
- AUv3Host - Audio Unit Host
