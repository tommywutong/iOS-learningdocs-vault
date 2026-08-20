---
title: AVCustomEditOSX
apple_id: DTS40013408
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-07-26'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEditOSX/Introduction/Intro.html
archived_at: '2026-07-18T03:00:12.409135Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AVCustomEditOSX

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2013-07-26 Update custom compositor initialization. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbqhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.0 or later, Mac OS X v10.9 or later |
| __Runtime Requirements:__ | Mac OS X v10.9 or later |

A simple AVFoundation based movie editing application demonstrating custom compositing to add transitions. The sample demonstrates the use of custom compositors to add transitions to an AVMutableComposition. It implements the AVVideoCompositing and AVVideoCompositionInstruction protocols to have access to individual source frames, which are then be rendered using OpenGL off screen rendering. This sample is ARC-enabled.

[Next](ReadMe.txt.md)

