---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Introduction/Intro.html
archived_at: '2026-07-18T03:00:09.602093Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AVCustomEdit-main.m.md)

# AVCustomEdit

|  |  |
| --- | --- |
| __Last Revision:__ | Version 3.0, 2017-08-17 Added Swift target which renders the frames using Metal off screen rendering. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbrgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 8.3.3, iOS 10.3 SDK |
| __Runtime Requirements:__ | iOS 9.3.3 or later |

The sample demonstrates the use of custom compositors to add transitions to an AVMutableComposition. It implements the AVVideoCompositing and AVVideoCompositionInstruction protocols to have access to individual source frames, which are then be rendered using OpenGL or Metal off screen rendering.

[Next](AVCustomEdit-main.m.md)

