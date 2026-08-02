---
title: AudioReflectorDriver
apple_id: DTS40008750
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: IOKit
published: '2009-04-21'
source_url: https://developer.apple.com/library/archive/samplecode/AudioReflectorDriver/Introduction/Intro.html
archived_at: '2026-07-18T03:01:28.898835Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AudioReflectorDriver

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2009-04-21 This project builds a kernel-based audio driver that reflects data going out one channel back to the corresponding input channel |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

This project builds a kernel-based audio driver that:

- builds for both Intel and PowerPC

- reflects data going out one channel back to the corresponding input channel

- has a completely configurable list of supported formats and stream layouts via it's Info.plist

- provides a dummy control for just about every standard kind control supported by the IOAudio family

- demonstrates how to localize strings

- includes a configurable time stamp generator to allow the simulation of various timing situations

- includes an integer-to-floating-point and floating-point-to-integer blitting library optimized for SSE3 on Intel processors and Altivec on PowerPC processors

[Next](ReadMe.txt.md)

